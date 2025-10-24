from transformers import Trainer, TrainingArguments
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from transformers import DataCollatorForSeq2Seq
from datasets import load_dataset, load_from_disk
from textSummarizer.entity import ModelTrainerConfig
import torch
import os


class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    def train(self):
        
        device = "cuda" if torch.cuda.is_available() else "cpu"

        # Load tokenizer and model
        tokenizer = AutoTokenizer.from_pretrained(self.config.model_ckpt)
        model_pegasus = AutoModelForSeq2SeqLM.from_pretrained(self.config.model_ckpt).to(device)
        seq2seq_data_collator = DataCollatorForSeq2Seq(tokenizer, model=model_pegasus)

        # Load the dataset
        dataset_samsum_pt = load_from_disk(self.config.data_path)

        # Tokenize function
        def tokenize(batch):
            inputs = tokenizer(batch["dialogue"], padding="max_length", truncation=True, max_length=512)
            outputs = tokenizer(batch["summary"], padding="max_length", truncation=True, max_length=128)
            return {
                "input_ids": inputs["input_ids"],
                "attention_mask": inputs["attention_mask"],
                "labels": outputs["input_ids"]
            }

        # Apply tokenization
        dataset_samsum_pt = dataset_samsum_pt.map(tokenize, batched=True, remove_columns=["dialogue", "summary", "id"])

        # Training arguments
        trainer_args = TrainingArguments(
            output_dir=self.config.root_dir,
            num_train_epochs=1,
            per_device_train_batch_size=1,
            per_device_eval_batch_size=1,
            fp16=torch.cuda.is_available(),  # Enable mixed-precision training
            warmup_steps=500,
            weight_decay=0.01,
            logging_steps=10,
            save_steps=1000,
            gradient_accumulation_steps=16,
            remove_unused_columns=False,  # VERY IMPORTANT to avoid the ValueError
        )

        # Trainer
        trainer = Trainer(
            model=model_pegasus,
            args=trainer_args,
            tokenizer=tokenizer,
            data_collator=seq2seq_data_collator,
            train_dataset=dataset_samsum_pt["test"],
            eval_dataset=dataset_samsum_pt["validation"],
        )

        # Start training
        trainer.train()
        os.makedirs(self.config.root_dir, exist_ok=True)
        # Save model and tokenizer
        model_pegasus.save_pretrained(os.path.join(self.config.root_dir, "pegasus-samsum-model"))
        tokenizer.save_pretrained(os.path.join(self.config.root_dir, "tokenizer"))

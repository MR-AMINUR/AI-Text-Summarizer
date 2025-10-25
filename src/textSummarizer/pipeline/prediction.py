# from textSummarizer.config.configuration import ConfigurationManager
# from transformers import AutoTokenizer
# from transformers import pipeline

# class PredictionPipeline:
#     def __init__(self):
#         self.config = ConfigurationManager().get_model_evaluation_config

#     def predict(self, text):
#         tokenizer = AutoTokenizer.from_pretrained(self.config.tokenizer_path)
#         gen_kwargs = {"length_penalty": 0.8, "num_beams": 8, "max_length": 128}

#         pipe = pipeline("summarization", model=self.config.model_path, tokenizer=tokenizer)

#         print("Dialogue:")
#         print(text)

#         output = pipe(text, **gen_kwargs)[0]["summary_text"]
#         print("\nModel Summary:")
#         print(output)


#         return output

from transformers import pipeline
import torch

class PredictionPipeline:
    def __init__(self):
        # FORCE using the reliable pre-trained model
        print("Initializing reliable BART-large-cnn model...")
        self.pipe = pipeline(
            "summarization",
            model="facebook/bart-large-cnn",
            tokenizer="facebook/bart-large-cnn", 
            device=0 if torch.cuda.is_available() else -1
        )
        print("✓ Reliable model loaded successfully")

    def predict(self, text):
        """Generate quality summary using proven model"""
        try:
            # Clean text
            cleaned_text = text.replace('<file_gif>', '').replace('<file_photo>', '')
            cleaned_text = ' '.join(cleaned_text.split())
            
            print("Input Text:")
            print(text[:500] + "..." if len(text) > 500 else text)
            print(f"Text length: {len(text)} characters")

            # Use proven parameters for BART model
            summary = self.pipe(
                cleaned_text,
                max_length=150,
                min_length=50,
                do_sample=False,
                num_beams=4,
                length_penalty=2.0,
                early_stopping=True
            )[0]['summary_text']
            
            print("\nGenerated Summary:")
            print(summary)
            print(f"Summary length: {len(summary)} characters")

            return summary
            
        except Exception as e:
            print(f"Error: {e}")
            # Last resort - extract first and last sentences
            sentences = [s.strip() for s in text.split('.') if s.strip()]
            if len(sentences) >= 2:
                return f"{sentences[0]}. {sentences[-1]}."
            return text[:150] + "..." if len(text) > 150 else text
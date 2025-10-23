from textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from textSummarizer.pipeline.stage_02_data_validation import DataValidationPipeline
from textSummarizer.pipeline.stage_03_data_transformation import DataTransformationPipeline
from textSummarizer.pipeline.stage_04_model_trainer import  ModelTrainerTrainingPipeline
from textSummarizer.pipeline.stage_05_model_evaluation import  ModelEvaluationTrainingPipeline
from textSummarizer.logging import logger


# ===================== Stage 1: Data Ingestion =====================
STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
    data_ingestion = DataIngestionPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<<\n\nX==========x")
except Exception as e:
    logger.exception(e)
    raise e


# ===================== Stage 2: Data Validation =====================
STAGE_NAME = "Data Validation Stage"
try:
    logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
    data_validation = DataValidationPipeline()
    data_validation.main()
    logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<<\n\nX==========x")
except Exception as e:
    logger.exception(e)
    raise e


# ===================== Stage 3: Data Transformation =====================
STAGE_NAME = "Data Transformation Stage"
try:
    logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
    data_transformation = DataTransformationPipeline()
    data_transformation.main()
    logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<<\n\nX==========x")
except Exception as e:
    logger.exception(e)
    raise e


# ===================== Stage 4: Model Trainer =====================
STAGE_NAME = "Model Trainer Stage"
try:
    logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
    model_trainer = ModelTrainerTrainingPipeline()
    model_trainer.main()
    logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<<\n\nX==========x")
except Exception as e:
    logger.exception(e)
    raise e
# ===================== Stage 5: Model Evaluation stage =====================
STAGE_NAME = "Model Evaluation Stage"
try:
    logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
    model_evaluation = ModelEvaluationTrainingPipeline()
    model_evaluation.main()
    logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<<\n\nX==========x")
except Exception as e:
    logger.exception(e)
    raise e

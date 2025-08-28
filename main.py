# def main():
#     print("Hello from text-summarizer!")


# if __name__ == "__main__":
#     main()
from src.textSummarizer.logging import logging
from src.textSummarizer.pipeline.stage_1_data_ingestion import DataIngestionTrainingPipeline
from src.textSummarizer.pipeline.stage_2_data_transformation import DataTransformationPipeline
from src.textSummarizer.pipeline.stage_3_model_training import ModelTrainingPipeline
from src.textSummarizer.pipeline.stage_4_model_evaluation import ModelEvaluationPipeline

STAGE_NAME="Data Ingestion Stage"
try:
    logging.info(f"Stage {STAGE_NAME} initiated")
    data_ingestion_pipeline=DataIngestionTrainingPipeline()
    data_ingestion_pipeline.initiate_data_ingestion()
    logging.info(f"Stage {STAGE_NAME} Completed")
except Exception as e:
    logging.exception(e)

    
STAGE_NAME="Data Transformation Stage"
try:
    logging.info(f"Stage {STAGE_NAME} initiated")
    data_transformation_pipeline=DataTransformationPipeline()
    data_transformation_pipeline.initiate_data_transformation()
    logging.info(f"Stage {STAGE_NAME} Completed")
except Exception as e:
    logging.exception(e)

STAGE_NAME="Model Training Stage"
try:
    logging.info(f"Stage {STAGE_NAME} initiated")
    model_training_pipeline=ModelTrainingPipeline()
    model_training_pipeline.initiate_model_training()
    logging.info(f"Stage {STAGE_NAME} Completed")
except Exception as e:
    logging.exception(e)


STAGE_NAME="Model Evaluation Stage"
try:
    logging.info(f"Stage {STAGE_NAME} initiated")
    model_evaluation_pipeline=ModelEvaluationPipeline()
    model_evaluation_pipeline.initiate_model_evaluation()
    logging.info(f"Stage {STAGE_NAME} Completed")
except Exception as e:
    logging.exception(e)
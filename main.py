# def main():
#     print("Hello from text-summarizer!")


# if __name__ == "__main__":
#     main()
from src.textSummarizer.logging import logging
from src.textSummarizer.pipeline.stage_1_data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME="Data Ingestion Stage"
try:
    logging.info(f"Stage {STAGE_NAME} initiated")
    data_ingestion_pipeline=DataIngestionTrainingPipeline()
    data_ingestion_pipeline.initiate_data_ingestion()
    logging.info(f"Stage {STAGE_NAME} Completed")
except Exception as e:
    logging.exception(e)
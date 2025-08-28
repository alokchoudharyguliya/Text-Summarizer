from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
# Training
from transformers import DataCollatorForSeq2Seq
from transformers import TrainingArguments, Trainer
from src.textSummarizer.config.configuration import ModelTrainingConfig
import torch
from datasets import load_from_disk
class ModelTrainer:
    def __init__(self,config:ModelTrainingConfig):
        self.config=config
    def train(self):
        device="cuda" if torch.cuda.is_available() else "cpu"
        print(device)
        tokenizer=AutoTokenizer.from_pretrained(self.config.model_ckpt)
        model_pegasus=AutoModelForSeq2SeqLM.from_pretrained(self.config.model_ckpt).to(device)
        seq2seq_data_collator=DataCollatorForSeq2Seq(tokenizer,model=model_pegasus)
        
        dataset_samsum_pt=load_from_disk(self.config.data_path)
        trainer_args=TrainingArguments(
            output_dir='pegasus-samsum',num_train_epochs=1,warmup_steps=500,
            per_device_train_batch_size=1,per_device_eval_batch_size=1,
            weight_decay=0.01,logging_steps=10,
            eval_strategy='steps',eval_steps=500,save_steps=1e6,
            gradient_accumulation_steps=16
        )
        trainer=Trainer(model=model_pegasus,args=trainer_args,tokenizer=tokenizer,data_collator=seq2seq_data_collator,train_dataset=dataset_samsum_pt['test'],eval_dataset=dataset_samsum_pt['validation'])
        trainer.train()

        ## save model
        model_pegasus.save_pretrained("pegasus-samsum-model")
        tokenizer.save_pretrained("tokenizer")
import os,sys, logging as log

log_dir="logs"
logging_str="[%(asctime)s:%(levelname)s:%(module)s:%(message)s]"

log_filepath=os.path.join(log_dir,"continuous.log")

os.makedirs(log_dir,exist_ok=True)

log.basicConfig(
    level=log.INFO,
    format=logging_str,
    handlers=[
        log.FileHandler(log_filepath),
        log.StreamHandler(sys.stdout)
    ]
)
logging=log.getLogger("summarizerlogger")
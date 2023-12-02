import os
import sys
from pathlib import Path
import logging

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

#dir
log_dir = "logs"
# file
log_filepath = os.path.join(log_dir, "running_log")
os.makedirs(log_dir, exist_ok=True)


logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("ImageClassifierLogger")



import torch
from llms.configuration.prompts import PROMPTS

class Config:
    VDS_PATH = "MahmoodAnaam/OKVQA-Encoder-Violet-Captions"
    BDS_PATH = "MahmoodAnaam/OKVQA-VinVL-BiT-Captions"
    SPLIT = "validation"
    LANGUAGE = "ar"
    DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

    BATCH_SIZE = 20
    CAPTIONS = ["bit", "violet"]
    PROMPT_TEMPLATE = PROMPTS["default"]  # Use the "default" template

  

  

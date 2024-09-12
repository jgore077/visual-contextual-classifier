from transformers import AutoTokenizer,BertForSequenceClassification
from tqdm import tqdm
import requests
import torch
import os

# MODEL_URL throws ssl errors but I believe it is safe to supress warnings and use http
requests.packages.urllib3.disable_warnings() 
MODEL_URL="https://cs.usm.maine.edu/~behrooz.mansouri/visual_contextual_classifier/"
MODEL_FILE="model.safetensors"
MODEL_FILE_URL=MODEL_URL+MODEL_FILE
CONFIG="config.json"
MODEL_CONFIG_URL=MODEL_URL+CONFIG
MODEL_FOLDER="classifier/"

class VisualContextualClassifier():
    def __init__(self,tokenizer='bert-base-uncased') -> None:
        install_path=os.path.dirname(__file__)
        model_folder_path=os.path.join(install_path,MODEL_FOLDER)
        if not os.path.exists(model_folder_path):
            os.mkdir(model_folder_path)
            self._install(model_folder_path,[(MODEL_FILE_URL,MODEL_FILE),(MODEL_CONFIG_URL,CONFIG)])
        self.tokenizer=AutoTokenizer.from_pretrained(tokenizer,clean_up_tokenization_spaces=False)
        self.model=BertForSequenceClassification.from_pretrained(model_folder_path)
        
    def _install(self,path,files:list[tuple[str,str]]):
        for link,file_path in files:
            response=requests.get(link,verify=False,stream=True)
            total_size = int(response.headers.get("content-length", 0))
            block_size = 1024

            with tqdm(total=total_size, unit="B", unit_scale=True) as progress_bar:
                progress_bar.set_description(file_path)
                with open(os.path.join(path,file_path), "wb") as file:
                    for data in response.iter_content(block_size):
                        progress_bar.update(len(data))
                        file.write(data)

            if total_size != 0 and progress_bar.n != total_size:
                raise RuntimeError("Could not download file")
            
                
    def predict(self,input)->dict[str,float]:
        softmax=torch.nn.Softmax(dim=1)
        inputs = self.tokenizer(input, return_tensors="pt")
        outputs = self.model(**inputs)
        softmaxxed=torch.flatten(softmax(outputs.logits.data))
        return {
            "contextual":float(softmaxxed[0]),
            "visual":float(softmaxxed[1])
        }
        
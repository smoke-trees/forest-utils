import os
import json
import gdown
import torch
import zipfile
import transformers


class ModelFromTransformers(object):
    """
    A class for managing downloading and loading of transformers models.

    Attributes
    ----------
    base_url : str
        This is the base url for loading the required transformers model.
    url_id : str
        The complete url to the required transformers model.
    output : str
        Relative path to the output file for the downloaded model.
    zip : str
        Path to the zip file (by default it is 'model.zip').
    
    Methods
    -------
    _get_complete_url(url=""):
        Returns the complete url to the required transformers Model.
    _load_model():
        Downloads the model from the url to the output route and loads the model if successful, otherwise returns an error.

    """
    def __init__(self, output):
        """
        Constructs all the necessary attributes for the ModelFromTransformers Object.

        Parameter
        ----------
            output: Path to the 'output' file for saving the downloaded model.

        """
        super().__init__()
        
        self.base_url = 'https://drive.google.com/uc?id='
        self.url_id = self._get_complete_url(json.load(open('result.json','r'))["Link"])
        self.output = output
        self.zip = 'model.zip'
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.tokenizer, self.model = self._load_model()
        
    def _get_complete_url(self, url):
        """
        Returns the complete url for downloading the required transformers model.

        Parameter
        ---------
            url : The google drive link extracted from the 'result.json' file

        """
        split_url = url.split('/')
        return self.base_url + split_url[5]
        
    def _load_model(self, force_download = False):
        """
        Returns the downloaded model stored in 'output' file if model is downloaded successfully, 
        otherwise returns an error message.
        """

        try:
            if(not os.path.exists(self.zip) or force_download):
                gdown.download(self.url_id, self.zip, quiet = False)
            if not os.path.exists(self.output):
                with zipfile.ZipFile(self.zip, 'r') as zip_ref:
                    zip_ref.extractall()
            return transformers.AutoTokenizer.from_pretrained(self.output + "/tokenizer"), transformers.AutoModelWithLMHead.from_pretrained(self.output + "/model").to(self.device)
        except:
            print("[ERROR]:Error in loading model, please check downloaded file")
            
    def predict(self, sentence):
        
        with torch.no_grad():
            vector = self.model(torch.tensor(self.tokenizer.encode(sentence, add_special_tokens = True)).to(self.device).unsqueeze(0))[0].cpu().numpy().tolist()
        return vector

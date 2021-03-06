import os
import json
import gdown
import torch
import zipfile
import transformers


class ModelFromTransformerWithLMHead(object):
    """
    A class for managing downloading and loading of transformer language model.

    Attributes
    ----------
    base_url : str
        This is the base url for loading the required transformer language model.
    url_id : str
        The complete url to the required transformer language model.
    output : str
        Relative path to the output file for the downloaded model.
    zip : str
        Path to the zip file (by default it is 'model.zip').
    
    Methods
    -------
    _get_complete_url(url=""):
        Returns the complete url to the required transformers language model.
    _load_model():
        Downloads the model from the url to the output route and loads the model if successful, otherwise returns an error.

    """
    def __init__(self, output):
        """
        Constructs all the necessary attributes for the ModelFromTransformerWithLMHead Object.

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
        Returns the complete url for downloading the required transformers language model.

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
            return transformers.AutoTokenizer.from_pretrained(self.output), transformers.AutoModelWithLMHead.from_pretrained(self.output).to(self.device)
        except:
            print("[ERROR]:Error in loading model, please check downloaded file")
            
    def predict(self, sentence):
        
        with torch.no_grad():
            vector = self.model(torch.tensor(self.tokenizer.encode(sentence, add_special_tokens = True)).to(self.device).unsqueeze(0))
        return vector
    
    def fill_mask(self, sentence):
        
        nlp_fill = transformers.pipeline('fill-mask', model = self.model.to('cpu'), tokenizer = self.tokenizer)
        return nlp_fill(sentence + nlp_fill.tokenizer.mask_token)
    

class ModelFromTransformerForClassification(object):
    """
    A class for managing downloading and loading of transformer model for classification.

    Attributes
    ----------
    base_url : str
        This is the base url for loading the required transformer model for classification.
    url_id : str
        The complete url to the required transformer model for classification.
    output : str
        Relative path to the output file for the downloaded model.
    zip : str
        Path to the zip file (by default it is 'model.zip').
    
    Methods
    -------
    _get_complete_url(url=""):
        Returns the complete url to the required transformer model for classification.
    _load_model():
        Downloads the model from the url to the output route and loads the model if successful, otherwise returns an error.

    """
    def __init__(self, output):
        """
        Constructs all the necessary attributes for the ModelFromTransformerForClassification Object.

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
        Returns the complete url for downloading the required transformer model for classification.

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
            return transformers.AutoTokenizer.from_pretrained(self.output), transformers.AutoModelForSequenceClassification.from_pretrained(self.output).to(self.device)
        except:
            print("[ERROR]:Error in loading model, please check downloaded file")
        
    
    def predict(self, sentence):
        
        nlp_classif = transformers.pipeline('sentiment-analysis', model = self.model.to('cpu'), tokenizer = self.tokenizer)
        return nlp_classif(sentence)[0]['label']
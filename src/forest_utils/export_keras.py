import os
import json
import gdown
import zipfile

import tensorflow as tf


class ModelFromH5(object):
    """
    A class for managing downloads and loading of .h5 models

    Parameters
    ----------
    output : str
        path to output file for downloading the model (by default it is 'model.h5')
    
    Attributes
    ----------
    base_url : str
        This is the bace url for downloading the .h5 model files
    url_id 
        Contains the link to the model extracted from the results.json files
    output : str
        Relative path to the output file for the model download

    Methods
    -------
    _get_complete_url(url)
        method to get complete link from the given url
    _load_model()
        download the model .h5 file from the url to output route and returns the loaded keras model
    """

    def __init__(self, output = 'model.h5'):
        super().__init__()
        
        self.base_url = 'https://drive.google.com/uc?id='
        self.url_id = self._get_complete_url(json.load(open('result.json', 'r'))['Link'])
        self.output = output
        self.model = self._load_model()
        
    def _get_complete_url(self, url):
        """
        method (used internally inside class) to get complete link (including base_url) from the given url

        Parameters
        ----------
        url : str
            url of the model
        
        Returns
        -------
        link : str
            complete url to the model file

        """
        split_url = url.split('/')
        return self.base_url + split_url[5]
        
    def _load_model(self, force_download = False):
        """
        method to download model from the url to the output file and load it into keras

        Returns 
        -------
        keras model
            downloaded model loaded into keras model ready to use!
        """
        try:
            if(not os.path.exists(self.output) or force_download):
                gdown.download(self.url_id, self.output, quiet = False)
            return tf.keras.models.load_model(self.output)
        except:
            print("[ERROR]:Error in loading model, please check downloaded file")
    

    
class ModelFromSavedModel(object):
    """
    A class for managing downloading and loading of tf models.

    Attributes
    ----------
    base_url : str
        This is the base url for loading the required tf model.
    url_id : str
        The complete url to the required tf model.
    output : str
        Relative path to the output file for the downloaded model.
    zip : str
        Path to the zip file (by default it is 'model.zip').
    
    Methods
    -------
    _get_complete_url(url=""):
        Returns the complete url to the required tf Model.
    _load_model():
        Downloads the model from the url to the output route and loads the model if successful, otherwise returns an error.

    """
    def __init__(self, output):
        """
        Constructs all the necessary attributes for the ModelFromSavedModel Object.

        Parameter
        ----------
            output: Path to the 'output' file for saving the downloaded model.

        """
        super().__init__()
        
        self.base_url = 'https://drive.google.com/uc?id='
        self.url_id = self._get_complete_url(json.load(open('result.json','r'))["Link"])
        self.output = output
        self.zip = 'model.zip'
        self.model = self._load_model()
        
    def _get_complete_url(self, url):
        """
        Returns the complete url for downloading the required tf model.

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
            return tf.keras.models.load_model(self.output)
        except:
            print("[ERROR]:Error in loading model, please check downloaded file")


class ModelFromCheckpoint(object):
    """
    A class for managing downloading and loading of tf models.

    Attributes
    ----------
    base_url : str
        This is the base url for loading the required tf model.
    url_id : str
        The complete url to the required tf model.
    output : str
        Relative path to the output file for the downloaded model.
    zip : str
        Path to the zip file (by default it is 'model.zip').
    
    Methods
    -------
    _get_complete_url(url=""):
        Returns the complete url to the required tf Model.
    _load_model():
        Downloads the model from the url to the output route and loads the model if successful, otherwise returns an error.

    """
    def __init__(self, model_obj, optimizer):
        """
        Constructs all the necessary attributes for the ModelFromSavedCheckpoint Object.

        Parameter
        ----------
            output: Path to the 'output' file for saving the downloaded model.

        """
        super().__init__()
        
        self.base_url = 'https://drive.google.com/uc?id='
        self.url_id = self._get_complete_url(json.load(open('result.json','r'))["Link"])
        self.output = "checkpoints"
        self.zip = 'model.zip'
        self.model_obj = model_obj
        self.optimizer = optimizer
        self.model = self._load_model()
        
    def _get_complete_url(self, url):
        """
        Returns the complete url for downloading the required tf model.

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
            checkpoint_path = "checkpoints"

            ckpt = tf.train.Checkpoint(transformer = self.model_obj,
                                       optimizer = self.optimizer)
            
            ckpt_manager = tf.train.CheckpointManager(ckpt, checkpoint_path, max_to_keep = 1)
            
            if ckpt_manager.latest_checkpoint:
              ckpt.restore(ckpt_manager.latest_checkpoint)
              print ('[INFO]:Latest checkpoint restored!')
            return self.model_obj
        except:
            print("[ERROR]:Error in loading model, please check downloaded file")

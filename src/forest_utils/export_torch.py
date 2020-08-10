import os
import json
import gdown
import zipfile
import torch


class ModelFromPt(object):
    """
    A class for managing downloads and loading of pt models

    Parameters
    ----------
    output : str
        path to output file for downloading the model (by default it is 'model.pt')

    Attributes
    ----------
    base_url : str
        This is the base url for downloading the .h5 model files
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

    def __init__(self, output='model.pt'):
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

    def _load_model(self, force_download=False):
        """
        method to download model from the url to the output file and load it into keras

        Returns
        -------
        keras model
            downloaded model loaded into keras model ready to use!
        """
        try:
            if (not os.path.exists(self.output) or force_download):
                gdown.download(self.url_id, self.output, quiet=False)
            model = torch.load(self.output)
            model.eval()
            return model
        except:
            print("[ERROR]:Error in loading model, please check downloaded file")

class ModelFromState_Dict(object):
    """
        Class for loading only state_dicts of models. In order to use this class the user
        needs to construct the architecture of the model in his code.

        Parameters
        ----------
        output : str
            path to output file for downloading the state_dict (by default it is 'model.pt')

        Attributes
        ----------
        base_url : str
            This is the base url for downloading the state_dict files
        url_id
            Contains the link to the model extracted from the results.json files
        output : str
            Relative path to the output file for the model download

    """
    def __init__(self,output="model.pt"):
        print("You are loading state_dict of the model... please make sure you define the model architecture\
         in code")
        self.base_url = 'https://drive.google.com/uc?id='
        self.url_id = self._get_complete_url(json.load(open('result.json', 'r'))['Link'])
        self.output = output
        self.state_dict = self._load_state_dict()


    def _get_complete_url(self, url):
        """
        method (used internally inside class) to get complete link (including base_url) from the given url

        Parameters
        ----------
        url : str
            url of the state_dict

        Returns
        -------
        link : str
            complete url to the state_dict file

        """
        split_url = url.split('/')
        return self.base_url + split_url[5]


    def _load_state_dict(self, force_download=False):
        """
        method to download model from the url to the output file and load it into keras

        Returns
        -------
        keras model
            downloaded model loaded into keras model ready to use!
        """
        try:
            if (not os.path.exists(self.output) or force_download):
                gdown.download(self.url_id, self.output, quiet=False)
            state_dict = torch.load(self.output)

            return state_dict
        except:
            print("[ERROR]:Error in loading state dict, please check downloaded file")





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
        self.url_id = self._get_complete_url(json.load(open('result.json', 'r'))["Link"])
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


    def _load_model(self, force_download=False):
        """
        Returns the downloaded model stored in 'output' file if model is downloaded successfully,
        otherwise returns an error message.
        """

        try:
            if (not os.path.exists(self.zip) or force_download):
                gdown.download(self.url_id, self.zip, quiet=False)
            if not os.path.exists(self.output):
                with zipfile.ZipFile(self.zip, 'r') as zip_ref:
                    zip_ref.extractall()
            return torch.load(self.output)
        except:
            print("[ERROR]:Error in loading model, please check downloaded file")

class ModelFromSavedState_Dict(object):
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
        self.url_id = self._get_complete_url(json.load(open('result.json', 'r'))["Link"])
        self.output = output
        self.zip = 'model.zip'
        self.state_dict = self._load_state_dict()


    def _get_complete_url(self, url):
        """
        Returns the complete url for downloading the required tf model.

        Parameter
        ---------
            url : The google drive link extracted from the 'result.json' file

        """
        split_url = url.split('/')
        return self.base_url + split_url[5]


    def _load_state_dict(self, force_download=False):
        """
        Returns the downloaded state_dict stored in 'output' file if model is downloaded successfully,
        otherwise returns an error message.
        """

        try:
            if (not os.path.exists(self.zip) or force_download):
                gdown.download(self.url_id, self.zip, quiet=False)
            if not os.path.exists(self.output):
                with zipfile.ZipFile(self.zip, 'r') as zip_ref:
                    zip_ref.extractall()
            return torch.load(self.output)
        except:
            print("[ERROR]:Error in loading model, please check downloaded file")




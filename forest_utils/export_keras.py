import os
import json
import gdown

import tensorflow as tf


class ModelFromH5(object):
    """
    A class for managing downloads and loading of .h5 models

    Parameters
    ----------
    output : str
        path to output file for downloading the model (by default it is 'model.h5')
    config : str
        path to the config file of the model (by default it is 'result.json')

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

    def __init__(self, output='model.h5', config='result.json'):
        super().__init__()

        self.base_url = 'https://drive.google.com/uc?id='
        self.url_id = self._get_complete_url(
            json.load(open('result.json', 'r'))['Link'])
        self.output = output

    def _get_complete_url(self, url):
        """
        method (used internally inside class) to get complete link (including base_url) from the given url

        Parameters
        ----------
        url : str
            url to split and make complete url from

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

        Parameter
        ---------
        force_download: bool
            Forces to redownload  the model default(False)

        Returns 
        -------
        keras model
            downloaded model loaded into keras model ready to use!
        """
        try:
            if(not os.path.exists(self.output) or force_download):
                gdown.download(self.url_id, self.output, quiet=False)
            return tf.keras.models.load_model(self.output)
        except:
            print("[ERROR]:Error in loading model, please check downloaded file")

    def __call__(self, force_download=False):
        """
        method to download model from the url to the output file and load it into keras

        Parameter
        ---------
        force_download: bool
            Forces to redownload  the model default(False)
        Returns 
        -------
        keras model
            downloaded model loaded into keras model ready to use!
        """
        return self._load_model(force_download=force_download)

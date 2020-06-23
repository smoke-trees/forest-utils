
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 05:49:08 2020

@author: tanmay
"""

import json
import gdown
import spacy
import zipfile


class ModelFromSpacy(object):
    """
    A class for managing downloading and loading of spaCy models.

    Attributes
    ----------
    base_url : str
        This is the base url for loading the required spaCy model.
    url_id : str
        The complete url to the required spaCy model.
    output : str
        Relative path to the output file for the downloaded model.
    zip : str
        Path to the zip file (by default it is 'model.zip').
    
    Methods
    -------
    get_complete_url(url=""):
        Returns the complete url to the required spaCy Model.
    load_model():
        Downloads the model from the url to the output route and loads the model if successful, otherwise returns an error.

    """
    def __init__(self, output):
        """
        Constructs all the necessary attributes for the ModelFromSpacy Object.

        Parameter
        ----------
            output: Path to the 'output' file for saving the downloaded model.

        """
        super().__init__()
        
        self.base_url = 'https://drive.google.com/uc?id='
        self.url_id = self.get_complete_url(json.load(open('result.json','r'))["Link"])
        self.output = output
        self.zip = 'model.zip'
        
    def get_complete_url(self, url):
        """
        Returns the complete url for downloading the required spaCy model.

        Parameter
        ---------
            url : The google drive link extracted from the 'result.json' file

        """
        split_url = url.split('/')
        return self.base_url + split_url[5]
        
    def load_model(self):
        """
        Returns the downloaded model stored in 'output' file if model is downloaded successfully, 
        otherwise returns an error message.
        """

        try:
            gdown.download(self.url_id, self.zip, quiet = False)
            with zipfile.ZipFile(self.zip, 'r') as zip_ref:
                zip_ref.extractall()
            return spacy.load(self.output)
        except:
            print("[ERROR]:Error in loading model, please check downloaded file")


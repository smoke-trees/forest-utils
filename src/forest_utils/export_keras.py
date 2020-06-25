#!/usr/bin/env python3
# -*- coding: utf-8 -*-

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
    get_complete_url(url)
        method to get complete link from the given url
    load_model()
        download the model .h5 file from the url to output route and returns the loaded keras model
    """

    def __init__(self, output = 'model.h5', config = 'result.json'):
        super().__init__()
        
        self.base_url = 'https://drive.google.com/uc?id='
        self.url_id = self.check_for_json(config)
        self.check_for_url_id(self.url_id)
        self.output = output
        
    def check_for_url_id(self, url):
        if url!=False and url!='':
            print('Link found !!')
        else:
            return
        
    def check_for_json(self, path):
        if os.path.isfile(path):
            try:
                with open(os.path.join(os.getcwd(),path), encoding='utf-8') as file:
                    content = file.read()
                    link = json.loads(content)["Link"]
                    return link
            except:
                print("Link not found!!")
                return False
        else:
            print("File do not exists")
            return False
        
    def get_complete_url(self, url):
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
        
    def load_model(self):
        """
        method to download model from the url to the output file and load it into keras

        Returns 
        -------
        keras model
            downloaded model loaded into keras model ready to use!
        """
        try:
            gdown.download(self.url_id, self.output, quiet = False)
            return tf.keras.models.load_model(self.output)
        except:
            print("Download error occured")
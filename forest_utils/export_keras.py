#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import gdown

import tensorflow as tf


class ModelFromH5(object):
    
    def __init__(self, output = 'model.h5'):
        super().__init__()
        
        self.base_url = 'https://drive.google.com/uc?id='
        self.url_id = self.get_complete_url(json.load(open('result.json','r'))["Link"])
        self.output = output
        
    def get_complete_url(self, url):
        split_url = url.split('/')
        return self.base_url + split_url[5]
        
    def load_model(self):
        try:
            gdown.download(self.url_id, self.output, quiet = False)
            return tf.keras.models.load_model(self.output)
        except:
            print("Download error occured")
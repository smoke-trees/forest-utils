#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

import json
import gdown

import tensorflow as tf


class ModelFromH5(object):
    
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
                link = json.load(open(path))["Link"]
            except:
                print("Link not found!!")
                return False
        else:
            print("File do not exists")
            return False
        
    def get_complete_url(self, url):
        split_url = url.split('/')
        return self.base_url + split_url[5]
        
    def load_model(self):
        try:
            gdown.download(self.url_id, self.output, quiet = False)
            return tf.keras.models.load_model(self.output)
        except:
            print("Download error occured")
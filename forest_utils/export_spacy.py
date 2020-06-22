#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import gdown
import spacy
import zipfile


class ModelFromSpacy(object):
    
    def __init__(self, output):
        super().__init__()
        
        self.base_url = 'https://drive.google.com/uc?id='
        self.url_id = self.get_complete_url(json.load(open('result.json','r'))["Link"])
        self.output = output
        self.zip = 'model.zip'
        
    def get_complete_url(self, url):
        split_url = url.split('/')
        return self.base_url + split_url[5]
        
    def load_model(self):
        try:
            gdown.download(self.url_id, self.zip, quiet = False)
            with zipfile.ZipFile(self.zip, 'r') as zip_ref:
                zip_ref.extractall()
            return spacy.load(self.output)
        except:
            print("[ERROR]:Error in loading model, please check downloaded file")
import os
import gdown
import pickle

import pandas as pd


class Datasets(object):
    """
    A class for managing downloads and loading of SmokTrees' datasets
    """

    def __init__(self, output = 'datasets.pickle', config = 'result.json'):
        super().__init__()
        
        self.base_url = 'https://drive.google.com/uc?id='
        self.url_id = self.get_complete_url('https://drive.google.com/file/d/10G-d7rdIHsQ9s8XE1mgs6t-hfQjVD-KA/view?usp=sharing')
        self.output = output
        
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
    
    def get_emo_tweets(self, force_download = False):
        try:
            if(not os.path.exists(self.output) or force_download):
                gdown.download(self.url_id, self.output, quiet = False)
            if(not os.path.exists('tweets.csv') or force_download): 
                gdown.download(self.get_complete_url(pickle.load(open(self.output, 'rb'))['emotion_tweets']['link']), 'tweets.csv', quiet = False)
            return pd.read_csv('tweets.csv')
        except:
            print("[ERROR]:Error in loading dataset, please check downloaded file")
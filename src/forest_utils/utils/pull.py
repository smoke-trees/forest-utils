import requests
import wget

def get_model_from_zoo(modelname):
    res = wget.download(modelname)
    print(res)
    
get_model_from_zoo('https://github.com/smoke-trees/model-zoo/tree/master/CORD-Spacy-word2vec')
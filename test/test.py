import tf_module

url = 'Enter_url_here'

download = tf_module.model_from_h5(url)

download.download_model()
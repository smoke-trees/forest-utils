## Forest Utils package for smoketrees model zoo

This package will be useful for carrying out all the utilities of the SmokeTrees Model Zoo lovingly called SmokeTrees Forest.`

## Features

- [X] Pull down HDF5 (.h5) models from the zoo and load with keras
- [X] Pull down the spacy model from the zoo

> Package is under test before being published to PyPI

## Steps to install the package from source code

- Clone the repo by the following command
    ``` bash
        git clone https://github.com/smoke-trees/forest-utils.git
    ```
- Change the directory to the package 
    ``` bash
        cd forest-utils
    ```
- Execute the following command
    ``` bash
        pip install -e .
    ```

## Example Usage 

- Load Model using Tensorflow

``` Python
    from forest_utils import export_keras

    model = export_keras.ModelFromH5().load_model()
```

- Load Dataset

``` Python
    from forest_utils import datasets

    tweets = datasets.Dataset().get_emo_tweets()
```

After pulling down the model use it for predictions and other evalutaion functionalities.
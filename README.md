## Forest Utils package for smoketrees model zoo

This package will be useful for carrying out all the utilities of the model zoo.`

## Features

- [X] Pull down HDF5 (.h5) models from the zoo and load with keras
- [X] Pull down the spacy model from the zoo

## Steps to install the package

``` bash
    pip install forest_utils
```

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

``` Python
    from forest_utils import export_keras

    export_url = '<url where model is hosted>'
    model = export_keras.model_from_h5(export_url)
```
After pulling down the model use it for predictions and other evalutaion functionalities.
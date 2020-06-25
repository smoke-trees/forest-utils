import sys

sys.path.append('../src/')
from forest_utils import export_keras


model = export_keras.ModelFromH5()

print(model.load_model())
import utils
from config import load_config, log_config
from dataset import loadMatlabDataset
import models
import training
from checkpoint import save_model_weights, load_model_weights
import tensorflow as tf
import numpy as np
import os

def get_file_size(file_path):
    size = os.path.getsize(file_path)
    return size
    
def convert_bytes(size, unit=None):
    if unit == "KB":
        return print('File size: ' + str(round(size / 1024, 3)) + ' Kilobytes')
    elif unit == "MB":
        return print('File size: ' + str(round(size / (1024 * 1024), 3)) + ' Megabytes')
    else:
        return print('File size: ' + str(size) + ' bytes')

def representative_dataset():    
    for i in range(128):
        yield [X_train[i:i+1].astype(np.float32)]

settings = load_config('base_config.yaml')
utils.print_dictionary(settings)

X_train, Y_train, X_test, Y_test, encoder, metadata = loadMatlabDataset(settings['dataset'])
print(X_train.shape, '\n', Y_train.shape)

model_cfg = settings['model']
model_cfg.update({'input_shape': (metadata['observations'], 1), 'output_shape': metadata['classes']})

utils.print_dictionary(model_cfg)

experiment_path = utils.set_timestamp_dir()
log_config(settings, experiment_path)

model = models.build_model(settings['model'])
model = load_model_weights(model, 'run_08_13-21_28')

model = training.evaluate(model, X_test, Y_test, metadata['categories'])

print("*** TFLite Conversion ***")
converter = tf.lite.TFLiteConverter.from_keras_model(model)
converter.optimizations = [tf.lite.Optimize.DEFAULT]

converter.representative_dataset = representative_dataset

converter.target_spec.supported_ops = [tf.lite.OpsSet.TFLITE_BUILTINS_INT8]
converter.inference_input_type = tf.uint8
converter.inference_output_type = tf.uint8

quantized_model = converter.convert()

model_path = experiment_path / "model.tflite"
with open(model_path, "wb") as f:
    f.write(quantized_model)

convert_bytes(get_file_size(model_path), "MB")


X_testi = (X_test - X_test.min()) / (X_test.max() - X_test.min())
X_testi *= 255.0
X_testi = np.array(X_testi, dtype=np.uint8)

training.evaluate_tflite(model_path, X_testi, Y_test, metadata['categories'])


#model = training.train(model, settings['training'], X_train, Y_train, X_test, Y_test)
#

#save_model_weights(model, experiment_path)
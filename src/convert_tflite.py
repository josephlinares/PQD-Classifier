import utils
from config import load_config, log_config
from dataset import loadMatlabDataset, scale_dataset
from models import build_model
import training
from checkpoint import save_model_weights
import tensorflow as tf
import numpy as np
import os

from conversion import convert_to_tflite
from checkpoint import save_model_tflite

settings = load_config('base_config.yaml')
utils.print_dictionary(settings)

X_train, Y_train, X_test, Y_test, encoder, metadata = loadMatlabDataset(settings['dataset'])

model_cfg = settings['model']
model_cfg.update({'input_shape': (metadata['observations'], 1), 'outputs': metadata['classes']})
model_cfg.update({'categories' : (metadata['categories'])})

utils.print_dictionary(model_cfg)

weights_path = utils.MODELS_DIR / 'run_08_16-20_33' / 'model.weights.h5'
experiment_path = utils.set_timestamp_dir()
model_path = experiment_path / "model.tflite"
log_config(settings, experiment_path)

model = build_model(settings['model'])
model.load_weights(weights_path)

training.evaluate(model, X_test, Y_test, metadata['categories'])

quantized_model = convert_to_tflite(model, X_train)
save_model_tflite(quantized_model, experiment_path)

X_testi = scale_dataset(X_test)

interpreter = tf.lite.Interpreter(model_path = model_path)
training.evaluate_tflite(interpreter, X_testi, Y_test, settings['model'], experiment_path) 


#model = training.train(model, settings['training'], X_train, Y_train, X_test, Y_test)
#

#save_model_weights(model, experiment_path)
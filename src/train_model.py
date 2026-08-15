import utils
from config import load_config, log_config
from dataset import loadMatlabDataset
import models
import training
from checkpoint import save_model_weights

settings = load_config('base_config.yaml')
utils.print_dictionary(settings)

X_train, Y_train, X_test, Y_test, encoder, metadata = loadMatlabDataset(settings['dataset'])
print(X_train.shape)
print(Y_test)

model_cfg = settings['model']
model_cfg.update({'input_shape': (metadata['observations'], 1), 'outputs': metadata['classes']})


utils.print_dictionary(model_cfg)

experiment_path = utils.timestamp_dir()
log_config(settings, experiment_path)

model = models.build_model(settings['model'])
model = training.train(model, settings['training'], X_train, Y_train, X_test, Y_test)
model = training.evaluate(model, X_test, Y_test, metadata['categories'], experiment_path)

save_model_weights(model, experiment_path)
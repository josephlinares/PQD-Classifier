from utils import print_dictionary, set_timestamp_dir
from config import load_config, log_config
from dataset import loadMatlabDataset
from models import build_model
from training import train, evaluate
from checkpoint import save_model_weights

settings = load_config()
print_dictionary(settings)

X_train, Y_train, X_test, Y_test, encoder, metadata = loadMatlabDataset(settings['dataset'])

model_cfg = settings['model']
model_cfg.update({'input_shape': (metadata['observations'], 1), 'outputs': metadata['classes']})

print_dictionary(model_cfg)

experiment_path = set_timestamp_dir()
log_config(settings, experiment_path)

model = build_model(settings['model'])
model = train(model, settings['training'], X_train, Y_train, X_test, Y_test, experiment_path)
evaluate(model, X_test, Y_test, metadata['categories'], experiment_path)

save_model_weights(model, experiment_path)
from pathlib import Path
from utils import convert_bytes, get_file_size

def save_model_weights(model, filepath : Path):
    model.save_weights(filepath / 'model.weights.h5')
    print(f"Weights saved to {filepath}")

def save_model_tflite(model, filepath : Path):
    with open(filepath / 'model.tflite', "wb") as f:
        f.write(model)

    convert_bytes(get_file_size(filepath), "MB")
import keras.models
from pathlib import Path

def save_model_weights(model, filepath : Path):
    model.save_weights(filepath / 'model.weights.h5')
    print(f"Weights saved to {filepath}")
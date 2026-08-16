import numpy as np
import keras
from keras import Sequential
from keras.layers import Input, Conv1D, MaxPool1D, BatchNormalization, GlobalMaxPooling1D, Flatten, Dense
from keras.optimizers import Nadam, AdamW, SGD

# Not supported at the time
class LiteratureCNN(keras.Model):
    """Keras Model for 1D-CNN described in
    open-source dataset generator paper"""

    def __init__(self, num_classes: int = 16, input_shape: int = 533, 
                 k_size: int = 3, stride: int = 1, learning_rate: float = 0.01, **kwargs):
        super(LiteratureCNN, self).__init__()

        self.learning_rate = learning_rate
        self.architecture = keras.Sequential([
            Input(shape=(input_shape, 1)),

            Conv1D(filters=32, kernel_size=k_size, strides=stride, activation='relu'),
            Conv1D(filters = 32, kernel_size=k_size, strides=stride, activation='relu'),
            MaxPool1D(pool_size=3, strides = 1),

            Conv1D(filters = 64, kernel_size=k_size, strides=stride, activation='relu'),
            Conv1D(filters = 64, kernel_size=k_size, strides=stride, activation='relu'),
            MaxPool1D(pool_size=(3), strides = 1),

            Conv1D(filters = 128, kernel_size=k_size, strides=stride, activation='relu'),
            Conv1D(filters = 128, kernel_size=k_size, strides=stride, activation='relu'),
            GlobalMaxPooling1D(),

            BatchNormalization(),
            Flatten(),
            Dense(units=256, activation='relu',use_bias=True),
            Dense(units=128, activation='relu',use_bias=True),
            BatchNormalization(),
            Dense(units=num_classes, activation='softmax',use_bias=True)
        ])

        self.print_layers()

    def scheduler(self, epoch):
        """
        Compute the learning rate for the current epoch
        """
        dropEvery = 10
        initAlpha = self.learning_rate
        factor = 0.5
        exp = np.floor((1 + epoch) / dropEvery)
        alpha = initAlpha * (factor ** exp)
        print('lr =', alpha)
        return float(alpha)

    def print_layers(self):
        for layer in self.layers:
            print(layer.name, type(layer))
            if isinstance(layer, keras.Sequential):
                layer.summary()

    def call(self, inputs):
        return self.architecture(inputs)

def build_model(cfg: dict):
    # learning rates and weight decays should be passed in optimizers
    optimizer_config = cfg['optimizer']

    if optimizer_config == 'nadam':
        optimizer = Nadam()
    elif optimizer_config == 'adamw':
        optimizer = AdamW()
    else:
        optimizer = SGD()

    if cfg['loss_function'] == 'cross-entropy':
        loss_function = 'categorical_crossentropy'
    if cfg['name'] == 'LiteratureCNN':
        model = literature_cnn(
        cfg['input_shape'],
        cfg['outputs'], 
        cfg['kernel_size'],
        cfg['stride'])

        model.compile(loss=loss_function,
                      optimizer=optimizer,
                      metrics=['accuracy'])

    return model

def literature_cnn(input_shape: tuple=(533, 1), outputs: int=16, 
                   k_size: int = 3, stride: int = 1):
    model = Sequential([
        Input(shape=input_shape),
        Conv1D(filters=32, kernel_size=k_size, strides=stride, activation='relu'),
        Conv1D(filters = 32, kernel_size=k_size, strides=stride, activation='relu'),
        MaxPool1D(pool_size=3, strides = 1),
        Conv1D(filters = 64, kernel_size=k_size, strides=stride, activation='relu'),
        Conv1D(filters = 64, kernel_size=k_size, strides=stride, activation='relu'),
        MaxPool1D(pool_size=(3), strides = 1),
        Conv1D(filters = 128, kernel_size=k_size, strides=stride, activation='relu'),
        Conv1D(filters = 128, kernel_size=k_size, strides=stride, activation='relu'),
        GlobalMaxPooling1D(),
        BatchNormalization(),
        Flatten(),
        Dense(units=256, activation='relu',use_bias=True),
        Dense(units=128, activation='relu',use_bias=True),
        BatchNormalization(),
        Dense(units=outputs, activation='softmax',use_bias=True)
    ])
    return model

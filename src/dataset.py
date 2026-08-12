import numpy as np
from scipy.io import loadmat

import yaml
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split

def loadMatlabDataset(settings: dict):
    filename = settings['filename']
    # YAML creates a tuple (0.10,)
    test_percentage = settings['test_percentage']
    seed_random = settings['seed_random']

    print(f'Loading dataset from {filename}')
    dataset = loadmat(filename)
    dataset = dataset['SignalsDataBase'][0]

    X = [None]
    Y = [None]

    for sample in dataset:
        X.append(sample['signals'][0])
        Y.append(sample['labels'][0])

    # Create numpy array and reshape it
    X = np.array(X[1:])
    Y = np.array(Y[1:])
    X = np.expand_dims(X, axis=-1)
    Y = np.reshape(Y, (len(Y), 1))
    print(f'Successfully read {X.shape[0]} samples')

    Y_encoded, encoder = encodeDataset(Y)

    X_train, X_test, Y_train, Y_test = train_test_split(
        X,
        Y_encoded,
        test_size=test_percentage,
        random_state=seed_random,
        stratify=Y_encoded
    )
    print(f'Splitted training ({1 - test_percentage}) and testing sets ({test_percentage})')

    metadata = {
        'classes': Y_encoded[0].shape[0],
        'categories' : encoder.categories_[0].tolist(),
        'samples': X.shape[0],
        'observations': X.shape[1]}

    return X_train, Y_train, X_test, Y_test, encoder, metadata

def encodeDataset(labels):
    print('Encoding labels with OneHot')
    encoder = OneHotEncoder(sparse_output=False)
    encoded_labels = encoder.fit_transform(labels)

    print(f'Successfully encoded {len(encoder.categories_[0])} categories')
    return encoded_labels, encoder
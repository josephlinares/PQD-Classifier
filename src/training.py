import numpy as np
import keras
import seaborn as sns
import yaml

from sklearn.metrics import f1_score, classification_report, accuracy_score, confusion_matrix
from matplotlib import pyplot as plt
from pathlib import Path

import utils

# In the future, hyperparameter tuning?

def train(model, config, X_train, Y_train, X_test, Y_test):
    callback = keras.callbacks.LearningRateScheduler(scheduler)
    history = model.fit(X_train, Y_train,
                        batch_size=config['batch_size'],
                        epochs=config['epochs'],
                        callbacks=[callback],
                        validation_data=(X_test, Y_test),
                        verbose=1)

    print('Successfully trained the model')
    return model

def scheduler(self, epoch):
    """
    Compute the learning rate for the current epoch
    """
    dropEvery = 10
    initAlpha = 0.001
    factor = 0.5
    exp = np.floor((1 + epoch) / dropEvery)
    alpha = initAlpha * (factor ** exp)
    print('lr =', alpha)
    return float(alpha)

def evaluate(model, X_test, Y_test, categories, path : Path = None):
    metrics = dict()
    
    score = model.evaluate(X_test, Y_test, verbose=0)
    metrics[model.metrics_names[1]] = score[1]*100

    Y_pred = np.round(model.predict(X_test))

    metrics['accuracy'] = accuracy_score(Y_test, Y_pred)
    metrics['macro_f1'] = f1_score(Y_test, Y_pred, average="macro")
    metrics['weighted_f1'] = f1_score(Y_test, Y_pred, average="weighted")
    metrics['classification_report'] = classification_report(
        Y_test, Y_pred, target_names=categories)
    
    for key, value in metrics.items():
        print(f'{key}: {value}')

    if path:
        with open(path / "metrics.yaml", "w", encoding="utf-8") as file:
            yaml.safe_dump(metrics, file, default_flow_style=False, sort_keys=False)
        print('Successfully wrote metrics.yaml')

        cm = confusion_matrix(np.argmax(Y_test, axis=1), np.argmax(Y_pred, axis=1))

        plt.figure(figsize=(7, 7))
        sns.heatmap(
            cm,
            annot=True,
            fmt="d",
            cmap="Blues",
            xticklabels=categories,
            yticklabels=categories
        )

        plt.xlabel("Predicted Label")
        plt.ylabel("True Label")
        plt.title("Confusion Matrix: 1D-CNN")
        plt.xticks(rotation=45, ha="right")
        plt.yticks(rotation=0)
        plt.tight_layout()
        plt.savefig(path / 'confusion matrix.png')

        print('Successfully wrote \'confusion matrix.png\'')

    return model
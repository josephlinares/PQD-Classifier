import numpy as np
from keras.callbacks import LearningRateScheduler
import seaborn as sns
import yaml

from sklearn.metrics import f1_score, classification_report, accuracy_score, confusion_matrix
from matplotlib import pyplot as plt
from pathlib import Path

import utils

# Default initial learning rate
def create_lr_schedule(cfg: dict):
    pass

# In the future, hyperparameter tuning?

def scheduler(epoch):
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

def train(model, config, X_train, Y_train, X_test, Y_test, path : Path = None):
    callback = LearningRateScheduler(scheduler)
    history = model.fit(X_train, Y_train,
                        batch_size=config['batch_size'],
                        epochs=config['epochs'],
                        callbacks=[callback],
                        validation_data=(X_test, Y_test),
                        verbose=1)

    if path:
        # Plot CNN's accuracy vs. epoch num:
        fig = plt.figure()
        plt.plot(history.history['accuracy'])
        plt.plot(history.history['val_accuracy'])
        plt.xlabel('Epoch')
        plt.ylabel('Accuracy')
        plt.title('CNN : Accuracy vs. number of Epochs')
        plt.legend(['train','validation'])
        plt.savefig(path / 'training accuracy.png')
    print('Successfully trained the model')
    return model

def create_markdown(results : list, path : Path):
    '''Writes a MarkDown file for experimentation results

    Parameters:
    results (list): Macro F1 and Classification in MD format
    path (Path): Experimentation path where this will be stored
    '''
    with open(path / "README.md", "w", encoding="utf-8") as file:
        print("# Experimentation results\n", file=file)
        print(results[0], '\n', file=file)
        print(results[1], '\n', file=file)
        print('# Annotations\n', file=file)
        
def get_macrof1(Y_test, Y_pred, categories):
    '''Evaluate Macro F1 and Classification metrics of predictions
    
    Parameters:
    Y_test (array): Classification true labels
    Y_pred (array): Classification prediction labels
    categories (): Categories names

    
    '''
    accuracy = accuracy_score(Y_test, Y_pred)
    macro_f1 = f1_score(Y_test, Y_pred, average="macro")
    weighted_f1 = f1_score(Y_test, Y_pred, average="weighted")

    # Create dictionary prior to dataframe
    macrof_dict = {
        'Metric': ['Accuracy', 'Macro F1', 'Weighted F1'],
        'Value': [accuracy, macro_f1, weighted_f1]
    }

    # Create dataframe and round values to 2 decimal values
    macrof_df = pd.DataFrame(macrof_dict).round(2)
    
    report_dict = classification_report(
        Y_test, Y_pred, target_names=categories, output_dict=True)

    report_df = pd.DataFrame(report_dict).transpose().round(2)

    # Print results, useful when they will not be stored
    print(macrof_df)
    print(report_df)
    
    return [macrof_df.to_markdown(), report_df.to_markdown()]

def evaluate(model, X_test, Y_test, categories, path : Path = None):
    '''Evaluate Keras model and print confusion matrix
    
    Parameters:
    model (keras.Model): NN architecture to evaluate
    X_test (array): Signal inputs
    Y_test (array): Classification true labels
    categories (): Categories names
    path (Path): Optional path to save the results
    '''
    score = model.evaluate(X_test, Y_test, verbose=0)
    
    Y_pred = np.round(model.predict(X_test))
    results = get_macrof1(Y_test, Y_pred, categories)

    if path:
        create_markdown(results, path)

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
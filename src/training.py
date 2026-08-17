import numpy as np
import pandas as pd
import tensorflow as tf
import seaborn as sns

from pathlib import Path
from matplotlib import pyplot as plt
from sklearn.metrics import f1_score, classification_report, accuracy_score, confusion_matrix
from keras.callbacks import LearningRateScheduler

from utils import create_markdown

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

def save_confusion_matrix(confusion, categories, path : Path):
    plt.figure(figsize=(6, 6))
    sns.heatmap(
        confusion,
        annot=True,
        fmt="d",
        cmap="Blues",
        xticklabels=categories,
        yticklabels=categories
    )

    plt.xlabel("Predicted Label")
    plt.ylabel("True Label")
    plt.title("Confusion Matrix")
    plt.xticks(rotation=45, ha="right")
    plt.yticks(rotation=0)
    plt.tight_layout()
    plt.savefig(path / 'confusion matrix.png')

    print('Successfully wrote \'confusion matrix.png\'')

def evaluate(model, X_test, Y_test, categories, path : Path = None):
    '''Evaluate Keras model and print confusion matrix
    
    Parameters:
    model (keras.Model): NN architecture to evaluate
    X_test (array): Signal inputs
    Y_test (array): Classification true labels
    categories (): Categories names
    path (Path): Optional path to save the results
    '''
    print('Evaluating Keras model')
    model.evaluate(X_test, Y_test, verbose=0)
    Y_pred = np.round(model.predict(X_test))
    
    mf1 = get_macrof1(Y_test, Y_pred, categories)
    cm = confusion_matrix(np.argmax(Y_test, axis=1), np.argmax(Y_pred, axis=1))

    if path:
        create_markdown(mf1, path)
        save_confusion_matrix(cm, categories, path)

def evaluate_tflite(interpreter, X_test, Y_test, shape_cfg : dict, path : Path=None):
    print('Evaluating TFLite model')
    
    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()

    tensor_input_shape = (X_test.shape[0],)
    tensor_input_shape =  tensor_input_shape + shape_cfg['input_shape']
    tensor_output_shape = (X_test.shape[0], shape_cfg['outputs'])

    interpreter.resize_tensor_input(input_details[0]['index'], tensor_input_shape)
    interpreter.resize_tensor_input(output_details[0]['index'], tensor_output_shape)
    interpreter.allocate_tensors()

    interpreter.set_tensor(input_details[0]['index'], X_test)
    interpreter.invoke()

    Y_pred = interpreter.get_tensor(output_details[0]['index'])
    Y_pred = np.argmax(Y_pred, axis=1)
    Y_test = np.argmax(Y_test, axis=1)
    categories = shape_cfg['categories']

    mf1 = get_macrof1(Y_test, Y_pred, categories)
    cm = confusion_matrix(Y_test, Y_pred)
    
    if path:
        create_markdown(mf1, path)
        save_confusion_matrix(cm, categories, path)
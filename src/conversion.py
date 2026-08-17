import numpy as np
import tensorflow as tf

def make_representative_dataset(X_train):
    def representative_dataset():
        for i in range(512):
            yield [X_train[i:i+1].astype(np.float32)]
    return representative_dataset

def convert_to_tflite(model, X_train):
    print("*** TFLite Conversion ***")
    converter = tf.lite.TFLiteConverter.from_keras_model(model)
    converter.optimizations = [tf.lite.Optimize.DEFAULT]

    converter.representative_dataset = make_representative_dataset(X_train)

    converter.target_spec.supported_ops = [tf.lite.OpsSet.TFLITE_BUILTINS_INT8]
    converter.inference_input_type = tf.uint8
    converter.inference_output_type = tf.uint8

    converted_model = converter.convert()
    return converted_model


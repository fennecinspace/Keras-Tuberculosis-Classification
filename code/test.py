from keras.models import load_model
import tensorflow as tf
from numpy import array
from common import readcsv, BASE_DIR, os

test_path = os.path.join(*[BASE_DIR, 'data', 'test.csv'])
test = readcsv(test_path)[1:]

x_test = array([row[:-1] for row in test])
y_test = array([row[-1] for row in test])

## model
model = tf.keras.models.Sequential()

## hidden layer
model.add(tf.keras.layers.Dense(300, activation = tf.nn.relu))
model.add(tf.keras.layers.Dense(50, activation = tf.nn.relu))

## output layer 
model.add(tf.keras.layers.Dense(5, activation = tf.nn.softmax))

## cost
model.compile(optimizer = 'adam', loss = 'sparse_categorical_crossentropy', metrics=['accuracy'])

## Loading Weights
model.fit(x_test[1:2], y_test[1:2], epochs = 0)
model.load_weights('weights.h5')

[Loss, Accuracy] = model.test_on_batch(x_test, y_test)

print("Loss : {} / Accuracy : {}".format(Loss, Accuracy))
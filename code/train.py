import tensorflow as tf 
from numpy import array
from common import readcsv, BASE_DIR, os

train_path = os.path.join(*[BASE_DIR, 'data', 'train.csv'])

train = readcsv(train_path)[1:]

train_70 = len(train)//3*2

x_train = array([row[:-1] for row in train[:train_70]])
y_train = array([row[-1] for row in train[:train_70]])

x_test = array([row[:-1] for row in train[train_70:]])
y_test = array([row[-1] for row in train[train_70:]])

## model
model = tf.keras.models.Sequential()

## hidden layer
model.add(tf.keras.layers.Dense(300, activation = tf.nn.relu))
model.add(tf.keras.layers.Dense(50, activation = tf.nn.relu))

## output layer 
model.add(tf.keras.layers.Dense(5, activation = tf.nn.softmax))

## cost
model.compile(optimizer = 'adam', loss = 'sparse_categorical_crossentropy', metrics=['accuracy'])

## learning
model.fit(x_train, y_train, epochs = 3)

val_loss, val_acc = model.evaluate(x_test, y_test)
print("Loss {} \nAccuracy {}".format(val_loss, val_acc))

model.save_weights('weights.h5')
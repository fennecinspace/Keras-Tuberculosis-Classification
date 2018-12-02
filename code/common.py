import csv
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

def readcsv(filename):  
    ifile = open(filename, "r")
    reader = csv.reader(ifile, delimiter=";")

    rownum = 0  
    a = []

    for row in reader:
        a += [row[0].split(',')]
        rownum += 1
    
    
    for i in range(len(a)):
        for j in range(len(a[i])):
            try:
                a[i][j] = eval(a[i][j])
            except:
                pass
    
    ifile.close()
    return a

# test = readcsv('./test.csv')[1:]
    
# x_train = array([row[:-1] for row in train])
# y_train = array([row[-1] for row in train])

# x_test = array([row[:-1] for row in test])
# y_test = array([row[-1] for row in test])

# x_train_normalized = tf.keras.utils.normalize(x_train, axis = 1)
# x_test_normalized = tf.keras.utils.normalize(x_test, axis = 1)
from csv_parser import Parser
import random
a = Parser('transport_data.csv')
a.open()
dots = a.get_data()



zero = []
first = []
second = []
q = []
for dot in dots:
    if dot.label == '0':
        zero.append(dot)
    if dot.label == '1':
        first.append(dot)
    if dot.label == '2':
        second.append(dot)
    if dot.label == '?':
        q.append(dot)

dots = first+second+zero
random.shuffle(dots)

def get_min(dot, arr, num_of):
    dist = []
    for d in arr:
        if d == dot:
            continue
        dist.append(dot.dist(d))
    ans = []
    for i in range(num_of):
        tmp = min(dist)
        ans.append(tmp)
        dist.remove(tmp)
    return ans

import numpy as np
import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Conv2D, MaxPooling2D
import matplotlib.pyplot as plt
from keras.utils import np_utils
import os
from sklearn.model_selection import train_test_split
batch_size = 200
num_classes = 3
epochs = 100
data_augmentation = True
X = []
y = []
rt = 3
if False:
    for _, dot in enumerate(dots[:10000]):
        z = np.matrix(get_min(dot, zero, rt**2)).reshape(rt,rt)
        z /= np.linalg.norm(z)
        f = np.matrix(get_min(dot, first, rt**2)).reshape(rt,rt)
        f /= np.linalg.norm(f)
        s = np.matrix(get_min(dot, second, rt**2)).reshape(rt,rt)
        s /= np.linalg.norm(s)
        ans = np.array([z, f, s]).reshape(rt,rt,3)
        X.append(ans)
        y.append(np_utils.to_categorical(dot.label, 3))
        if _%1000 == 0:
            print("=", end="")
            import sys
            sys.stdout.flush()
    y = np.array(y)
    np.save("y3x3", y)
    X = np.array(X)
    np.save("X3x3", X)

X = np.load("X3x3.npy")
y = np.load("y3x3.npy")
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=42)
print('x_train shape:', x_train.shape)
print(x_train.shape[0], 'train samples')
print(x_test.shape[0], 'test samples')

model = Sequential()
model.add(Conv2D(64, (3, 3), padding='same',
                 input_shape=(rt, rt, 3)))
model.add(Activation('relu'))
model.add(Conv2D(128, (2, 2)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(1, 1)))
model.add(Dropout(0.25))

model.add(Flatten())
model.add(Dense(256))
model.add(Activation('relu'))
model.add(Dropout(0.5))
model.add(Dense(3, activation='softmax'))

# initiate RMSprop optimizer
opt = keras.optimizers.rmsprop(lr=0.0001, decay=1e-6)

# Let's train the model using RMSprop
if __name__ == "__main__":
    model.compile(loss='categorical_crossentropy',
                  optimizer=opt,
                  metrics=['accuracy'])

    """
    history: данные полученные во время обучения сети, необходимые для построения различных графиков"""

    history = model.fit(x=X, y=y, batch_size=batch_size, epochs=epochs,
                        shuffle=True, validation_data=(x_test, y_test))
    """if not os.path.isdir(save_dir):
        os.makedirs(save_dir)
    model_path = os.path.join(save_dir, model_name)
    model.save(model_path)
    print('Saved trained model at %s ' % model_path)


    Данные полученные после тестирования сети - точность работы на тренировчном множестве """

    scores = model.evaluate(x_test, y_test, verbose=1)
    print("Точность работы на тестовых данных: %.2f%%" % (scores[1] * 100))
    plt.plot(history.history['acc'])
    plt.show()


"""
label 0 - маршрут 5
label 1 - маршрут 11 
label 2 - маршрут 7
"""

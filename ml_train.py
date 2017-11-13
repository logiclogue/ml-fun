import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.examples.tutorials.mnist import input_data
from sklearn.externals import joblib

mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

#grabs training images, training labels, testing images, testing labels
trX, trY, teX, teY = mnist.train.images, mnist.train.labels, mnist.test.images, mnist.test.labels


#build tflow graph
x = tf.placeholder("float",shape=[None,784])
y = tf.placeholder("float",shape=[None,10])

#random initialization of weights
w = tf.Variable(tf.random_normal([784,10]))
#yhat -> predicted values
yhat = tf.matmul(x,w)
cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=y,logits=yhat))
optmizer = tf.train.GradientDescentOptimizer(0.01).minimize(cost)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    cost_values = []
    
    #implementing mini batch gradient descent
    #mini batch size = 128

    for epoch in range(100):
        print("Epoch " + str(i))
        for start, end in zip(range(0, len(trX), 1), range(1, len(trX)+1, 1)):
            _,c=sess.run([optmizer,cost], feed_dict={x: trX[start:end], y: trY[start:end]})
            cost_values.append(c)

        #prints out accuracy after every epoch
        pred = np.argmax(sess.run(yhat,{x:teX}),axis=1)
        print(np.mean(pred==np.argmax(teY,axis=1)))

    joblib.dump(sess.run(w), 'weights.pkl')

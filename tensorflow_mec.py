import tensorflow as tf

from tensorflow.examples.tutorials.mnist import input_data

NUM_CLASSES = 10
IMAGE_SIZE = 28
IMAGE_PIXELS = IMAGE_SIZE * IMAGE_SIZE

FLAGS = None
batch_size = 10


def placeholder_inputs(batch_size):
	images_placeholder = tf.placeholder(tf.float32, shape=(batch_size, IMAGE_PIXELS))
	labels_placeholder = tf.placeholder(tf.int32, shape=(batch_size))
	return images_placeholder, labels_placeholder

weights = tf.Variable(tf.truncated_normal([IMAGE_PIXELS, hidden1_units],stddev=1.0 / math.sqrt(float(IMAGE_PIXELS))),
	name='weights')
biases = tf.Variable(tf.zeros([hidden1_units]),name='biases')

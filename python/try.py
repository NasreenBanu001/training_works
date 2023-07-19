# import tensorflow as tf
# import os
# os.environ['TF_CPP_MIN_LOG_LEVEL'] = "2"
# print("TensorFlow version:", tf.__version__)

# mnist = tf.keras.datasets.mnist

# (x_train, y_train), (x_test, y_test) = mnist.load_data()
# x_train, x_test = x_train / 255.0, x_test / 255.0

# model = tf.keras.models.Sequential([
#   tf.keras.layers.Flatten(input_shape=(28, 28)),
#   tf.keras.layers.Dense(128, activation='relu'),
#   tf.keras.layers.Dropout(0.2),
#   tf.keras.layers.Dense(10)
# ])

# # a=tf.constant("Hello world")
# # print (a)

# # s = tf.Session()
# # print (s.run(a))
# # s.close()

# # # with tf.Session() as s:
# # #     print(s.run(a))

# import cv2
# # The function cv2.imread() is used to read an image.
# img_grayscale = cv2.imread('/home/provility/Downloads/image1.jpeg',)
 
# # The function cv2.imshow() is used to display an image in a window.
# cv2.imshow('graycsale image',img_grayscale)
 
# # waitKey() waits for a key press to close the window and 0 specifies indefinite loop
# cv2.waitKey(0)
 
# # cv2.destroyAllWindows() simply destroys all the windows we created.
# cv2.destroyAllWindows()
 
# # The function cv2.imwrite() is used to write an image.
# cv2.imwrite('grayscale.jpg',img_grayscale)

import cv2
 
# Read the image using imread function
image = cv2.imread('/home/provility/Downloads/image1.jpeg')
cv2.imshow('Original Image', image)
 
# let's downscale the image using new  width and height
down_width = 300
down_height = 200
down_points = (down_width, down_height)
resized_down = cv2.resize(image, down_points, interpolation= cv2.INTER_LINEAR)
 
# let's upscale the image using new  width and height
up_width = 600
up_height = 400
up_points = (up_width, up_height)
resized_up = cv2.resize(image, up_points, interpolation= cv2.INTER_LINEAR)
 
# Display images
cv2.imshow('Resized Down by defining height and width', resized_down)
cv2.waitKey()
cv2.imshow('Resized Up image by defining height and width', resized_up)
cv2.waitKey()
 
#press any key to close the windows
cv2.destroyAllWindows()
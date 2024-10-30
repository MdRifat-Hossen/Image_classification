import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import load_model
import streamlit as st
import numpy as np
st.header('Image Classification Model')
model = load_model('C:\\Users\\HP\\OneDrive\\Desktop\\Image_clasification\\Image_classify.keras')
image = 'Apple (2).jpg'

data_cat=['apple',
 'banana',
 'beetroot',
 'bell pepper',
 'cabbage',
 'capsicum',
 'carrot',
 'cauliflower',
 'chilli pepper',
 'corn',
 'cucumber',
 'eggplant',
 'garlic',
 'ginger',
 'grapes',
 'jalepeno',
 'kiwi',
 'lemon',
 'lettuce',
 'mango',
 'onion',
 'orange',
 'paprika',
 'pear',
 'peas',
 'pineapple',
 'pomegranate',
 'potato',
 'raddish',
 'soy beans',
 'spinach',
 'sweetcorn',
 'sweetpotato',
 'tomato',
 'turnip',
 'watermelon']
img_width=180
img_height=180

image = st.text_input('Enter Image name','Apple (2).jpg')

image_load=tf.keras.utils.load_img(image,target_size=(img_height,img_width))
img_arr=tf.keras.utils.array_to_img(image_load)
img_bat=tf.expand_dims(img_arr,0)

predict=model.predict(img_bat)
st.image(image,width=200)
score=tf.nn.softmax(predict)




st.write('Fruit in image is {} with accuracy of {:0.2f}%'.format(data_cat[np.argmax(score)], np.max(score) * 100))

# Importation de TensorFlow 
import tensorflow as tf
#Création du modèle
model=tf.keras.Sequential()
#Ajout d'une couche d'entrée avec 4 entrée
model.add(tf.keras.layers.Input(shape=[4], name='input_image'))
#Ajout d'une couche cachée dense de 18 neurones
model.add(tf.keras.layers.Dense(18, activation='relu'))
#Ajout d'une couche de sortie
model.add(tf.keras.layers.Dense(3, activation='softmax'))

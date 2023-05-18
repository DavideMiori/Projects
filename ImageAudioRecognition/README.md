# Computer Vision Project
This project is divided into three tasks: Speaker Identification, Image Recogntion and Image Retrieval.   
The first one concerns the development of a model which is capable of recognizing who is talking. Thanks to the mfcc features we have trained a cnn to recognize a person by his voice.     
The second task is equal to the first execpt that we have used images instead of audio signals. So the model recognizes a person by a picture.  
The last task concerns about retrieving ten pictures of famous people which are similar to a face. We have deployed a cnn again which extracts the neural features from the images and compares them. 

The Acquisition.ipynb file contains the code used for recording audios and taking pictures.  
The Demo.ipynb contains the code to activate the live demo for the three tasks.   
The remaining three files are associated with the three tasks described above.

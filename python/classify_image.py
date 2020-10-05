import os
import sys
import json

from weka import Weka
from classifier import Classifier
from read_image import ReadImage

if __name__ == "__main__":

    my_path1 = os.getcwd()
    filename1 = 'bob (18).jpg'
    file_path1 = my_path1 + '/images/' + filename1

    my_path2 = os.getcwd()
    filename2 = 'caracteristicas.arff'
    file_path2 = my_path2 + '/images/' + filename2
    
    image = [file_path1]
    model = [file_path2]

    # Predict image
    Classifier().classify(img=image, model=model)

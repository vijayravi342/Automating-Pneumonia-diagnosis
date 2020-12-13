import sys 
import os
import cv2
import numpy as np
import importlib
sys.path.append('C:\\Users\\ROG\\Anaconda3\\envs\\base\\Lib\\site-packages')
#from PIL import Image
#sys.path.append(os.path.dirname(os.path.realpath("ChestXrayProject")))
#sys.path.append('C:/Users/Mango/Documents/Python Scripts')
dirname, basename = os.path.split('C:\\Users\\ROG\\Documents\\Python Scripts\\Predict.py')
sys.path.append(dirname)
module_name = os.path.splitext(basename)[0]
module = importlib.import_module(module_name)
import Predict



Predict = Predict.Predict()
if __name__=="__main__":
    value = (input("enter input here :")).replace("'", "")
    value = Predict.main(value)
    #print(value)
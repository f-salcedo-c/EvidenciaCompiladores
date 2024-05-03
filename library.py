import numpy as np
import cv2 
import matplotlib.pyplot as plt

def load_image(path):
    path = path.strip()
    return cv2.imread(path)


def save_image(filename, image):
    cv2.imwrite(filename, image)

def show_image(img):
    cv2.imshow('window' , img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return img

def search_cv2(function_name):
    try:
        return getattr(cv2, function_name) 
    except:
        return None    
    return None

def gen_matrix(a,b,*args):
    s = np.array(args)
    return s.reshape(int(a),int(b))

def gen_vector(*args):
    s = np.array(args)
    return s


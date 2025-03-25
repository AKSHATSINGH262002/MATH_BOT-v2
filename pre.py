

from pytesseract import pytesseract 
import io
#import  re
#import pandas as pd




pytesseract.tesseract_cmd=r'git@github.com:AKSHATSINGH262002/MATH_BOT-v2.git'
def extract(image_path):
  #image=Image.open(image_path)
   text=pytesseract.image_to_string(image_path)
   arr=text.split()
   return arr





    

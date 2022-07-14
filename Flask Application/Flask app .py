# Import libraries

from flask import Flask, render_template, request, redirect, url_for
from keras.models import load_model
import numpy as np
import cv2
import os
from flask import Flask
from werkzeug.utils import secure_filename
import os
from tensorflow import keras
from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
import dlib
import tensorflow as tf
from tensorflow.keras.preprocessing.image import img_to_array, load_img

#****************************************************************************************

# Display Home Page 

app = Flask(__name__ , template_folder='static/templates')
@app.route('/')
def main():
  return render_template ("Home.html")

#***************************************************************************************************

# Redirect To Upload  

@app.route('/upload_video', methods=['POST'])
def Video():
  return render_template ("Upload_Video.html")

@app.route('/upload_image', methods=['POST'])
def image():
    return render_template('Upload_image.html')
@app.route('/About-us', methods=['POST'])
def About_us():
  return render_template('About-us.html')

#*********************************************************************************************************

# Load Model 

model = tf.keras.models.load_model('model/deepfake-detection-tensor.h5')

#***********************************************************************************************************

# Function Prediction 


def prediction (filepath):
  input_shape = (128, 128, 3)
  pr_data = []
  detector = dlib.get_frontal_face_detector()
  cap = cv2.VideoCapture(filepath)
  frameRate = cap.get(5)
  while cap.isOpened():
      frameId = cap.get(1)
      ret, frame = cap.read()
      if ret != True:
          break
      if frameId % ((int(frameRate)+1)*1) == 0:
          face_rects, scores, idx = detector.run(frame, 0)
          for i, d in enumerate(face_rects):
              x1 = d.left()
              y1 = d.top()
              x2 = d.right()
              y2 = d.bottom()
              crop_img = frame[y1:y2, x1:x2]
              data = img_to_array(cv2.resize(crop_img, (128, 128))).flatten() / 255.0
              data = data.reshape(-1, 128, 128, 3)
              print((model.predict(data) > 0.5).astype("int32"))
              outt=''
  if ((model.predict(data) > 0.5).astype("int32")[0][0] == 0 ):
    return 'Real'
  else:
    return'Fake'

#***********************************************************************************************************

# Upload File 

UPLOAD_FOLDER = 'static'
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

#********************************************************************************************************

# Video Prediction & Display Result 

@app.route('/predict_video', methods=['POST'])
def upload_video():
	file = request.files['file']
	filename = secure_filename(file.filename)
	file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
	filepath = "static/"+filename
	preds = prediction(filepath)
	return render_template("Display_Video.html",prediction =preds ,video_path = filename)

#***********************************************************************************************************

# Image Prediction & Display Result 

@app.route('/Predict_image', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        f = request.files['file']
        file_path = os.path.join (app.config['UPLOAD_FOLDER'], secure_filename(f.filename))
        f.save(file_path)
        # Make prediction
        preds = prediction(file_path)
    return render_template("Display_image.html",prediction = preds, img_path= f.filename )

#****************************************************************************************************************

"""# Run Flask Application  """

if __name__ =='__main__': 
  app.run()
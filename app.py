import datetime
import base64
import numpy as np
import io
from PIL import Image
import re
import os
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
from flask import request, render_template
from flask import jsonify
from flask import Flask
import requests
from flask import Flask, render_template
# Imports the Cloud Logging client library
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from werkzeug.wrappers import Request, Response
from werkzeug.utils import secure_filename
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array

from tensorflow import keras
model = keras.models.load_model('./model/chest_xray_model2.h5')
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)


app = Flask(__name__)#, template_folder='./templates', static_folder='./static'
UPLOAD_FOLDER = os.path.join(app.instance_path, '/static/img')
app_root = os.path.dirname(os.path.abspath(__file__))
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def hello_world():
    return render_template("index.html")
    
@app.route('/upload_static_file', methods=['POST'])
def upload_static_file():
    print("Got request in static files")
    print(request.files)
    f = request.files['static_file']
    f.save(os.path.join(r'C:\Users\dhars\OneDrive\Desktop\test' , f.filename))
    resp = {"success": True, "response": "file saved!"}
    return jsonify(resp), 200
 
 

@app.route('/email_to', methods=['GET', 'POST'])
def email_to():

    #target = os.path.join('', '/img')
    #if not os.path.isdir(target):
    #    os.makedirs(target)
    file = request.files['file']
    #file_name = file.filename or ''
    #destination = '/'.join([target, file_name])
    filename = secure_filename(file.filename)
    #try:
    filename = secure_filename(file.filename)
    image_path = "./images/" + file.filename
    file.save(image_path)
    
    image = load_img(image_path, target_size=(300, 300))
    image = img_to_array(image)/255
    image = image.reshape(-1,300,300,3)
    #image = preprocess_input(image)
    yhat = model.predict(image)
    prediction = yhat
    output = str(yhat*100)
    if (prediction>0.50):
        result = 'positive'
    else:
        result = 'negative'

    #return render_template('index.html')
        
    #except:
    #    raise
    #    print('error')
    #    prediction = 'error'
    gmail_user = 'labtechnologies5@gmail.com'
    gmail_password = 'labtech5'

    from fpdf import FPDF
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
  
# save FPDF() class into a 
# variable pdf
    pdf = FPDF()
  
# Add a page
    pdf.add_page()
    
# set style and size of font 
# that you want in the pdf
    pdf.set_font("Arial", size = 12)
  
# create a cell
    pdf.cell(200, 10, txt = "I AM LAB", 
         ln = 1, align = 'C')
  
# add another cell
    pdf.cell(200, 10, txt = "TEST REPORT",
         ln = 2, align = 'C')
         
# add another cell
    pdf.cell(200, 10, txt = "No:CBTC-YGT786899999787                                                Page 1 of 1",
         ln = 3, align = ' ')
 
# add another cell
    pdf.cell(200, 10, txt = "The submitted file and information was/were submitted by/on the behalf of the client",
         ln = 4, align = ' ',border=1)
         
# add another cell
    pdf.cell(200, 10, txt = "Good Day! Thank You for choosing I am Lab.",
         ln = 3, align = ' ')
         
# add another cell
    pdf.cell(200, 10, txt = "PNEUMONIA:",
         ln = 5, align = ' ')
         
# add another cell
    pdf.cell(200, 10, txt = "Pneumonia is an infection that inflames the air sacs in one or both lungs.",
         ln = 6, align = ' ')
         
# add another cell
    pdf.cell(200, 10, txt = "Please consult the doctor immediately if you have the following symptoms:",
         ln = 6, align = ' ') 

# add another cell
    pdf.cell(200, 10, txt = "Pneumonia symptoms may include:",
         ln = 6, align = ' ')
         
# add another cell
    pdf.cell(200, 10, txt = "1.Chest pain when you breathe or cough.",
         ln = 6, align = ' ')
         
# add another cell
    pdf.cell(200, 10, txt = "2.Confusion or changes in mental awareness (in adults age 65 and older).",
         ln = 6, align = ' ')
         
# add another cell
    pdf.cell(200, 10, txt = "3.Cough, which may produce phlegm.",
         ln = 6, align = ' ')
         
# add another cell
    pdf.cell(200, 10, txt = "4.Fatigue, Fever, sweating and shaking chills.",
         ln = 6, align = ' ')
         
# add another cell
    pdf.cell(200, 10, txt = "5.Lower than normal body temperature (in adults older than age 65 and people with weak immune systems).",
         ln = 6, align = ' ')
         
# add another cell
    pdf.cell(200, 10, txt = "6.Nausea, vomiting or diarrhea.",
         ln = 6, align = ' ')
         
# add another cell
    pdf.cell(200, 10, txt = "7.Shortness of breath.",
         ln = 6, align = ' ')
         
         
# add another cell
    pdf.cell(200, 10, txt = "EXAMINATION: Chest PA and Lateral",
         ln = 9, align = 'C')
 

# add another cell
    pdf.cell(200, 10, txt = "Here are the results to your test report.",
         ln = 4, align = ' ' )

# add another cell
    pdf.cell(200, 10, txt = "FINDINGS:",
         ln = 4, align = ' ' )

# add another cell
    pdf.cell(200, 10, txt = "Probability of Pneumonia :  "+output,
         ln = 4, align = 'C' )
         
# add another cell
    pdf.cell(200, 10, txt = "IMPRESSION:"+result ,
         ln = 5, align = 'C')
         
# add another cell
    pdf.cell(200, 10, txt = "Terms and Conditions",
         ln = 13, align = ' ')
# add another cell
    pdf.cell(200, 10, txt = "1. Scope of These Terms and Conditions",
         ln = 14, align = ' ')
# add another cell
    pdf.cell(200, 10, txt = "These Terms and Conditions are applicable to your access to and use of www.iamlab.com.",
         ln = 15, align = ' ')   
         
# add another cell
    pdf.cell(200, 10, txt = "2. Privacy Statement and Notice of Privacy Practices",
         ln = 16, align = ' ')
# add another cell
    pdf.cell(200, 10, txt = "Our Privacy Statement and, with respect to protected health information, our Notice of Privacy Practices",
         ln = 17, align = ' ')
# add another cell
    pdf.cell(200, 10, txt = "describe how iamlab collects information about you through the Online Services, and how ",
         ln = 18, align = ' ')

# add another cell
    pdf.cell(200, 10, txt = "we use, disclose, and protect that information.",
         ln = 19, align = ' ')
         
# add another cell
    pdf.cell(200, 10, txt = "Click the URL to direct back to the website:http://127.0.0.1:5000/",
         ln = 5, align = ' ')
         
# add another cell
    pdf.cell(200, 10, txt = "******For more detailed information,please refer the website******",
         ln = 22, align = 'C')
         

#add image         
    pdf.image(image_path, x=50, y=90,w=100,h=75)
    

  
# save the pdf with name .pdf
    pdf.output("report.pdf")
    gmail_user = 'labtechnologies5@gmail.com'
    gmail_password = 'yktbtcuntljtbuff'
    
    sent_from = gmail_user
    to = ['dharshumurali99@gmail.com', 'msatishmuralitharan@gmail.com']
    subject = 'Your result has arrived'
    body = "Your result pdf is attached."
    #to.append(report)
    email_text = """\
    From: %s
    To: %s
    Subject: %s
    
    %s
    """ % (sent_from, ", ".join(to), subject, body)
    
    
     
    #server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    #server.ehlo()
    #server.login(gmail_user, gmail_password)
    #server.sendmail(sent_from, to, email_text)
    #server.close()
    
    
    fromaddr = "labtechnologies5@gmail.com"
    toaddr = ", ".join(to)
    to = request.form['email']
    # instance of MIMEMultipart
    msg = MIMEMultipart()
    
    # storing the senders email address  
    msg['From'] = fromaddr
    
    # storing the receivers email address 
    msg['To'] =  request.form['email']
    
    # storing the subject 
    msg['Subject'] = "Report from Lab Technologies"
    
    # string to store the body of the mail
    body = "Your result pdf is attached. This is not the final result. Please consult a doctor with this report or book an appointment with our doctor."
    
    # attach the body with the msg instance
    msg.attach(MIMEText(body, 'plain'))
    
    # open the file to be sent 
    filename = "report.pdf"
    attachment = open("report.pdf", "rb")
    
    # instance of MIMEBase and named as p
    p = MIMEBase('application', 'octet-stream')
    
    # To change the payload into encoded form
    p.set_payload((attachment).read())
    
    # encode into base64
    encoders.encode_base64(p)
    
    p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    
    # attach the instance 'p' to instance 'msg'
    msg.attach(p)
    
    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)
    
    # start TLS for security
    s.starttls()
    
    # Authentication
    s.login(fromaddr, gmail_password )
    
    # Converts the Multipart msg into a string
    text = msg.as_string()
    
    # sending the mail
    s.sendmail(fromaddr, toaddr, text)
    
    # terminating the session
    s.quit()
    return render_template('index.html')
    
        
        

def get_model():
    global model
    try:
        email_to()
        model = load_model('model/chest_xray_model2.h5')  # 'VGG16_cats_and_dogs.h5')
        response = {
            'response': {
                'success': 'Model Loaded Successfully.'
            }
        }
        print(" * Model loaded!")

        print(response)
        return jsonify(response)
    except Exception as e:
        response = {
            'response': {
                'error': 'Model Loading failed.<br>Something went wrong, please try again later..'
            }
        }
        print(response)
        return jsonify(response)

def preprocess_image(image, target_size):
    if image.mode != "RGB":
        image = image.convert("RGB")

    image = image.resize(target_size)
    print('Image Size:',image.size)

    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)
    return image

# get_model()

@app.route("/loadModel", methods=['GET','POST'])
def loadModel():
    email_to()
    print(" * Loading Keras model...")
    return get_model()

@app.route("/index", methods=['GET', 'POST'])  # ,"GET"])
def predict():
    email_to()
    print('In: 1')

    message = request.get_json(force=True)  # json#
    encoded = message['image']
    image_data = re.sub('^data:image/.+;base64,', '', encoded)

    # print(img_type)
    decoded = base64.b64decode(image_data)#encoded)
    print('Image Type::: ',type(decoded))
    image = Image.open(io.BytesIO(decoded))
    processed_image = preprocess_image(image, target_size=(256, 256))

    respone = ''
    isNegative = True

    prediction = model.predict(processed_image).tolist()
    negative = prediction[0][0] * 100
    positive = prediction[0][1] * 100
    print('Negative',negative,':', 'Positive:',positive)
    if float(prediction[0][0])>float(prediction[0][1]):
        #respone = 'Patient X-ray report seems {}% Covid Negative'.format(negative)
        respone = 'Patient X-ray report seems Covid Negative'
        isNegative=True
    else:
        #respone = 'Patient X-ray report seems {}% Covid Positive'.format(positive)
        respone = 'Patient X-ray report seems Covid Positive'
        isNegative = False

    response = {
        'prediction': {
            'response': respone,
            'isNegative': isNegative
            # 'Negative': prediction[0][0],
            # 'Positive': prediction[0][1]
        }
    }
    print(response)
    return jsonify(response)



if __name__ == "__main_":
	app.debug = False
	from werkzeug.serving import run_simple
	run_simple("localhost", 5000, app)
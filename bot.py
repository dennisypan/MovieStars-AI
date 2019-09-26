from flask import Flask, request, jsonify
import json
import requests
import pandas as pd

import boto3
#import urllib.request
from PIL import Image
from io import BytesIO
import cv2
import numpy


app = Flask(__name__)
port = '5000'


# Input region_name, aws_access_key_id, aws_secret_access_key
client=boto3.client('rekognition', region_name='us-west-2', 
                    aws_access_key_id='', 
                    aws_secret_access_key='')

response1 = None

response = ""
temps = []
A = ""
B = ""
C = ""
D = ""
E = ""
F = ""
URLs = ""

@app.route('/', methods=['POST'])
def index():
    data = json.loads(request.get_data())

    # FETCH THE IMAGE URL
    #if data['conversation']['memory']['url']['type']:
        #URLs = data['conversation']['memory']['url']['type']

    #else:
    URLs = data['conversation']['memory']['url']['raw']
	
	
    try:
        response1 = requests.get(URLs)
        img = Image.open(BytesIO(response1.content))

        # Change image to numpy array
        np_im = numpy.array(img)

        # Change image to RGB color
        image_rgb = cv2.cvtColor(np_im, cv2.COLOR_BGR2RGB)

        # Save image to local file
        cv2.imwrite('Temp.jpg', image_rgb) 


        # Get JSON response in recognizing celebrity in image
        photo='Temp.jpg'

        with open(photo, 'rb') as image:
            response1 = client.recognize_celebrities(Image={'Bytes': image.read()})
        
        		
        for celebrity in response1['CelebrityFaces']:
            A = "\n" + 'Name: ' + ''.join(celebrity['Name']) + "\n"
            B = 'Id: ' + ''.join(celebrity['Id']) + "\n"
            C = 'Confidence: ' + ''.join('{:.3f}'.format(celebrity['Face']['Confidence'])) + "\n"
            D = 'Left Position: ' + ''.join('{:.2f}'.format(celebrity['Face']['BoundingBox']['Height'])) + "\n"
            E = 'Top Position: ' + ''.join('{:.2f}'.format(celebrity['Face']['BoundingBox']['Top'])) + "\n" 
            for url in celebrity['Urls']:
                F = url + "\n" 
            temps.append(A)
            temps.append(B)
            temps.append(C)
            temps.append(D)
            temps.append(E)
            temps.append(F)
            temps.append("\n")			
		
        response = ''.join(temps)        
		
		# for debugging use
        print(response)	
        
        # clear out previous information from the list "temps"		
        temps[:] = []
		
        # Print this only if no celebrities got detected         
        if not response1['CelebrityFaces']:
            response = 'Sorry, no celebrities got detected. Try another image URL!'

    except:
        response = 'Sorry, either image not detected or you did not enter a valid URL!  Please enter a valid image URL!'



    return jsonify(
        status=200,
        replies=[{
          'type': 'text',
          'content': response 
        }]
  )

@app.route('/errors', methods=['POST'])
def errors():
  print(json.loads(request.get_data()))
  return jsonify(status=200)

print(response)
app.run(port=port)

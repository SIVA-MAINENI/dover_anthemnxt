import os
import io
import json
import requests
from PIL import Image, ImageDraw, ImageFont
import msrest.authentication
import azure.cognitiveservices.vision.computervision
from msrest.authentication import CognitiveServicesCredentials
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes, VisualFeatureTypes


credential = json.load(open('api_key.json'))
api_key = credential['API_KEY']
endpoint = credential['END_POINT']
 
cv_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(api_key))

img_url1 = 'https://i.gaw.to/vehicles/photos/40/19/401931-2020-audi-a4.jpg?1024x640'


# img_url2 =  
img = 'DoverFuelHk\Audi4.jpeg'

max_description = 20
result = cv_client.analyze_image(img_url1, visual_features=['brands'])

if len(result.brands) > 0:
    for brand in result.brands:
        print("'{}' brand detected with confidence {:.1f}% at location {}, {}, {}, {}".format( \
            brand.name, brand.confidence * 100, brand.rectangle.x, brand.rectangle.x + brand.rectangle.w, \
            brand.rectangle.y, brand.rectangle.y + brand.rectangle.h))
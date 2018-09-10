import re
import requests
import json

response=requests.get("https://apit.17shanyuan.com/1.0/rs-project3/pre-see/4ccdd5d4b935465bafaed54342388656")

jsonText=response.json()

print jsonText

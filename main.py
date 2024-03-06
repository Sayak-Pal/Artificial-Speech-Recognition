from api_communiction import *
import json
import sys

filename=sys.argv[1]  
audio_url=upload(filename)
save_transcript(audio_url,filename)
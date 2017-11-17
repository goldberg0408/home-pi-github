# -*- coding: utf-8 -*-

import sys
import urllib.request


client_id = "h1pO8IUrZsmwiGRqY_dQ"
client_secret = "fDoPMVSaCA"
encText = urllib.parse.quote("미세먼지 등급이 나쁨이이므로 외출을 안하시는게 좋지 않을까요??")
data = "speaker=jinho&speed=1&text=" + encText;
url = "https://openapi.naver.com/v1/voice/tts.bin"
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request, data=data.encode('utf-8'))
rescode = response.getcode()
if(rescode==200):
  print("음성합성완료")
  response_body = response.read()

  with open('dust_bad1.mp3', 'wb') as f:
   f.write(response_body)
   #os.system("omxplayer wether.mp3")
else:
  print("Error Code:" + rescode)


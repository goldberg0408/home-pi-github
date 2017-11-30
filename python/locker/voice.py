import sys
import urllib.request


client_id = "h1pO8IUrZsmwiGRqY_dQ"
client_secret = "fDoPMVSaCA"
encText = urllib.parse.quote("원하는 사물함을 선택해주세요.")
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

  with open('choice.mp3', 'wb') as f:
   f.write(response_body)
   #os.system("omxplayer wether.mp3")
else:
  print("Error Code:" + rescode)

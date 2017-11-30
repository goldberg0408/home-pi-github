import sys
import urllib.request


client_id = "h1pO8IUrZsmwiGRqY_dQ"
client_secret = "fDoPMVSaCA"
encText = urllib.parse.quote("에바쎄바 참치 넙치 꽁치 뭉치면 살고 흩어지면 죽는 각을 부장 판사님은 인정하십니까? 예. 인정합니다")
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

  with open('agree.mp3', 'wb') as f:
   f.write(response_body)
   #os.system("omxplayer wether.mp3")
else:
  print("Error Code:" + rescode)

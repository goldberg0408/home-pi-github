
import requests,json


data = {"text":"hi","call":"calldf"}
response = requests.post('http://115.40.151.150:5000/post',data=data)


print (response.status_code)
data=json.loads(response.text)

print(data['text'])
print(data['call'])
#print (dic["text"])
#print (dic["call"])

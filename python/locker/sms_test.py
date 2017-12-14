# -*- coding: utf-8 -* 
import sys
import pymysql
import requests
from sdk.api.message import Message
from sdk.exceptions import CoolsmsException

##  @brief This sample code demonstrate how to send sms through CoolSMS Rest API PHP

    # set api key, api secret
api_key = "NCS76REGORDXIHMI"
api_secret = "XSCPKTB0CVFBVWBMHV1QNLM7IG2KL2XB"
db = pymysql.connect(host="192.168.1.180",user="client",passwd="1234",db="lockersystem",charset="utf8")
cur = db.cursor()
cur.execute("select * from m_info where sec_key='ad1s'")
rs = cur.fetchone()
text = "지역:"+rs[2]+"\r\n"+rs[3]+"고객님의 인증키는 \r\n"+rs[5]+"\r\n입니다"
    ## 4 params(to, from, type, text) are mandatory. must be filled
params = dict()
params['type'] = 'sms' # Message type ( sms, lms, mms, ata )
params['to'] = '01066592209' # Recipients Number '01000000000,01000000001'
params['from'] = '01066592209' # Sender number
params['text'] = text # Message

cool = Message(api_key, api_secret)
try:
  response = cool.send(params)
  print("Success Count : %s" % response['success_count'])
  print("Error Count : %s" % response['error_count'])
  print("Group ID : %s" % response['group_id'])

  if "error_list" in response:
     print("Error List : %s" % response['error_list'])

except CoolsmsException as e:
  print("Error Code : %s" % e.code)
  print("Error Message : %s" % e.msg)

  sys.exit()

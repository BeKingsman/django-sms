import requests
import json
from credentials import EMAIL,USERNAME,SECRET_KEY



URL = 'https://www.sms4india.com/api/v1/sendCampaign'

# get request
def sendPostRequest(reqUrl, apiKey, secretKey, useType, phoneNo, senderId, textMessage):
  req_params = {
  'apikey':apiKey,
  'secret':secretKey,
  'usetype':useType,
  'phone': phoneNo,
  'message':textMessage,
  'senderid':senderId
  }
  return (requests.post(reqUrl, req_params))
# get response
response = sendPostRequest(URL, USERNAME, SECRET_KEY, 'stage', 9799813598, EMAIL, 'just for testing' )

print (response.text)

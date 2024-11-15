# -*- coding:utf-8 -*-
import urllib3
import json

openApiURL = "http://aiopen.etri.re.kr:8000/WiseQAnal"
accessKey = "42a375cd-d064-490f-888f-0600aba6333c"
text = "오늘 날짜알려줘"

requestJson = {
    "argument": {
        "text": text
    }
}

http = urllib3.PoolManager()
response = http.request(
    "POST",
    openApiURL,
    headers={"Content-Type": "application/json; charset=UTF-8", "Authorization": accessKey},
    body=json.dumps(requestJson)
)

print("[responseCode] " + str(response.status))
print("[responBody]")
print(str(response.data, "utf-8"))
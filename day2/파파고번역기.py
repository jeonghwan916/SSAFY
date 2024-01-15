import os
import sys
import urllib.request
import json

def doit(msg):
    client_id = "2n8boAJ6vtHPBmVeYYYN" # 개발자센터에서 발급받은 Client ID 값
    client_secret = "xJAiGzBX5x" # 개발자센터에서 발급받은 Client Secret 값
    encText = urllib.parse.quote(msg)
    data = "source=ko&target=en&text=" + encText
    url = "https://openapi.naver.com/v1/papago/n2mt"
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request, data=data.encode("utf-8"))
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        print(response_body.decode('utf-8'))
        print(type(response_body.decode('utf-8')))

        # 응답받은 json 포멧의 데이터를 파이썬 객체로 바꾸기 (디코딩)
        ret=json.loads(response_body.decode('utf-8'))
        print(type(ret))
        print(ret['message']['result']['translatedText'])

    else:
        print("Error Code:" + rescode)

msg=input()  # 번역할 메시지 입력받기
doit(msg)    # 입력받은 메시지 doit 함수로 전달하기
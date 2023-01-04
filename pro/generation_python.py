# encoding:utf-8

import requests
import json

'''
Code Generation
'''
API_KEY = "82359e5f0e3a4aa482843cb4c7cb0ddf"  # 从控制台获取
API_SECRET = "43cd071203bd410e99979d1982b59e1c"  # 从控制台获取
PROMPT = ""
NUMBER = 1
LANG = "PHP"
request_url = "https://tianqi.aminer.cn/api/v2/"
api = 'multilingual_code_generate'



# 指定请求参数格式为json
headers = {'Content-Type': 'application/json'}
request_url = request_url + api
data = {
    "apikey": API_KEY,
    "apisecret": API_SECRET,
    "prompt":PROMPT,
    "n":NUMBER,
    "lang":LANG
}

def main():
    response = requests.post(request_url, headers=headers, data=json.dumps(data))
    if response:
        print(response.json())

if __name__ == '__main__':
    main()

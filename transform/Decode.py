# coding:utf-8
import requests
import re

def getTempInfo(patten, strTemp):
    searchObj = re.search(patten, strTemp)
    if searchObj:
        #print "searchObj.group() : ", searchObj.group()
        #print "searchObj.group(1) : ", searchObj.group(1)
        return searchObj.group(1)
    else:
        print "Nothing found!!"

####################### 发送Get请求 ################################
def getDecode(uid, q, url):
    params = {"uid": uid,"q": q}
    res = requests.get(url=url, params=params)
    print(res.text)

def decodeFile(path, outPath):
    with open(path, encoding='utf-8') as file_obj:
        contents = file_obj.read()
        pattern = re.compile(r'Payload=<<"{(.*)">>')  # 查找数字
        resultList = pattern.findall(contents)
        for item in resultList:
            print(item)



if __name__ == '__main__':
    #读取xml文件
    #uid = "60ba2aba-3f7a-412b-bfc3-9241a4e5bdb21579501760396"
    #q = "aZKUJDxQE6hKIaBycL37lF61l6io-YODil4qeCB4Qi6t-puSmbQnAECIu_q051UBDVDJlwFMbG6VowkDjIGk-MAvm1HPfnNDXUW5uee1A9OUAxfF4hCfxg211nrB-uRjRltLEODcAygmtfqQ92ousbP66QFoKtmjKaiW4c4NEPM"
    url = "http://monitordevicetest.10101111.com/ucarmonitordevice/mqttDeviceMockSender/decryptQ.do_?"
    #getDecode(uid,q,url)

    strTemp = "\"q\":\"yXnZmD5M4s6cEd1NDN3lMTF1TIx5HLSgo5HZht5qK2PCj5RDi9wGQ0u08Xm68K7Zi2IKRYY-SzUsgum9XiZKNuRIxL5_Uyu8S4lzHeN1IH2dkBRp04VXWTQfoyNyNWrJWqSlmT5fnwIDKeGAaDVAny-Jzjn6qFNiyf9KwV9Q2O8\\u003d\\u003d\",\"sign\":\"989835319756959757680765076159123702\",\"timestamp\":1579504010910,\"uid\":\"5c3759c3-87e9-4051-ada5-8097cd10d87c1579504010158\"}"
    patten = r'\"uid\":\"(.*)\"}'
    uid = getTempInfo(patten,strTemp)
    print(uid)
    patten2 = r'\"q\":\"(.*)\",\"sign'
    temp = getTempInfo(patten2, strTemp)
    q = temp.replace("\\u003d","")
    print(q)
    getDecode(uid, q, url)

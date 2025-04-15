import requests
import json
if __name__ == "__main__":
    words = input("输入你想翻译的词语：")
    url = 'https://fanyi.baidu.com/sug'
    data = {
        'kw':words
    }
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    }
    dic_obj = requests.post(url=url,data=data,headers=headers).json()
    filename = f"./{words}.json"
    fp = open(filename,'w',encoding='utf-8')
    json.dump(dic_obj,fp=fp,ensure_ascii=False)
    print('over')
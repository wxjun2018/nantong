import json
import time
import requests
import urllib3

urllib3.disable_warnings()

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 '
                  'Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x6309071d) '
                  'XWEB/8529 Flue',
    'Content-Type': 'application/json',
    'userId': '74b44117626040afb2925617228776af',
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI3NGI0NDExNzYyNjA0MGFmYjI5MjU2MTcyMjg3NzZhZiIsIm9wZW5pZCI6Im9LeWF5dUFDMEMxMTYzQ3BTRU5icS1kN0IwenMiLCJleHAiOjE3MDczNzE5MjR9.SuQh1Buv92UtODQKKF2TT6QypJidDKTKKCiWtXexZaA',
    'Accept-Language': '*',
    'Origin': 'https://ntwlsc.zhwl.nantong.cn',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://ntwlsc.zhwl.nantong.cn/zjghynt-front/?code=001cUYkl2tlHRc4Azsml202zVa4cUYkf&state=STATE',
}

data_json = {
    "activityId": "685438601458089984",  # 6号15点，游船活动
    "rushtype": "01",
    "hasChildren": "",
}
data = json.dumps(data_json)

addOrderUrl = 'https://ntwlsc.zhwl.nantong.cn/mall-rush/rushPurchase/addOrder'

while True:
    try:
        response = requests.post(addOrderUrl, headers=headers, data=data, verify=False, timeout=30)
        response = json.loads(response.text)
        print(response, time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
        if response['message'] != '活动还未开始。' and response['code'] != 200:
            print(response.text)
            break
    except Exception as e:
        print('请求出错', e)
        continue
    finally:
        time.sleep(1)

import requests
import json

def getList(maxId, countNum, courseId, articleId, isReverse):
    url = 'https://www.biji.com/pc/bauhinia/pc/class/purchase/article_list'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4181.9 Safari/537.36', 'Content-Type': 'application/json; charset=utf-8'}
    payload = '{"chapter_id":"","count":' + str(countNum) + ',"detail_id":"' + str(courseId) + '","include_edge":false,"is_unlearn":false,"max_id":' + str(maxId) + ',"max_order_num":0,"reverse":' + str(isReverse) + ',"since_id":0,"since_order_num":0,"unlearn_switch":false}'

    response = requests.post(url=url, headers=headers, data=payload)
    result = response.content.decode('utf-8')
    resultJson = json.loads(result)
    for index in range(len(resultJson['c']['article_list'])):
        if resultJson['c']['article_list'][index]['enid'] == articleId:
            audio_m3u8 = resultJson['c']['article_list'][index]['audio']['mp3_play_url']
            audio_title = resultJson['c']['article_list'][index]['audio']['title']
            courseName = resultJson['c']['article_list'][index]['audio']['source_name']

    print(courseName + '-' + audio_title)
    print(audio_m3u8)


maxId = 0
countNum = 50
courseId = '5L9DznlwYyOVdwasGdKmbWABv0Zk4a'
articleId = 'wgpMLla6Py4qK25bpPXYmvNzjd2Zx1'
isReverse = 'true'
getList(maxId, countNum, courseId, articleId, isReverse)


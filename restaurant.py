import json
import requests
import sys
import io
with io.open('Mumbai.csv','w',encoding='utf-8') as f1:
    f1.write('name,area,totalRatingsString,deliveryTime,minDeliveryTime,maxDeliveryTime,costForTwoString+\n')
    f1.close()
sys.stdout.reconfigure(encoding='utf-8')

import requests

headers = {
    'authority': 'www.swiggy.com',
    '__fetch_req__': 'true',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/json',
    'cookie': '__SW=EA1zlwIKUU1jz17VIA6yTROzBQTeBT4E; _device_id=17ee724c-8997-b7db-6482-cc290be03d2b; fontsLoaded=1; _gcl_au=1.1.1720085660.1674312460; WZRK_G=5d6f5a4c7af24a1f8e1f436546b01782; userLocation={%22address%22:%22Nalasopara%20East%2C%20Nala%20Sopara%2C%20Maharashtra%2C%20India%22%2C%22area%22:%22%22%2C%22deliveryLocation%22:%22Nalasopara%20East%22%2C%22lat%22:19.4256875%2C%22lng%22:72.8373771}; _guest_tid=70714931-56e8-4f7c-8c94-f2ff7895e9f6; _sid=50k635eb-690d-434a-9348-306bfc4d61c0; _gid=GA1.2.875726348.1674571319; _ga_34JYJ0BCRN=GS1.1.1674571325.2.1.1674573084.0.0.0; WZRK_S_W86-ZZK-WR6Z=%7B%22p%22%3A1%2C%22s%22%3A1674573081%2C%22t%22%3A1674573201%7D; _ga=GA1.2.79383395.1674312461; _gat_UA-53591212-4=1',
    'referer': 'https://www.swiggy.com/city/mumbai?page=2',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (iPad; CPU OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/87.0.4280.77 Mobile/15E148 Safari/604.1',
}

params = (
    ('page', 0),
    ('ignoreServiceability', 'true'),
    ('lat', '19.2133035606211'),
    ('lng', '72.87611371920241'),
    ('pageType', 'SEE_ALL'),
    ('sortBy', 'RELEVANCE'),
    ('page_type', 'DESKTOP_SEE_ALL_LISTING'),
)

response = requests.get('https://www.swiggy.com/dapi/restaurants/list/v5', headers=headers, params=params)
response = response.text
data1 = json.loads(response)
page_no = data1['data']['pages']

dd = 0
for i in range (page_no):

    headers = {
        'authority': 'www.swiggy.com',
        '__fetch_req__': 'true',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/json',
        'cookie': '__SW=EA1zlwIKUU1jz17VIA6yTROzBQTeBT4E; _device_id=17ee724c-8997-b7db-6482-cc290be03d2b; fontsLoaded=1; _gcl_au=1.1.1720085660.1674312460; WZRK_G=5d6f5a4c7af24a1f8e1f436546b01782; userLocation={%22address%22:%22Nalasopara%20East%2C%20Nala%20Sopara%2C%20Maharashtra%2C%20India%22%2C%22area%22:%22%22%2C%22deliveryLocation%22:%22Nalasopara%20East%22%2C%22lat%22:19.4256875%2C%22lng%22:72.8373771}; _guest_tid=70714931-56e8-4f7c-8c94-f2ff7895e9f6; _sid=50k635eb-690d-434a-9348-306bfc4d61c0; _gid=GA1.2.875726348.1674571319; _ga_34JYJ0BCRN=GS1.1.1674571325.2.1.1674573084.0.0.0; WZRK_S_W86-ZZK-WR6Z=%7B%22p%22%3A1%2C%22s%22%3A1674573081%2C%22t%22%3A1674573201%7D; _ga=GA1.2.79383395.1674312461; _gat_UA-53591212-4=1',
        'referer': 'https://www.swiggy.com/city/mumbai?page=2',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (iPad; CPU OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/87.0.4280.77 Mobile/15E148 Safari/604.1',
    }

    params = (
        ('page', dd),
        ('ignoreServiceability', 'true'),
        ('lat', '19.2133035606211'),
        ('lng', '72.87611371920241'),
        ('pageType', 'SEE_ALL'),
        ('sortBy', 'RELEVANCE'),
        ('page_type', 'DESKTOP_SEE_ALL_LISTING'),
    )

    response = requests.get('https://www.swiggy.com/dapi/restaurants/list/v5', headers=headers, params=params)
    response = response.text
    dd = dd+1
    print('Page no. is '+str(dd))
    data1 = json.loads(response)
    data1 = data1['data']['cards']

    for i in range(len(data1)):
        name = data1[i]['data']['data']['name']
        area = data1 [i]['data']['data']['area']
        totalRatingsString = data1 [i]['data']['data']['totalRatingsString']
        deliveryTime = data1 [i]['data']['data']['deliveryTime']
        minDeliveryTime = data1 [i]['data']['data']['minDeliveryTime']
        maxDeliveryTime = data1 [i]['data']['data']['maxDeliveryTime']
        costForTwoString = data1 [i]['data']['data']['costForTwoString']
      
   
        scrapped_data = (name+", "+area+","+totalRatingsString+", "+str(deliveryTime)+","+str(minDeliveryTime)+","+str(maxDeliveryTime)+","+costForTwoString)
        with io.open('Mumbai.csv','a',encoding = 'utf-8') as f2:
            f2.write(scrapped_data+'\n')
            f2.close()

#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.get('https://www.swiggy.com/dapi/restaurants/list/v5?page=1&ignoreServiceability=true&lat=19.2133035606211&lng=72.87611371920241&pageType=SEE_ALL&sortBy=RELEVANCE&page_type=DESKTOP_SEE_ALL_LISTING', headers=headers)

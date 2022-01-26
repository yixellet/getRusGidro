from urllib.request import urlopen
import re

website = urlopen('http://www.rushydro.ru/hydrology/informer/')

html = website.read().decode('utf-8')

data = re.findall('value="\d{2}\.\d{2}\.\d{4}"', html)
print(data[0].split('"')[1])

with open('levels.json', 'a', encoding='utf-8') as file:
    date = re.findall('value="\d{2}\.\d{2}\.\d{4}"', html)
    gess = re.findall('<div class="data-block"[\S\s]+<sup>3', html)
    print(len(gess))
    data = {
        "date": data[0].split('"')[1],
        "data": [

        ]
    }

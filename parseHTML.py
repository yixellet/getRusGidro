import os
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs


def parseHTML(date, dataDir):
    baseURL = 'http://www.rushydro.ru/hydrology/informer/?date='
    website = urlopen(baseURL + date)
    html = website.read().decode('utf-8')

    soup = bs(html, 'lxml')

    dateInput = soup.find('input', id='popupDatepicker')
    date = dateInput['value']

    dataBlocks = soup.find_all('div', class_="data-block")
    for dataBlock in dataBlocks:
        river = dataBlock.img['src'].split('/')[-1][:-4]
        try:
            os.makedirs(os.path.join(dataDir, river))
            print('Создана директория "{0}"'.format(river))
        except:
            pass
        informerBlocks = dataBlock.find_all('div', class_="informer-block")
        for informerBlock in informerBlocks:
            wppName = informerBlock['class'][1]
            legendBlock = informerBlock.find('div', class_='legend')
            with open(os.path.join(dataDir, river, '{0}.csv'.format(wppName)), 'a', encoding='utf-8') as file:
                string = date + ','
                legendItems = legendBlock.find_all('p')
                for legendItem in legendItems:
                    string += legendItem.b.text.split(' ')[0] + ','
                string = string[:-1] + '\n'
                file.write(string)

if __name__ == '__main__':
    parseHTML('', 'data')
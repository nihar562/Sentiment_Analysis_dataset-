from bs4 import BeautifulSoup
import requests
import pandas as pd
## Reading input file
data = pd.read_excel('input.xlsx')

## Extract all information from all links
extracted = []
for i in range(len(data['URL'])):
    url = data['URL'][i]
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'}
    code = requests.get(url,headers=headers)
    soup = BeautifulSoup(code.content,'html.parser')
    title = soup.find('h1',class_='entry-title').text
    extracted.append(title)
    for j in soup.find_all('p'):
        extracted.append(j.text)
    with open(f'{str(i+1)}.txt', 'w',encoding='utf-8') as f:
        for line in extracted:
            f.write(line)
            f.write('\n')
    extracted.clear()

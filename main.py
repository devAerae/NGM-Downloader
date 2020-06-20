from requests import get
from bs4 import BeautifulSoup
import re

print('Made by Sepalum!')
print('=========================================')

def download(url, file_name = None):
	if not file_name:
		file_name = url.split('/')[-1]

	with open(file_name, "wb") as file:   
        	response = get(url)               
        	file.write(response.content)

musicID = input('음악 아이디를 입력해주세요 : ')

if (int(musicID) > 469776):
    source = get('https://www.newgrounds.com/audio/listen/' + musicID).text
    soup = BeautifulSoup(source, 'html.parser')
    fileName = str(soup.select('title')[0])
    fileName = fileName.replace('<title>','').replace('</title>','').replace(' ','-').replace('&','amp').replace('"','quot').replace('<','lt').replace('>','gt')
    if (len(fileName) > 27):
        fileName = fileName[:27]
    fileName = re.sub('[^a-zA-z0-9-]','',fileName)
    fileURL = 'https://audio-download.ngfiles.com/' + musicID[0:3] + '000/' + musicID + '_' + fileName + '.mp3'
    download(fileURL, musicID + '.mp3')
else:
    oldFileURL = 'https://www.newgrounds.com/audio/download/' + musicID
    download(oldFileURL, musicID + '.mp3')
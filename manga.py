import os
import re
import sys
from os import remove

import requests
from bs4 import BeautifulSoup

import argv
mangaName = (argv.k(sys.argv[1:]))
mangaChapterFirst = 1
mangaChapterEnd = 999  # default download all

for j in range(mangaChapterFirst, mangaChapterEnd + 1):
    mangaChapter = str(j)

    Url = 'https://goodmanga.net/' + mangaName + '/chapter/' + mangaChapter
    myPage = requests.get(Url).text
    soup = BeautifulSoup(myPage, "lxml")

    myPath = mangaName + '/' + mangaName + mangaChapter
    if not os.path.isdir(myPath):
        os.makedirs(myPath)

    # title=re.search(r'\w+')
    counter = re.search(r'<span>of (\d+?)</span>', myPage)
    print("downloading" + " " + mangaName + " " + "chapter" + " " +
          mangaChapter)
    print("this chapter counter is" + " " + counter.group(1))
    mangaCounter = int(counter.group(1))
    for i in range(1, mangaCounter + 1):
        imgUrlBase = 'https://www.goodmanga.net/images/manga/'
        imgUrlFina = mangaName + '/' + mangaChapter + '/' + str(i) + '.jpg'
        imgUrl = imgUrlBase + imgUrlFina
        page = requests.get(imgUrl)
        fileName = str(i) + '.jpg'
        filePath = myPath + '/' + fileName
        with open(filePath, 'wb') as out_file:
            out_file.write(page.content)
            a = os.path.getsize(filePath)
            # print(a)
            # if i == mangaCounter and a <= 74252:
            #     print('find useless file')
            #     out_file.close()
            #     remove(filePath)
            #     print('delete useless file done')
    print("this chapter is downloading done")

print("this manga downloading done")

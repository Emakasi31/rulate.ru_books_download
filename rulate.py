import requests
import fileinput
from urllib.request import urlopen,Request
from urllib.request import urlretrieve
from urllib.parse import quote
from bs4 import BeautifulSoup
from lxml.html.soupparser import fromstring


def geturl():
    table= Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    table = urlopen(table).read()
    bs= BeautifulSoup(table, features = "lxml")
    table=bs.findAll("a")
    for i in table:
        if i.get_text() =='Следующая глава':
            refs=i["href"]
            a='https://tl.rulate.ru'+str(refs)
    return a

def remove_trash(trash):
    ### Remove the target string
    with open('{0}.txt'.format(book_name), 'r') as file :
        filedata = file.read()
    filedata = filedata.replace(str(trash), '')
    with open('{0}.txt'.format(book_name), 'w') as file:
        file.write(filedata)
    file.close()

def trash_list():
        remove_trash('Зарегистрировавшись, вы сможете добавлять свои версии перевода, общаться в блоге, ставить\n                            оценки переводам.\n')
        remove_trash('Готово:\n')
        remove_trash('Вы не можете прослушивать данное аудио.\n')
        remove_trash('Использование:\n')
        remove_trash('\n                Авторские права переводчиков - их интеллектуальная собственность.\n')
        remove_trash('\n                Копирование материалов сайта с платной подписки запрещено к распространению.\n')
        remove_trash('Вы покидаете сайт tl.rulate.ru и переходите по внешней ссылке.\n')
        remove_trash('Убедитесь, что данная ссылка полностью является доверенной и ограждена от вредоносных влияний.\n')
        remove_trash('\n            Если же ссылка показалась вам подозрительной, убедительная просьба сообщить об этом администрации.\n')
        remove_trash('Нажмите на  чтоб перейти.\n')
        remove_trash('	В этой главе нет ни одного переведённого фрагмента.')
        remove_trash('Вы не можете прослушивать данное аудио.')
        remove_trash('                Авторские права переводчиков - их интеллектуальная собственность.\n')
        remove_trash('Копирование материалов сайта с платной подписки запрещено к распространению.')
        remove_trash('Использование:')
        remove_trash('К оглавлению |')


url= str(input('url: '))
#https://tl.rulate.ru/book/997/628115/ready
book_name = str(input('book name: '))

for charapter in range(1, 20000):
    response = requests.get(url)
    #add err response.status_code 404
    our_content = response.content
    our_file = open('{0}.txt'.format(book_name), 'a+')
    if charapter == 1:
        our_file.write('{0}\n'.format(book_name)+'\n')
    our_soup = BeautifulSoup(our_content, 'lxml')
    for tag in our_soup.find_all('p'):
            our_file.write(tag.text + '\n')
    print(url +  ' %d download' % (charapter))
    trash_list()
    try:
        url = geturl()
    except UnboundLocalError:
        break

our_file.close()

trash_list()














#import re
#strings = our_soup.find_all(string=re.compile('http://tl.rulate.ru/book'))
#for txt in strings:
#    print(" ".join(txt.split()))

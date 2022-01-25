#! python3
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

form_data = {
    'username': '',
    'password': ''
}

i = 2924
while i < 3031:
    login_post_url = 'https://kanji.koohii.com/account'
    internal_url = 'https://kanji.koohii.com/study/kanji/' + str(i)

    with requests.session() as sesh:
        sesh.post(login_post_url, data=form_data)    
        response = sesh.get(internal_url)
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')

        character = soup.find(class_='cj-k').get_text()
        keyword = soup.find(class_='JSEditKeyword').get_text()
        number = soup.find(class_='framenum').get_text()

        print(character + ',' + keyword + ',' + number)
        i += 1

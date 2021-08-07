import os
import requests
from bs4 import BeautifulSoup
from scraper import get_page
import ssl
import ext_url

ssl._create_default_https_context = ssl._create_unverified_context

s = requests.session()

print('Enter shikoto story project code below: ')
pj_code = input()

print('Enter the number of chapters below: ')
num = input()

print("Enter file name below: ")
file_name = input()

if not os.path.exists(file_name):
    os.mkdir(file_name)


main_page_url = 'https://www.shikoto.com/articles/{}.html'.format(pj_code)

main_page = s.get(main_page_url)

with open('page.html', 'wb') as f:
            content = get_page(main_page_url)
            f.write(content)
            f.close()

chap_list = []

chap_list = ext_url.ext_url(chap_list, num)

ticks = 0
for urls in chap_list:

    with open('content.html', 'wb') as f:
            content = get_page(urls)
            f.write(content)
            f.close()

    with open('content.html', 'r', encoding='utf-8') as fr:
        page_content = fr.read()
        soup = BeautifulSoup(page_content, 'html.parser')

        """

        count = 1
        for t in soup.find_all():
            if t.name=='div':
                print(t.getText())
                print(count)
                print("\n\n")
                count += 1
                
        """

        # the main story is in 17th div

        raw_text = soup.find_all('div')[16].get_text()

        # print(raw_text)

        fr.close()

        path = file_name + '_' + str(ticks) + '.txt'

        final_path = os.path.join(file_name, path)

        with open(final_path, 'w', encoding='utf-8') as f:

            f.write(raw_text)
            f.close()
        ticks += 1


s.close()
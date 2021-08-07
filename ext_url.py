from bs4 import BeautifulSoup

def ext_url(link_in_text, chap_count):

    with open('page.html', 'r', encoding='utf-8') as fr:
        page_content = fr.read()
        
        soup = BeautifulSoup(page_content, 'html.parser')

        all_a = soup.find_all('a')

        """
        count = 1
        for elements in all_a:
            print(count)
            print(elements)
            count += 1
        """
        # the url to chapter 1 is in 41th

        # print(all_a[40]['href'])

        index = 40

        for ticks in range(int(chap_count)):
            link_text = all_a[index]['href']
            URL = 'https://www.shikoto.com' + link_text
            
            link_in_text.append(URL)
            index += 1

        # print(list(link_in_text))
        return link_in_text

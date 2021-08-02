import requests

def get_page(url):
    s = requests.session()
    page = s.get(url)
    return page.content


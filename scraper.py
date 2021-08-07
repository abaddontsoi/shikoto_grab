import requests

def get_page(url):
    s = requests.session()
    page = s.get(url)
    status = '\"{URL}\":{STATUS}'.format(URL = url, STATUS = page.status_code)
    print(status)
    s.close()
    return page.content


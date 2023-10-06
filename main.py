import httpx,random,string,threading


def checker():
        
        prx = open('proxy.txt', 'r').read().splitlines()
        proxy = 'http://' + random.choice(prx)
        headers = {
            'Accept': '*/*',
            'Accept-Language': 'pl-PL',
            'Client-Id': 'kimne78kx3ncx6brgo4mv6wki5h1ko',
            'Client-Integrity': 'v4.public.eyJjbGllbnRfaWQiOiJraW1uZTc4a3gzbmN4NmJyZ280bXY2d2tpNWgxa28iLCJjbGllbnRfaXAiOiI3OS4xOTEuMjM0LjIyNyIsImRldmljZV9pZCI6IklnSEk0YTRKVWVaNjZnanV6dXNOYXF0a09KaW9haEl6IiwiZXhwIjoiMjAyMy0xMC0wNlQyMjo1NzowN1oiLCJpYXQiOiIyMDIzLTEwLTA2VDA2OjU3OjA3WiIsImlzX2JhZF9ib3QiOiJmYWxzZSIsImlzcyI6IlR3aXRjaCBDbGllbnQgSW50ZWdyaXR5IiwibmJmIjoiMjAyMy0xMC0wNlQwNjo1NzowN1oiLCJ1c2VyX2lkIjoiIn3yWB4B3XJz8-Wsaboe5SGVz6OFLZyMgUsfrzgtB9n-hD9vFHppUGkrBJjl7zEzChhqiYKsdlKLBrXGW2MdCZ4H',
            'Client-Session-Id': 'd1078a471ed967fd',
            'Client-Version': 'c321bc77-08a8-4cc5-b644-46db0d4dd034',
            'Connection': 'keep-alive',
            'Content-Type': 'text/plain;charset=UTF-8',
            'Origin': 'https://www.twitch.tv',
            'Referer': 'https://www.twitch.tv/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-site',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
            'X-Device-Id': 'IgHI4a4JUeZ66gjuzusNaqtkOJioahIz',
            'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }

        usernames = ''.join(random.choice(string.digits + string.ascii_letters) for _ in range(4))
        payload = '[{"operationName":"UsernameValidator_User","variables":{"username":"' + str(usernames) + '"},"extensions":{"persistedQuery":{"version":1,"sha256Hash":"fd1085cf8350e309b725cf8ca91cd90cac03909a3edeeedbd0872ac912f3d660"}}}]'

        try:
            r = httpx.post('https://gql.twitch.tv/gql', headers=headers, data=payload, proxies=proxy)

            result = r.json()[0]['data']['isUsernameAvailable']
            if result:
                print(f'✔ {usernames}')
                with open('x.txt', 'a') as file:
                    file.write(f'{usernames}\n')
            else:
                print(f'❌ {usernames}')
        except Exception as e:
            pass

def xxxx(xxxxx):
    threads = []

    for _ in range(xxxxx):
        thread = threading.Thread(target=checker)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == '__main__':
    xxxxx = int(input('Write how many check: '))
    with open('x.txt', 'w') as file:
        file.write('\n')
    xxxx(xxxxx)

# BY COSNEY 🤔

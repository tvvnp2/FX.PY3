import requests
def instagram_login(user,password):
	
             
             url = 'https://www.instagram.com/accounts/login/ajax/' 
             headers = {
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.9',
            'content-length': '275',
            'content-type': 'application/x-www-form-urlencoded',
            'cookie': 'ig_did=303991DA-0420-41AC-A26D-D9F27C8DF624; mid=YMdanwAEAAHbGwbzL3d_mjVac16b; csrftoken=voNeU14Q1AMv8Sg3TtyFW2KA2UkSJlpL;',
            'origin': 'https://www.instagram.com',
            'referer': 'https://www.instagram.com/',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36',
            'x-csrftoken': 'voNeU14Q1AMv8Sg3TtyFW2KA2UkSJlpL',
            'x-ig-app-id': '936619743392459',
            'x-ig-www-claim': 'hmac.AR3tv9HzzLkZIUlGMRu3lzHfEeePw9CgWg8cuXGO22LfU8x0',
            'x-instagram-ajax': '0c15f4d7d44a',
            'x-requested-with': 'XMLHttpRequest'
        }
            
             data = {
                'username': f'{user}',
                'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:&:{password}',
                'queryParams': '{}',
                'optIntoOneTap': 'false'
                }
             req_login = requests.post(url,headers=headers,data=data).text
             if 'authenticated":true' in req_login:
                 print('done login')
             elif 'To secure your account' in req_login :
                 print('secure')
             elif 'Sorry, there was a problem with your request' in req_login :
                 print('Block')
             else:
             	print('Bad login')
            


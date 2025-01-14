import requests
import os, sys
import time

def clear_console():
    if sys.platform.startswith('win'):
        os.system('cls')
    else:
        os.system('clear')

clear_console()

banner = f">    Kage Get Token By User & Pass\n>    Telegram Channel : @Blackdegens\n>    YouTube Channel : @Blackdegens"
print(banner)
print('-' * 40)
print('\033[0;32mNote : Accounts format is `email|pass` \nSave accounts in accounts.txt \033[0m')
print('-' * 40)

def get_captcha_token(api_key):
    while True:
        json_data = {
            'username': api_key
        }
        try:
            response = requests.get('https://cryptohubnp.pythonanywhere.com/get_captcha', json=json_data)
            response.raise_for_status()
            result = response.json()
            if result['success']:
                print('Captcha token retrieval successful')
                return result['token']
            else:
                time.sleep(0.5)  # Wait before retrying
        except requests.RequestException as e:
            print(f"Error getting captcha token: {e}")
            time.sleep(1)  # Wait before retrying

def login_accounts(email, password, captcha_token):
    try:
        json_data = {
            'user': email,
            'password': password,
            'remember_me': True,
            'recaptcha_token': captcha_token
        }
        headers = {
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/json',
            'origin': 'https://play.google.com/store/apps/details?id=io.chirptoken.kage',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'
        }
        # Assuming this is the login endpoint for Kage. Adjust as necessary.
        url = "https://api.kage.com/auth/login"  # This is a placeholder; use the actual endpoint
        response = requests.post(url, headers=headers, json=json_data, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        return f'Error during login request: {str(e)}'

api_key = input('Enter Captcha API key: ')
print('-' * 40)

accounts_list = open('accounts.txt', 'r').read().splitlines()

for account in accounts_list:
    email, password = account.split('|')
    print(f'Trying to login with account: {email}')
    captcha_token = get_captcha_token(api_key)
    token_data = login_accounts(email, password, captcha_token)
    
    if isinstance(token_data, str):  # Check if we got an error string instead of a JSON response
        print(f'\033[0;31mLogin failed: {token_data}\033[0m')
    else:
        try:
            token = token_data['data']['token']
            with open('token.txt', 'a') as file:
                file.write(token + '\n')
            print('Token saved successfully')
        except KeyError:
            print(f'\033[0;31mFailed to get token for {email}: Response data missing token\033[0m')
    
    print('-' * 40)

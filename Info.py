import os
import logging
from dotenv import load_dotenv
import cloudscraper

# Load environment variables
load_dotenv()

# Configurations
class Config:
    API_BASE_URL = "https://api.chirptoken.io"
    REFERER = "https://play.google.com/store/apps/details?id=io.chirptoken.kage"
    USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
    TOKENS = os.getenv('KAGE_TOKENS', '').split(',')
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')

    @staticmethod
    def get_headers(token: str) -> dict:
        return {
            'authority': Config.API_BASE_URL.split('//')[-1],
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/json',
            'referer': Config.REFERER,
            'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Linux"',
import os
import logging
from dotenv import load_dotenv
import cloudscraper

# Load environment variables
load_dotenv()

# Configurations
class Config:
    API_BASE_URL = "https://api.chirptoken.io"
    REFERER = "https://play.google.com/store/apps/details?id=io.chirptoken.kage"
    USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
    TOKENS = os.getenv('KAGE_TOKENS', '').split(',')
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')

    @staticmethod
    def get_headers(token: str) -> dict:
        return {
            'authority': Config.API_BASE_URL.split('//')[-1],
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/json',
            'referer': Config.REFERER,
            'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Linux"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'cross-site',
            'user-agent': Config.USER_AGENT,
            'authorization': f'Bearer {token}'
        }

# Set up logging
logging.basicConfig(level=Config.LOG_LEVEL, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

# Banner for the script
banner = f"""
>    Kage Referral Generator
>    Telegram Channel : @Blackdegens
>    YouTube Channel : @Blackdegens
----------------------------------------
\033[0;32mNote : Save Kage tokens in 
token.txt, one token per line \033[0m
----------------------------------------"""

def generate_referral(token: str) -> str:
    scraper = cloudscraper.create_scraper()
    try:
        response = scraper.post(f'{Config.API_BASE_URL}/api/referrals/generate', headers=Config.get_headers(token))
        response.raise_for_status()
        referral_data = response.json()
        return f"Referral Code: {referral_data.get('referral_code', 'Error')}\nReferral Link: {referral_data.get('referral_link', 'Error')}"
    except Exception as e:
        logger.error(f"Error generating referral for token: {token[:8]}... Error: {str(e)}")
        return "Error generating referral"

def check_wallet_status(token: str) -> str:
    scraper = cloudscraper.create_scraper()
    try:
        response = scraper.get(f'{Config.API_BASE_URL}/api/wallet/status', headers=Config.get_headers(token))
        response.raise_for_status()
        data = response.json()['data']
        return f"Wallet: {data['wallet_address']}\nEmail: {data['email']}\nStatus: {(data['status']).capitalize()}"
    except Exception as e:
        logger.error(f"Error checking wallet status for token: {token[:8]}... Error: {str(e)}")
        return 'Wallet Status: Error to check'

def get_balance_info(token: str) -> str:
    scraper = cloudscraper.create_scraper()
    try:
        response = scraper.get(f'{Config.API_BASE_URL}/api/user/balance', headers=Config.get_headers(token))
        response.raise_for_status()
        return f"Balance: {response.json()['data']['balance']}"
    except Exception as e:
        logger.error(f"Error getting balance for token: {token[:8]}... Error: {str(e)}")
        return 'Process Error'

def process_token(token: str):
    print(f"Processing token: {token[:8]}...")
    print(get_balance_info(token))
    print(generate_referral(token))
    print(check_wallet_status(token))
    print('----------------------------------------')

def main():
    clear_console()
    print(banner)
    
    if not Config.TOKENS:
        logger.error("No tokens found in environment variable KAGE_TOKENS.")
        return

    for token in Config.TOKENS:
        process_token(token)

    print('All Account Checks Complete')
    input('Press Enter to Exit ')

if __name__ == "__main__":
    main()￼Enter            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'cross-site',
            'user-agent': Config.USER_AGENT,
            'authorization': f'Bearer {token}'
        }

# Set up logging
logging.basicConfig(level=Config.LOG_LEVEL, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

# Banner for the script
banner = f"""
>    Kage Referral Generator
>    Telegram Channel : @Blackdegens
>    YouTube Channel : @Blackdegens
----------------------------------------
\033[0;32mNote : Save Kage tokens in 
token.txt, one token per line \033[0m
----------------------------------------"""

def generate_referral(token: str) -> str:
    scraper = cloudscraper.create_scraper()
y:
        response = scraper.post(f'{Config.API_BASE_URL}/api/referrals/generate', headers=Config.get_headers(token))
        response.raise_for_status()
        referral_data = response.json()
        return f"Referral Code: {referral_data.get('referral_code', 'Error')}\nReferral Link: {referral_data.get('referral_link', 'Error')}"
    except Exception as e:
        logger.error(f"Error generating referral for token: {token[:8]}... Error: {str(e)}")
        return "Error generating referral"

def check_wallet_status(token: str) -> str:
    scraper = cloudscraper.create_scraper()
    try:
        response = scraper.get(f'{Config.API_BASE_URL}/api/wallet/status', headers=Config.get_headers(token))
        response.raise_for_status()
        data = response.json()['data']
        return f"Wallet: {data['wallet_address']}\nEmail: {data['email']}\nStatus: {(data['status']).capitalize()}"
    except Exception as e:
        logger.error(f"Error checking wallet status for token: {token[:8]}... Error: {str(e)}")
        return 'Wallet Status: Error to check'

def get_balance_info(token: str) -> str:
    scraper = cloudscraper.create_scraper()
    try:
        response = scraper.get(f'{Config.API_BASE_URL}/api/user/balance', headers=Config.get_headers(token))
        response.raise_for_status()
        return f"Balance: {response.json()['data']['balance']}"

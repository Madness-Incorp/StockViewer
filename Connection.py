import requests

def check_internet_connection():
    try:
        response = requests.get('https://google.com')
        return True
    except requests.exceptions.ConnectionError:
        return False
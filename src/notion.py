import sys
import requests
from colorama import Fore, Style

def info(*msg):
    print(f"{Style.BRIGHT}{Fore.GREEN}[INFO]:{Style.RESET_ALL}", *msg)

def error(*msg):
    print(f"{Style.BRIGHT}{Fore.RED}[ERROR]:{Style.RESET_ALL}", *msg)
    sys.exit(1)

def exception(_exception, *msg):
    print(f"{Style.BRIGHT}{Fore.RED}[ERROR]<{_exception.__class__.__name__}>:{Style.RESET_ALL} {_exception.args}")
    sys.exit(2)

class Notion:
    API = "https://api.notion.com/v1"

    def __init__(self):
        self.headers = {
            "Authorization": "",
            "Notion-Version": "2025-09-03"
        }

    def set_bearer_api_key(self, api_key: str):
        self.headers["Authorization"] = f"Bearer {api_key}"
    
    def set_notion_version(self, version: str):
        self.headers["Notion-Version"] = version
    
    def request(self, func, method, *args, **kwargs):
        return func(self.API + method, *args, headers=self.headers, **kwargs)

    def get_database(self, database_id: str):
        res = self.request(requests.get, f"/databases/{database_id}")
        return res.json()
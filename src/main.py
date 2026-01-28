from notion import Notion, info

api = open(".api_key", "r").read()

n = Notion()
n.set_bearer_api_key(api)

info(n.get_database("2f6a67c3b14781879f14d8fe33ca5bb0")["data_sources"])
from notion import Notion, info
import json

api = open(".api_key", "r").read()

n = Notion()
n.set_bearer_api_key(api)

sources = n.get_database("2f6a67c3b14781879f14d8fe33ca5bb0")["data_sources"]

for src in sources:
    pages = n.get_pages_from_datasource(src["id"])
    for page in pages["results"]:
        props = page["properties"]
        info("Page id:", page["id"])
        info("Name:", props["Name"]["title"][0]["plain_text"])
        info("Status:", props["Status"].get("status", {}).get("name"))
        
        date = props["Due date"]["date"]
        if date:
            info("Due date:", date.get("end"))
        else:
            info("No due date")
        info("Priority:", props["Priority"]["select"])

        info("Description:", props["Description"]["rich_text"][0]["plain_text"])
        print("\n")
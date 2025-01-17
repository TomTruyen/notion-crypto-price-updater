import json
import time

import requests
import yaml


class NotionCryptoPriceUpdater:

    def __init__(self):
        """
        Gets required variable data from config yaml file.
        """
        print("Initializing NotionCryptoPriceUpdater...")
        with open("my_variables.yml", 'r') as stream:
            try:
                self.my_variables_map = yaml.safe_load(stream)
                print("Loaded variables from my_variables.yml")
            except yaml.YAMLError as exc:
                print("[Error]: while reading yml file", exc)
        self.my_variables_map["NOTION_ENTRIES"] = {}
        self.getDatabaseId()
        self.getNotionDatabaseEntities()

    def getDatabaseId(self):
        print("Fetching Notion database ID...")
        url = "https://api.notion.com/v1/databases/"
        headers = {
            'Notion-Version': '2021-05-13',
            'Authorization':
                'Bearer ' + self.my_variables_map["MY_NOTION_SECRET_TOKEN"]
        }
        response = requests.request("GET", url, headers=headers)
        self.my_variables_map["DATABASE_ID"] = response.json()["results"][0]["id"]
        print(f"Database ID: {self.my_variables_map['DATABASE_ID']}")

    def getNotionDatabaseEntities(self):
        print("Fetching Notion database entities...")
        url = f"https://api.notion.com/v1/databases/{self.my_variables_map['DATABASE_ID']}/query"
        headers = {
            'Notion-Version': '2021-05-13',
            'Authorization': 'Bearer ' + self.my_variables_map["MY_NOTION_SECRET_TOKEN"]
        }
        response = requests.request("POST", url, headers=headers)
        resp = response.json()
        for v in resp["results"]:
            self.my_variables_map["NOTION_ENTRIES"].update({v["properties"]["Name"]["title"][0]["text"]["content"]: {"page": v["id"], "price": float(v["properties"]["Price/Coin"]["number"])}})
        print(f"Fetched {len(self.my_variables_map['NOTION_ENTRIES'])} entries from Notion database")

    def getCryptoPrices(self):
        """
        Download the required crypto prices using Binance API.
        Ref: https://github.com/binance/binance-api-postman
        """
        print("Fetching crypto prices from Binance...")
        for name, data in self.my_variables_map["NOTION_ENTRIES"].items():
            url = f"https://api.binance.com/api/v3/avgPrice?"\
                f"symbol={name}USDT"
            response = requests.request("GET", url)
            if response.status_code == 200:
                content = response.json()
                data['price'] = content['price']
                print(f"Updated price for {name}: {data['price']}")

    def updateNotionDatabase(self, pageId, coinPrice):
        """
        A notion database (if integration is enabled) page with id `pageId`
        will be updated with the data `coinPrice`.
        """
        print(f"Updating Notion database for page ID {pageId} with price {coinPrice}...")
        url = "https://api.notion.com/v1/pages/" + str(pageId)
        headers = {
            'Authorization':
                'Bearer ' + self.my_variables_map["MY_NOTION_SECRET_TOKEN"],
            'Notion-Version': '2021-05-13',
            'Content-Type': 'application/json'
        }
        payload = json.dumps({
            "properties": {
                "Price/Coin": {
                    "type": "number",
                    "number": float(coinPrice),
                },
            }
        })
        response = requests.request(
                "PATCH", url, headers=headers, data=payload
            )
        print(f"Response from Notion: {response.text}")

    def UpdateIndefinitely(self):
        """
        Orchestrates downloading prices and updating the same
        in notion database.
        """
        print("Starting indefinite update loop...")
        while True:
            try:
                self.getNotionDatabaseEntities()
                self.getCryptoPrices()
                for _, data in self.my_variables_map["NOTION_ENTRIES"].items():
                    self.updateNotionDatabase(
                        pageId=data['page'],
                        coinPrice=data['price'],
                    )
                    time.sleep(2 * 10)
                time.sleep(1 * 60)
            except Exception as e:
                print(f"[Error encountered]: {e}")


if __name__ == "__main__":
    # With sleeps to prevent rate limit from kicking in.
    NotionCryptoPriceUpdater().UpdateIndefinitely()
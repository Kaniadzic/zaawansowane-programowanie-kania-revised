
import requests
import json


class Brewery:
    def __init__(self,
                 id: int, name: str, brewery_type: str, street: str,
                 city: str, state: str, postal_code: str, country: str,
                 phone: str, website_url: str):
        self.id = id
        self.name = name
        self.brewery_type = brewery_type
        self.street = street
        self.city = city
        self.state = state
        self.postal_code = postal_code
        self.country = country
        self.phone = phone
        self.website_url = website_url

    def __str__(self) -> str:
        return f'Brewery {self.name} is located in {self.city}, {self.country}'


class HttpClient:
    def __init__(self, url: str, endpoint: str):
        self.url = f'{url}/{endpoint}'

    def get(self, items_per_page: int):
        return requests.get(
            self.url,
            params={'per_page': items_per_page}
        ).content

    def deserialize_data(self, data: dict):
        data = json.loads(data)
        breweries = []

        for d in data:
            brewery = Brewery(
                d["id"],
                d["name"],
                d["brewery_type"],
                d["street"],
                d["city"],
                d["state"],
                d["postal_code"],
                d["country"],
                d["phone"],
                d["website_url"],
            )
            breweries.append(brewery.__str__())

        return breweries


http_client = HttpClient("https://api.openbrewerydb.org", "breweries")
breweries = http_client.deserialize_data(http_client.get(20))
print(breweries[0])

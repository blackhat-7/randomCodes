import requests
import json


class Scraper:
    def __init__(self):
        params = {
            "api_key": "tNqJ6coGLCBB",
            "format": "json"
        }
        r = requests.get('https://www.parsehub.com/api/v2/projects/t33Gqwjzcm4R/last_ready_run/data', params=params)
        self.data = json.loads(r.text)
        # print(self.data)

    def get_world_data(self):
        print('World Data')
        for item in self.data['world']:
            print(item['name'], item['value'])

    def get_country_data(self, country_name):
        for country in self.data['country']:
            if country['name'].lower() == country_name.lower():
                for item in country:
                    print(item + ': ' + country[item])


if __name__ == '__main__':
    sc = Scraper()
    sc.get_world_data()

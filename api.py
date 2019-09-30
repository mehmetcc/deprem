from crawler import KandilliCrawler
import json

class Kandilli:

    instance = KandilliCrawler.get_instance()

    @staticmethod
    def get_latest():
        return Kandilli.instance.kandilli_data[0]

    @staticmethod
    def get_earthquakes():
        return Kandilli.instance.kandilli_data
    
    @staticmethod
    def to_json():
        return json.dumps(Kandilli.instance.kandilli_data)



print(Kandilli.to_json())
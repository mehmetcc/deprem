from lxml import html
import requests
import logging


class KandilliCrawler:

    __instance = None

    def __init__(self):
        logging.basicConfig(level=logging.DEBUG)

        if KandilliCrawler.__instance != None:
            logging.error('This is a singleton object. It is not possible to create an instance of it')
        else:
            KandilliCrawler.__instance = self


        self.start_url = 'http://www.koeri.boun.edu.tr/scripts/lst0.asp'
        self.kandilli_data = self._format(self._parse())


    @staticmethod
    def get_instance():
        if KandilliCrawler.__instance == None:
            return KandilliCrawler()
        else:
            logging.error('This is a singleton object. It is not possible to create an instance of it')

    def parse(self):
        document = self._parse()
        return self._format(document)

    def _parse(self):
        logging.info("Crawling started")
        page = requests.get(self.start_url)
        tree = html.fromstring(page.content)
        logging.info("Kandilli successfully crawled")

        return tree.xpath('//body/pre/text()')[0].splitlines()[7:-1]

    def _format(self, incoming):

        dictified_list = list()

        for line in incoming:
            dictified = dict()

            split_line = line.split()
            tarih = split_line[0]
            saat = split_line[1]
            enlem = split_line[2]
            boylam = split_line[3]
            derinlik = split_line[4]
            buyukluk = split_line[6]

            yer_list = list()

            for i in range(8, len(split_line)-1, 1):
                if split_line[i] is 'İlksel':
                    break
                elif 'REVIZE' in split_line[i]:
                    break
                else:
                    yer_list.append(split_line[i])

            dictified['tarih'] = tarih
            dictified['saat'] = saat
            dictified['enlem'] = enlem
            dictified['boylam'] = boylam
            dictified['derinlik'] = derinlik
            dictified['buyukluk'] = buyukluk
            yer = ' '.join(yer_list)
            dictified['yer'] = yer

            dictified_list.append(dictified)

        logging.debug("Processing successfull")
        return dictified_list


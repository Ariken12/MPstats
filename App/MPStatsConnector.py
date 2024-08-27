from Requests import OzonRequest, WildberriesRequest


class MPStatsConnector():
    def __init__(self, token):
        self.token = token
        self.ozon_brands = []
        self.wildberries_brands = []
        self.ids_ozon = []
        self.ids_wildberries = []
    
    def add_id(self, id, site='ozon'):
        if site == 'ozon':
            self.ids_ozon.append(id)
        elif site == 'wildberries':
            self.ids_wildberries.append(id)

    def search(self):
        pass
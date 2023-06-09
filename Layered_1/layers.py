class DataLayer:
    items = []

    def __init__(self):
        self.connect_db()

    def connect_db(self):
        self.items = [
            Item("One", "1"),
            Item("Two", "2"),
            Item("Three", "3"),
            Item("Four", "4"),
        ]

    def get_item_value(self, item_key):
        return next((item.pair_value for item in self.items if item.pair_key == item_key), None)

    def get_items_keys(self):
        return [item.pair_key for item in self.items]


class Item:
    pair_key = None
    pair_value = None

    def __init__(self, pair_key, pair_value=None):
        self.pair_key = pair_key
        self.pair_value = pair_value


class ApplicationLayer:
    is_init = False
    database = None
    names_cache = None

    def __init__(self, db_layer: DataLayer):
        self.database = db_layer
    
    def load_cache(self):
        if(self.is_init):
            return False
        
        self.names_cache = self.database.get_items_keys()
        self.is_init = True
    
    def cache_init_protection(self):
        if(not self.is_init):
            self.load_cache()

    def get_item_value(self, item_key):
        self.cache_init_protection()
        try:
            if item_key not in self.names_cache: 
                return None
            
            print('Pair value:', self.database.get_item_value(item_key))
            return self.database.get_item_value(item_key)
        except:
            return None

class PresentationLayer:
    application_interface = None
    def __init__(self, application: ApplicationLayer) -> None:
        self.application = application

    def get_item_value(self):
        item_key = input("Item key:")
        search_res = self.application.get_item_value(item_key)
        if search_res is None:
            print(f'No [{item_key}] values in database')
        else:
            print(f'[{item_key}] key paired with [{search_res}]')
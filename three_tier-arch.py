class Data:
    def __init__(self) -> None:
        
        self.data = {
            'order' : {'item': 'laptop','price': 4500},
            'order2' : {'item': 'laptop','price': 5500},
            'order3' : {'item': 'laptop','price': 2500},
            'order4' : {'item': 'laptop','price': 45200},
        }

    def get_order_detail(self,orderId):
        return self.data[orderId]

class Application:
    pass

class GUI:
    pass
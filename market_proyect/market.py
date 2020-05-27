import connection

class Market():
    def __init__(self, name):
        self.__name = name        
    
    def __str__(self):
        return self.__name
    
    def marketSelect(self, select):        
        return connection.executeSelect(select)

if __name__ == "__main__":
    market = Market("elecrec")
    print(market)
    s = "SELECT * FROM MARKET"
    print(market.marketSelect(s))

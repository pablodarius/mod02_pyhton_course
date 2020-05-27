import sqlite3

bbdd = "supermarketfood.db"

def executeSelect(select):
    # conexion y se creara si no existe la BBDD
    conect = sqlite3.connect(bbdd)
    cursor = conect.cursor()
    cursor.execute(select)
    result = cursor.fetchall()   
    conect.close()

    return result

if __name__ == "__main__":    
    print(executeSelect( "SELECT * FROM MARKET" ))
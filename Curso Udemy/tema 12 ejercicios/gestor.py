from io import open
import pickle

class Personaje:
    
    # Constructor de clase
    def __init__(self, nombre, vida, ataque, defensa, alcance):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
        self.defensa = defensa
        self.alcance = alcance
        print('Se ha creado el personaje:', self.nombre)
        
    def __str__(self):
        return '{}: {} de vida, {} de ataque, {} de defensa y {} de alcance'.format(self.nombre, self.vida, self.ataque, self.defensa, self.alcance)


class Gestor:
    
    personajes = []
    
    # Constructor de clase
    def __init__(self):
        self.cargar()
        
    def agregar(self,p):
        for i in self.personajes:
            if p.nombre == i.nombre:
                print("Ya existe!")
                return                
        self.personajes.append(p)
        self.guardar()

    def mostrar(self):
        if len(self.personajes) == 0:
            print("El archivo está vacío.")
            return
        for p in self.personajes:
            print(p)
    
    def borrar(self,nombre):
        if len(self.personajes) == 0:
            print("El archivo está vacío.")
            return
        for i,n  in enumerate(self.personajes):
            if nombre == n.nombre:
                del self.personajes[i]                
                print("Borrado el", nombre)
                self.guardar()
    
    def cargar(self):
        fichero = open("personajes.pckl", "ab+") # append binario de lectura y escritura, si no existe lo crea
        fichero.seek(0) #el modo append deja el fichero al final
        try:
            self.personajes = pickle.load("fichero")
        except:
            pass
            # print("El fichero está vacío") # la primera vez que haga load dará error vendra aqui
        finally:
            fichero.close()            
            print("Se han cargado {} personajes.".format( len(self.personajes) ))
    
    def guardar(self):
        fichero = open("personajes.pckl","wb")
        pickle.dump(self.personajes, fichero)
        fichero.close()        
    
    # destructor de clase
    def __del__(self):
        self.guardar() # guardado automático
        print("Se ha guardado el fichero.")


if __name__ == "__main__":    
    g = Gestor()
    g.agregar( Personaje("Caballero",4,2,4,2))
    g.agregar( Personaje("Caballero",4,2,4,2))
    g.agregar( Personaje("Guerrero",2,4,2,4))  
    g.agregar( Personaje("Arquero",2,4,1,8))      
    del(g)
    g = Gestor()
    g.mostrar() 
    g.borrar("Arquero")
    g.mostrar() 
    del(g)
    g = Gestor()
    g.mostrar() 
    del(g)
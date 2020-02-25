from random import randint, uniform,random

class MyThermometer():
    def __init__(self):
        self.__unit = 'C'
        self.__temperature = 0
    
    def __str__(self):
        return "Temperature {}° {}".format(self.__temperature, self.__unit)

    def unit(self, unit):
        if unit == None:
            return self.__unit
        else:
            if unit == 'C' or unit == 'F':
                self.__unit = unit

    def temperature(self, temperature):
        if temperature == None:
            return self.__temperature
        else:
            try:
                temperature = float(temperature)
                self.__temperature = temperature
            except:
                self.__temperature = 0
    
    def converter(self, unit):
        if unit == self.__unit:
            self.__str__()                        
        else:
            if unit == 'F':                
                self.temperature(self.__temperature * 9/5 + 32)
                self.unit('F')                
            elif unit == 'C':                
                self.temperature((self.__temperature - 32) * 5/9)
                self.unit('F')  
            else:
                return "Wrong unit"
    
    def takeTemperatureCelsius(self):
        temperature = randint(-32, 42)
        self.temperature(temperature)
        self.unit('C')

t = MyThermometer()
print(t)
t.takeTemperatureCelsius()
print(t)
t.converter('F')
print(t)






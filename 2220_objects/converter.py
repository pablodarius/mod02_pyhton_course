class Thermometer():
    def __init__(self):
        self.__unit = 'C'
        self.__temperature = 0
    
    def __str__(self):
        return "Temperature {}° {}".format(self.temperature, self.unit)

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
                temperature = int(temperature)
                self.__temperature = temperature
            except:
                self.__temperature = 0
    
    def converter(self, temperature, unit):
        if unit == 'C':
            return "{}° F".format(temperature * 9/5 + 32)
        elif unit == 'F':
            return "{}° C".format((temperature - 32) * 5/9)
        else:
            return "Wrong unit"
    
    def takeTemperature(self, unit):
        if unit == None or unit == self.__unit:
            return self.__str__()
        else:
            if unit == 'F' or unit == 'C':
                return self.converter(self.__temperature, unit)
            else:
                return self.__str__()



t = Thermometer()
t.unit('F')
t.unit()
t.takeTemperature
print(t.converter(0, 'C'))
print(t)
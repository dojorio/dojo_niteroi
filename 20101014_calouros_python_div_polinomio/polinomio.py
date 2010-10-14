class Polinomio(object):
    def __init__(self, coeficientes):
        self.coeficientes = coeficientes
        self.__quociente = None
        self.__resto = None

    def __eq__(self, polinomio):
        return self.coeficientes == polinomio.coeficientes

    def dividir_por(self, divisor):
        quociente = self.coeficientes[0] / divisor.coeficientes[0]
        self.__quociente = Polinomio([quociente])

        resto = self.coeficientes[0] % divisor.coeficientes[0]
        self.__resto = Polinomio([resto])

    @property
    def quociente(self):
        return self.__quociente

    @property
    def resto(self):
        return self.__resto

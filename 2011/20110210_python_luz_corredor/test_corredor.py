import unittest2
from corredor import anda_corredor

class TestCorredor(unittest2.TestCase):

    def test_lista_on_para_corredor_de_uma_lampada(self):
        numero_de_lampadas = 1

        estado_lampadas = anda_corredor(numero_de_lampadas)

        estado_desejado = ['on']
        self.assertEquals(estado_lampadas, estado_desejado)

    def test_lista_on_off_para_corredor_de_duas_lampadas(self):
        numero_de_lampadas = 2

        estado_lampadas = anda_corredor(numero_de_lampadas)

        estado_desejado = ['on', 'off']
        self.assertEquals(estado_lampadas, estado_desejado)

    def test_lista_on_off_off_para_corredor_de_tres_lampadas(self):
        numero_de_lampadas = 3

        estado_lampadas = anda_corredor(numero_de_lampadas)

        estado_desejado = ['on', 'off', 'off']
        self.assertEquals(estado_lampadas, estado_desejado)

    def test_lista_on_off_off_on_para_corredor_de_quatro_lampadas(self):
        numero_de_lampadas = 4

        estado_lampadas = anda_corredor(numero_de_lampadas)

        estado_desejado = ['on', 'off', 'off', 'on']
        self.assertEquals(estado_lampadas, estado_desejado)

    def test_lista_on_off_off_on_off_para_corredor_de_cinco_lampadas(self):
        numero_de_lampadas = 5

        estado_lampadas = anda_corredor(numero_de_lampadas)

        estado_desejado = ['on', 'off', 'off', 'on', 'off']
        self.assertEquals(estado_lampadas, estado_desejado)

    def test_lista_on_off_off_on_off_off_para_corredor_de_seis_lampadas(self):
        numero_de_lampadas = 6

        estado_lampadas = anda_corredor(numero_de_lampadas)

        estado_desejado = ['on', 'off', 'off', 'on', 'off', 'off']
        self.assertEquals(estado_lampadas, estado_desejado)

    def test_lista_on_off_off_on_off_off_para_corredor_de_sete_lampadas(self):
        numero_de_lampadas = 7

        estado_lampadas = anda_corredor(numero_de_lampadas)

        estado_desejado = ['on', 'off', 'off', 'on', 'off', 'off', 'off']
        self.assertEquals(estado_lampadas, estado_desejado)

    def test_lista_on_off_off_on_off_off_para_corredor_de_8_lampadas(self):
        numero_de_lampadas = 8

        estado_lampadas = anda_corredor(numero_de_lampadas)

        estado_desejado = ['on', 'off', 'off', 'on', 'off', 'off', 'off', 'off']
        self.assertEquals(estado_lampadas, estado_desejado)

    def test_lista_on_off_off_on_off_off_para_corredor_de_9_lampadas(self):
        numero_de_lampadas = 9

        estado_lampadas = anda_corredor(numero_de_lampadas)

        estado_desejado = ['on', 'off', 'off', 'on', 'off', 'off', 'off', 'off', 'on']
        self.assertEquals(estado_lampadas, estado_desejado)

unittest2.main()

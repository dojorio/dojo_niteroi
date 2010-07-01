import unittest
from sueca import Carta
from sueca import somatorio
from sueca import rodada

class TestGanhadorDaRodada(unittest.TestCase):

    def test_jogador_1_ganha_com_A_copas_trunfo_Copas(self):
        cartas = [
            Carta('Copas', 'A'),
            Carta('Copas', '3'),
            Carta('Copas', '4'),
            Carta('Copas', '5'),
        ]
        trunfo = "Copas"
        self.assertEquals(rodada(cartas, trunfo), (0)

class TestSomatorioMesa(unittest.TestCase):
    def test_2_3_4_5_retorna_0(self):
        cartas = [
            Carta('Copas', '2'),
            Carta('Copas', '3'),
            Carta('Copas', '4'),
            Carta('Copas', '5'),
        ]
        self.assertEquals(somatorio(cartas), 0)

    def test_A_3_4_5_retorna_11(self):
        cartas = [
            Carta('Copas', 'A'),
            Carta('Copas', '3'),
            Carta('Copas', '4'),
            Carta('Copas', '5')]
        self.assertEquals(somatorio(cartas), 11)

if __name__ == '__main__':
    unittest.main()

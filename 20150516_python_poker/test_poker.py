import unittest
from poker_FODA import poker

class TestPoker(unittest.TestCase):

    def test_maior_carta(self):
        mao = ['2o', '3c', '5e', '6p', '7o']
        self.assertEqual(poker(mao), 'maior carta')

    def test_par(self):
        mao = ['2o', '2c', '3e', 'Jo', 'Qp']
        self.assertEqual(poker(mao), 'um par')

    def test_par2(self):
        mao = ['2o', '2c', '3e', 'Qo', 'Kp']
        self.assertEqual(poker(mao), 'um par')

    def test_par3(self):
        mao = ['2e', '2p', '3e', 'Qo', 'Kp']
        self.assertEqual(poker(mao), 'um par')

    def test_par4(self):
        mao = ['2e', '2o', '3e', 'Qo', 'Kp']
        self.assertEqual(poker(mao), 'um par')

    def test_par5(self):
        mao = ['3e', '3c', '2c', '7o', '6c']
        self.assertEqual(poker(mao), 'um par')

    def test_par6(self):
        mao = ['Ke', 'Kc', '2c', '7o', '6c']
        self.assertEqual(poker(mao), 'um par')

    def test_par7(self):
        mao = ['10e', '10c', '2c', '7o', '6c']
        self.assertEqual(poker(mao), 'um par')

    def test_doispares1(self):
        mao = ['10e', '10c', '2c', '2o', '6c']
        self.assertEqual(poker(mao), 'dois pares')

    def test_trinca(self):
        mao = ['10e', '10c', '10o', '2o', '6c']
        self.assertEqual(poker(mao), 'trinca')

    def test_quadra(self):
        mao = ['10e', '10c', '10o', '10p', '6c']
        self.assertEqual(poker(mao), 'quadra')

    def test_full_hand(self):
        mao = ['10e', '10c', '6o', '6p', '6c']
        self.assertEqual(poker(mao), 'full hand')

    def test_flush(self):
        mao = ['2e', '3e', '4e', '6e', '7e']
        self.assertEqual(poker(mao), 'flush')

    def test_royal1(self):
        mao = ['10e', 'Je', 'Qe', 'Ke', 'Ae']
        self.assertEqual(poker(mao), 'royal')

    def test_royal2(self):
        mao = ['10c', 'Jc', 'Qc', 'Kc', 'Ac']
        self.assertEqual(poker(mao), 'royal')

    def test_royal3(self):
        mao = ['Jc', '10c', 'Qc', 'Kc', 'Ac']
        self.assertEqual(poker(mao), 'royal')

    def test_sequencia(self):
        mao = ['9o', '10c', 'Jc', 'Qc', 'Kc']
        self.assertEqual(poker(mao), 'sequencia')

    def test_sequencia(self):
        mao = ['Ao', '2c', '3c', '4c', '5c']
        self.assertEqual(poker(mao), 'sequencia')
    
    def test_straight_flush(self):
        mao = ['Ac', '2c', '3c', '4c', '5c']
        self.assertEqual(poker(mao), 'straight flush')



if __name__ == '__main__':
    unittest.main()
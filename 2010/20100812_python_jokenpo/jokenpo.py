import unittest

PEDRA = 'pedra'
TESOURA = 'tesoura'
PAPEL = 'papel'
EMPATE = 'empate'

dicionario = {
    PEDRA: {
        TESOURA: PEDRA,
        PAPEL: PAPEL,
    },
    TESOURA: {
        PAPEL: TESOURA,
    },
}

def jokenpo(jogada_1, jogada_2):
    resultado = None
    if jogada_1 == jogada_2:
        return EMPATE
    try:
        resultado = dicionario[jogada_1][jogada_2]
    except KeyError:
        resultado = dicionario[jogada_2][jogada_1]
    return resultado

class TestJokenpo(unittest.TestCase):

    def test_PAPEL_com_PAPEL_retorna_EMPATE(self):
        self.assertEqual(jokenpo(PAPEL, PAPEL), EMPATE)

    def test_PAPEL_com_TESOURA_retorna_TESOURA(self):
        self.assertEqual(jokenpo(PAPEL, TESOURA), TESOURA)

    def test_TESOURA_com_TESOURA_retorna_EMPATE(self):
        self.assertEqual(jokenpo(TESOURA, TESOURA), EMPATE)

    def test_TESOURA_com_PEDRA_retorna_PEDRA(self):
        self.assertEqual(jokenpo(TESOURA, PEDRA), PEDRA)

    def test_PEDRA_com_TESOURA_retorna_PEDRA(self):
        self.assertEqual(jokenpo(PEDRA, TESOURA), PEDRA)

    def test_PEDRA_com_PAPEL_retorna_PAPEL(self):
        self.assertEqual(jokenpo(PEDRA, PAPEL), PAPEL)

    def test_PAPEL_com_PEDRA_retorna_PAPEL(self):
        self.assertEqual(jokenpo(PAPEL, PEDRA), PAPEL)




unittest.main()

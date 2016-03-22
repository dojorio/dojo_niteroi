import unittest
from poker import poker, Carta

class TestPoker(unittest.TestCase):

    def test_highcard_Ao_Ko_Qo_10o_9e(self):
    	cartas = [
    	    Carta('A', 'ouros'),
    	    Carta('K', 'ouros'), 
    	    Carta('Q', 'ouros'), 
    	    Carta('10', 'ouros'), 
    	    Carta('9', 'espadas'),
        ]
        self.assertEqual(poker(cartas), 'High Card')
        
    def test_pair_Ao_Ae_Qo_10o_9e(self):
    	cartas = [
    	    Carta('A', 'ouros'),    
    	    Carta('A', 'espadas'), 
    	    Carta('Q', 'ouros'), 
    	    Carta('10', 'ouros'), 
    	    Carta('9', 'espadas'),
        ]
        self.assertEqual(poker(cartas), 'Pair')
        
    def test_pair_Ao_Qe_Qo_10o_9e(self):
    	cartas = [
    	    Carta('A', 'ouros'),    
    	    Carta('Q', 'espadas'), 
    	    Carta('Q', 'ouros'), 
    	    Carta('10', 'ouros'), 
    	    Carta('9', 'espadas'),
        ]
        self.assertEqual(poker(cartas), 'Pair')
        
    def test_pair_Qe_Ao_Qo_10o_9e(self):
    	cartas = [
    	    Carta('Q', 'espadas'), 
    	    Carta('A', 'ouros'),    
    	    Carta('Q', 'ouros'), 
    	    Carta('10', 'ouros'), 
    	    Carta('9', 'espadas'),
        ]
        self.assertEqual(poker(cartas), 'Pair')
        
    def test_toak_Qe_Qo_Qp_10o_9e(self):
    	cartas = [
    	    Carta('Q', 'espadas'), 
    	    Carta('Q', 'ouros'),    
    	    Carta('Q', 'paus'), 
    	    Carta('10', 'ouros'), 
    	    Carta('9', 'espadas'),
        ]
        self.assertEqual(poker(cartas), 'Three of a Kind')
        
        
    def test_foak_Qe_Qo_Qp_Qc_9e(self):
    	cartas = [
    	    Carta('Q', 'espadas'), 
    	    Carta('Q', 'ouros'),    
    	    Carta('Q', 'paus'), 
    	    Carta('Q', 'copas'), 
    	    Carta('9', 'espadas'),
        ]
        self.assertEqual(poker(cartas), 'Four of a Kind')
    
    def test_full_house_Qe_Qo_Qp_9c_9e(self):
    	cartas = [
    	    Carta('Q', 'espadas'), 
    	    Carta('Q', 'ouros'),    
    	    Carta('Q', 'paus'), 
    	    Carta('9', 'copas'), 
    	    Carta('9', 'espadas'),
    	    
        ]
        self.assertEqual(poker(cartas), 'Full House')
        
        
    def test_flush_Qp_Jp_Kp_9p_8p(self):
    	cartas = [
    	    Carta('Q', 'paus'), 
    	    Carta('J', 'paus'),    
    	    Carta('K', 'paus'), 
    	    Carta('9', 'paus'), 
    	    Carta('8', 'paus'),
    	    
        ]
        self.assertEqual(poker(cartas), 'Flush')
        
    def test_high_card_Qo_Jo_Kp_9p_8p(self):
    	cartas = [
    	    Carta('Q', 'ouros'), 
    	    Carta('J', 'ouros'),    
    	    Carta('K', 'paus'), 
    	    Carta('9', 'paus'), 
    	    Carta('8', 'paus'),
    	    
        ]
        self.assertEqual(poker(cartas), 'High Card')
    
    
        
    def test_straight_5o_6o_7p_8p_9p(self):
    	cartas = [
    	    Carta('5', 'ouros'), 
    	    Carta('6', 'ouros'),    
    	    Carta('7', 'paus'), 
    	    Carta('8', 'paus'), 
    	    Carta('9', 'paus'),
    	    
        ]
        self.assertEqual(poker(cartas), 'Straight')
        
    def test_straight_6o_8o_7p_5p_9p(self):
    	cartas = [
    	    Carta('6', 'ouros'),    
    	    Carta('8', 'paus'), 
    	    Carta('7', 'paus'), 
    	    Carta('5', 'ouros'), 
    	    Carta('9', 'paus'),
    	    
        ]
        self.assertEqual(poker(cartas), 'Straight')

unittest.main()

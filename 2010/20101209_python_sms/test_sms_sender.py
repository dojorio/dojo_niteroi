import unittest2
from sms_sender import send

class TestSmsSender(unittest2.TestCase):

    def to_send(self, message, sequence):
        self.assertEqual(send(message), sequence)

    def test_for_a_type_2(self):
        self.to_send('a', '2')

    def test_for_b_type_22(self):
        self.to_send('b', '22')

    def test_for_c_type_222(self):
        self.to_send('c', '222')

    def test_for_d_type_3(self):
        self.to_send('d', '3')

    def test_for_e_type_33(self):
        self.to_send('e', '33')

    def test_for_f_type_333(self):
        self.to_send('f', '333')

    def test_for_space_type_0(self):
        self.to_send(' ', '0')

    def test_for_z_type_9999(self):
        self.to_send('z', '9999')

    def test_for_ab_type_2p22(self):
        self.to_send('ab', '2.22')

    def test_for_paralelepipedo_type_7p2p777p2p555p33p555p33p7pppp(self):
        self.to_send('paralelepipedo', '7.2.777.2.555.33.555.33.7.444.7.33.3.666')

    def test_for_A_type_star_2_star(self):
        self.to_send('A', '*2')

    def test_for_aA_type_star_2_star(self):
        self.to_send('aA', '2.*2')

unittest2.main()

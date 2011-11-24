import unittest2
from datetime import datetime

minutos_para_segundos = lambda x: x * 60
horas_para_segundos = lambda x: x * 3600

class DataTempo(datetime):

    def segundos_desde_1990(self):

        tempo = self.second
        tempo += minutos_para_segundos(self.minute)
        tempo += horas_para_segundos(self.hour)

        return tempo



class TestContaSegundos(unittest2.TestCase):

    def setUp(self):
        self.default_params = {
            'year': 1990,
            'month': 1,
            'day': 1,
            'hour': 0,
            'minute': 0,
            'second': 0,
        }

    def test_data_inicial(self):
        data = DataTempo(**self.default_params)
        self.assertEqual(data.segundos_desde_1990(), 0)

    def test_1_segundo_depois(self):
        self.default_params['second'] = 1
        data = DataTempo(**self.default_params)
        self.assertEqual(data.segundos_desde_1990(), 1)

    def test_2_segundos_depois(self):
        self.default_params['second'] = 2
        data = DataTempo(**self.default_params)
        self.assertEqual(data.segundos_desde_1990(), 2)

    def test_1_minuto_depois(self):
        self.default_params['minute'] = 1
        data = DataTempo(**self.default_params)
        self.assertEqual(data.segundos_desde_1990(), 60)

    def test_2_minutos_depois(self):
        self.default_params['minute'] = 2
        data = DataTempo(**self.default_params)
        self.assertEqual(data.segundos_desde_1990(), 120)

    def test_3_minutos_depois(self):
        self.default_params['minute'] = 3
        data = DataTempo(**self.default_params)
        self.assertEqual(data.segundos_desde_1990(), 180)

    def test_1_hora_depois(self):
        self.default_params['hour'] = 1
        data = DataTempo(**self.default_params)
        self.assertEqual(data.segundos_desde_1990(), 3600)

    def test_2_horas_depois(self):
        self.default_params['hour'] = 2
        data = DataTempo(**self.default_params)
        self.assertEqual(data.segundos_desde_1990(), 7200)

    def test_3_horas_depois(self):
        self.default_params['hour'] = 3
        data = DataTempo(**self.default_params)
        self.assertEqual(data.segundos_desde_1990(), 10800)

    def test_1_minuto_e_1_segundo_depois(self):
        self.default_params['minute'] = 1
        self.default_params['second'] = 1
        data = DataTempo(**self.default_params)
        self.assertEqual(data.segundos_desde_1990(), 61)

    def test_1_minuto_e_2_segundos_depois(self):
        self.default_params['minute'] = 1
        self.default_params['second'] = 2
        data = DataTempo(**self.default_params)
        self.assertEqual(data.segundos_desde_1990(), 62)

    def test_1_hora_1_minuto_e_1_segundo(self):
        self.default_params['hour'] = 1
        self.default_params['minute'] = 1
        self.default_params['second'] = 1
        data = DataTempo(**self.default_params)
        self.assertEqual(data.segundos_desde_1990(), 3661)

unittest2.main()

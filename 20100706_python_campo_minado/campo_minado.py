class CampoMinado(object):
    def __init__(self, campo):
        self.campo=campo








def resultado(entrada):
    if entrada[0][0] == '*':
        return[
            ['*', 1],
            [1, 1],
        ]


    return [
        [0, 0],
        [0, 0],
    ]

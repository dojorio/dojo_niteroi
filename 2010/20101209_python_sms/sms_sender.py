class NumPadDict(dict):

    def find_key(self, char):
        resposta = [k for k in self.keys() if char in k]

        if not resposta:
            raise KeyError

        return resposta[0]


num_pad = NumPadDict({
    "abc"  : '2',
    "def"  : '3',
    "ghi"  : '4',
    "jkl"  : '5',
    "mno"  : '6',
    "pqrs" : '7',
    "tuv"  : '8',
    "wxyz" : '9',
    " "    : '0',

})

def send(message):

    return ".".join([char_value(letra) for letra in message ])



def char_value(message):

    searchable_message = message.lower()
    key = num_pad.find_key(searchable_message)
    index = key.index(searchable_message)

    upper = ''
    if message.isupper():
        upper = '*'

    return upper + num_pad[key] * (index + 1)

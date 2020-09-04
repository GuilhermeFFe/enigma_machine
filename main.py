from enigma import Machine

def run_word(word: str, machine: Machine) -> str:
    encrypted = ''
    for c in word:
        encrypted += machine.type(c)
    return encrypted

def type_msg(original):
    machine1 = Machine()
    machine2 = Machine()

    unencrypted = original.split()
    print(original)

    encrypted = ''
    decrypted = ''

    for word in unencrypted:
        _encrypted = run_word(word, machine1)
        encrypted += _encrypted + ' '
        _decrypted = run_word(_encrypted, machine2)
        decrypted += _decrypted + ' '
    
    print(encrypted)
    print(decrypted)

type_msg('BATATINHA QUANDO NASCE ESPALHA RAMA PELO CHAO')
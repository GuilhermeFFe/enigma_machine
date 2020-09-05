from enigma import Machine

def type_msg(original):
    machine1 = Machine()
    machine2 = Machine()

    machine1.add_plug('A', 'B')
    machine1.increment_rotor(150)
    machine2.add_plug('A', 'B')
    machine2.increment_rotor(150)

    unencrypted = original.split()
    print(original)

    encrypted = ''
    decrypted = ''

    for word in unencrypted:
        _encrypted = machine1.type_word(word)
        encrypted += _encrypted + ' '
        _decrypted = machine2.type_word(_encrypted)
        decrypted += _decrypted + ' '
    
    print(encrypted)
    print(decrypted)

type_msg('BATATA')
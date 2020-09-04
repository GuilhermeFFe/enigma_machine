from enigma import Machine

if __name__ == '__main__':
    machine1 = Machine()
    machine2 = Machine()

    original = 'BATATA'
    encrypted = machine1.type(original)
    decrypted = machine2.type(encrypted)

    print(original)
    print(encrypted)
    print(decrypted)
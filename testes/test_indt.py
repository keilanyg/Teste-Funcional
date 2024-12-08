import re

def verificar_string(string):
    if re.match(r'^[A-Za-z][a-zA-Z0-9]{0,5}$', string) is None:
        return False
    return True

def test_string1():
    teste = "a1@"
    assert verificar_string(teste) == False

def test_string2():
    teste = "1abcde"
    assert verificar_string(teste) == False

def test_string3():
    teste = "a1b2"
    assert verificar_string(teste) == True

def test_string4():
    teste = "@abcd1"
    assert verificar_string(teste) == False
    
def test_string5():
    teste = "ab c"
    assert verificar_string(teste) == False

def test_string6():
    teste = "abcdef"
    assert verificar_string(teste) == True

def test_string7():
    teste = "abc123@"
    assert verificar_string(teste) == False
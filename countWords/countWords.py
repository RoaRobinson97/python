import re, string

text = """ Python es un lenguaje de programación interpretado cuya filosofía hace hincapié en la legibilidad de su código.2​ Se trata de un lenguaje de programación multiparadigma, ya que soporta orientación a objetos, programación imperativa y, en menor medida, programación funcional. Es un lenguaje interpretado, dinámico y multiplataforma.
Es administrado por la Python Software Foundation. Posee una licencia de código abierto, denominada Python Software Foundation License"""

def normalize(val):
    regex = re.compile('[%s]' % re.escape(string.punctuation))
    return regex.sub('', val).lower()

def countWords( texto ):
    myDict = {};
    separateWords = texto.split()
    for val in separateWords:
        if (normalize(val) in myDict):
            myDict[normalize(val)] = myDict[normalize(val)] + 1
        else:
            myDict[normalize(val)] = 1
    print(myDict)

countWords(text)

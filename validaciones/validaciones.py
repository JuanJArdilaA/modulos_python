##Validarnombre
def validar_nombre(nombre):
    if len(nombre) > 0:
        return True
    else:
        return False

def validar_edad(edad):
    if edad>=15 and edad<=117:
        return True
    else:
        return False
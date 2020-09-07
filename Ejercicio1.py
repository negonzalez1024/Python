def calcularedad(edadactual,anactual):
  if edadactual>0:
    if anactual>0:
      edad1=2070
      edad2=edad1-anactual
      edadfinal=edadactual+edad2
      return edadfinal
    else:
      print("El año actual ingresado es mayor 2070")
  else: 
     print("Error los numeros deben ser mayores a 0")
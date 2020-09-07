def calcularpalabra(palabra):
  print("El tamaño de la palabra  es: ", len(palabra))
  primer_caracter = palabra[0]
  print("El primer caracter es: ", primer_caracter)
  ultimo_caracter=palabra[len(palabra)-1]
  print("El ultimo caracter es: ", ultimo_caracter)
  return primer_caracter, ultimo_caracter
import unittest
import Ejercicio3


class TestEjercicio3(unittest.TestCase):

	def testcalcularedad(self):
		self.assertEqual(Ejercicio3.calcularpalabra("Jose"),("J","e"))
		

if __name__== "__main__":
	unittest.main()
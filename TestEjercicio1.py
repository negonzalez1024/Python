import unittest
import Ejercicio1


class TestEdad(unittest.TestCase):

	def testcalcularedad(self):
		self.assertEqual(Ejercicio1.calcularedad(20,2020),70)
		self.assertEqual(Ejercicio1.calcularedad(10,2010),70)

if __name__== "__main__":
	unittest.main()
import unittest
import Ejercicio2


class TestEdad(unittest.TestCase):

	def testcalcularedad(self):
		self.assertEqual(Ejercicio2.calcularnumero(20),True)
		self.assertEqual(Ejercicio2.calcularnumero(5),False)

if __name__== "__main__":
	unittest.main()
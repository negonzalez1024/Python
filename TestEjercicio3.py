import unittest
import palabra


class TestEdad(unittest.TestCase):

	def testcalcularedad(self):
		self.assertEqual(palabra.calcularpalabra("Jose"),("J","e"))
		

if __name__== "__main__":
	unittest.main()
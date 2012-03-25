import unittest

from ocr_reader import *

class OcrReaderTest(unittest.TestCase):
  def test_deve_reconhecer_numero_um(self):
    numero_um_em_texto =  "   " + \
                          "  |" + \
                          "  |" + \
                          "   "

    self.assertEqual( 1, parse(numero_um_em_texto) )

  def test_deve_reconhecer_numero_dois(self):
    numero_dois_em_texto =  " _ " + \
                            " _|" + \
                            "|_ " + \
                            "   "
    self.assertEqual( 2, parse(numero_dois_em_texto) )

  def test_deve_reconhecer_numero_tres(self):
    numero_tres_em_texto =  " _ " + \
                            " _|" + \
                            " _|" + \
                            "   "
    self.assertEqual( 3, parse(numero_tres_em_texto) )

if __name__ == '__main__':
  unittest.main()

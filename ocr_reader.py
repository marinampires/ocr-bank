def parse(numero_em_texto):
  mapa_texto_para_numero = {
      numero_um(): 1,
      numero_dois(): 2,
      numero_tres(): 3
    }

  return mapa_texto_para_numero[numero_em_texto]

def numero_um():
  return  "   " + \
          "  |" + \
          "  |" + \
          "   "

def numero_dois():
  return " _ " + \
         " _|" + \
         "|_ " + \
         "   "

def numero_tres():
  return " _ " + \
         " _|" + \
         " _|" + \
         "   "

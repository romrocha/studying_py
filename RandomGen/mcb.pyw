#! Python 3

# mcb.pyw - Salva e carrega porções de texto no clipboard.

# Usage: mcb.pyw save <palavra-chave> - Salva clipboard na palavra-chave.
#        mcb.pyw <palavra-chave> - Carrega palavra chave no clipboard.
#        mcb.pyw list - Carrega todas as palavras-chave no clipboard.

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

#Salva conteúdo no clipboard.
if len(sys.argv) == 3 and sys.argv[1] == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
    #Lista palavras chave e carrega conteúdo.
    if sys.argv[1].lower() == 'list':
      print(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
      pyperclip.copy(mcbShelf[sys.argv[1]])

mcbShelf.close()
    


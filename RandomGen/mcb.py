#! Python 3

# mcb.py - Salva e carrega porções de texto no clipboard.


import shelve, pyperclip, sys, argparse


def pasting_clip(clipboardname):
    #Salva conteúdo no clipboard.
    mcbShelf[clipboardname] = pyperclip.paste()
    mcbShelf.close()
   
def delete_clip_content(clipboardname):
    #Deleta conteúdo no clipboard. 
    print('deleting' + clipboardname)
    del mcbShelf[clipboardname]
    mcbShelf.close()

def list_content():
    #Lista palavras chave e carrega conteúdo.
    print('listing all...')
    print(str(list(mcbShelf.keys())))
    mcbShelf.close()

def delete_all():
    print('deleting all...')
    mcbShelf.clear()
    mcbShelf.close()

def reading_clip(clip_content):
    print('loading')
    pyperclip.copy(mcbShelf[clip_content])
    mcbShelf.close()

def cli_arguments():
    my_parser = argparse.ArgumentParser(prog='mcb', description='Multiboard clipper v1 by r0m')
    my_parser.version = '1.0'
    my_parser.add_argument('-l', metavar='clipboardname', help='Carrega informações da palavra chave no seu clipboard. Exemplo: python mcb.py -l <palavrachave>')
    my_parser.add_argument('-s', metavar="clipboardname", help='Salve informações do seu clipboard em uma palavra chave. Exemplo: python mcb.py -s <palavrachave>')
    my_parser.add_argument('-delete', metavar="clipboardname", help='Deleta o conteúdo de uma palavra chave')
    my_parser.add_argument('-ls', action='store_true', help='Lista todas as palavras chave salvas')
    my_parser.add_argument('-deleteall', action='store_true', help='Deleta todas as palavras chaves salvas')
    user_raw_input = my_parser.parse_args()
    return user_raw_input

def main():
    user_raw_input = cli_arguments()
    print(vars(user_raw_input))
    global mcbShelf
    mcbShelf = shelve.open('mcb')
            
       
    print('hello main')
    if user_raw_input.l is not None:
            reading_clip(user_raw_input.l)
    elif user_raw_input.s is not None:
            pasting_clip(user_raw_input.s)
    elif user_raw_input.ls is True:
            list_content()
    elif user_raw_input.delete is not None:
            delete_clip_content(user_raw_input.delete)
    elif user_raw_input.deleteall is True:
            delete_all()      
    else:
        sys.exit('error')        
    

    
   

if __name__ == "__main__":
    main()



    


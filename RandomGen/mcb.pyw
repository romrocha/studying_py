#! Python 3

# mcb.pyw - Salva e carrega porções de texto no clipboard.

# Usage: mcb.pyw save <palavra-chave> - Salva clipboard na palavra-chave.
#        mcb.pyw delete <palavra-chave> - Deleta clipboard na palavra-chave.
#        mcb.pyw <palavra-chave> - Carrega palavra chave no clipboard.
#        mcb.pyw list - Carrega todas as palavras-chave no clipboard.
#        mcb.pyw deleteall - Apaga todas as palavras-chave no clipboard.


import shelve, pyperclip, sys, argparse


def pasting_clip(clipboardname):
 #Salva conteúdo no clipboard.
 #if len(sys.argv) == 3 and sys.argv[1] == 'save': 
 mcbShelf[sys.argv[2]] = pyperclip.paste()
   
def delete_clip_content(clipboardname):
 #Deleta conteúdo no clipboard. 
 #elif len(sys.argv) == 3 and sys.argv[1] == 'delete':
 del mcbShelf[sys.argv[2]]

#elif len(sys.argv) == 2:
def list_content():
 #Lista palavras chave e carrega conteúdo.
 #if sys.argv[1].lower() == 'list':
 print(str(list(mcbShelf.keys())))

def delete_all():
 #elif sys.argv[1].lower() == 'deleteall'
 print(deleting)
 del mcbShelf.clear

def reading_clip(clip_content):
 #sys.argv[1] in mcbShelf:
 pyperclip.copy(mcbShelf[clip_content])

def cli_arguments():
    parse_arg = argparse.ArgumentParser(prog='mcb', description='Multiboard clipper v1')
    parse_arg.add_argument('Nome do clipboard', action='store_true', type=str, help='Defina o nome para seu clipboard')
    parse_arg.add_argument('-save', metavar="clipboardname", type=str, help='Insira o nome de um identificador para seu clip board. Exemplo: python mcb.py -save <nome>')
    parse_arg.add_argument('-delete', metavar="clipboardname", type=str, help='Insira o nome do clipboard que deseja deletar')
    parse_arg.add_argument('-list', action='store_true', help='Lista todos os clipboards salvos')
    parse_arg.add_argument('-deleteall', action='store_true', help='Deleta todos os clipboards salvos')
    user_raw_input = parse_arg.parse_args()
    return user_raw_input

def main():
    user_raw_input = cli_arguments()
    
    if user_raw_input is not None:
        mcbShelf = shelve.open('mcb')
        print(user_raw_input)




        mcbShelf.close()

        


    else:
        sys.exit('Erro, insira algum argumento para continuar, ou -h para ver as opções disponivéis')

if __name__ == "__main__":
    main()



    


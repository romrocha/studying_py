#! python3
# regex catador - encontra número de telefones e e-mail no clipboard.

import pyperclip, re

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?               #codigo de area
    (\s|-|\.)?                       #separador
    (\d{3})                          # primeiros 3 digitos
    (\s|-|\.)?                       #separador
    (\d{4})                          #últimos 4 digitos)
    (\s*(ext|x|ext.)\s*(\d{2,5}))?   #extensão

)''', re.VERBOSE)

# TODO : Cria regex para pegar o e-mail

# TODO: Encontra correspondências no texto do clipboard

# TODO: Copia os resultados para o clipboard

"""exemplo de modulos, que exporta funções de outro ficheiro 
e também permite importar """

import modulos
from datetime import date

hoje = date(2026, 9, 17)   # date.today() dá a data atual
print("Fatura de", hoje.strftime("%d/%m/%Y"))
print("Total:", modulos.euros(modulos.preco_com_iva(40)))

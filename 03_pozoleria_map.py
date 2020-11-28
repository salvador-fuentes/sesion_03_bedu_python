## ¿Cómo usar la función map de python...

IVA = 0.16

def aplicar_iva(precio):
    resultado = precio * (1 + IVA)
    return round(resultado, 2)


precios_en_menu = [415, 90, 355, 385, 115, 100, 250, 660]
print(precios_en_menu)

# La función map ayuda a aplicar una función a cada elemento de mi lista. 
precios_con_iva = list(map(aplicar_iva , precios_en_menu))
print(precios_con_iva)

#Añadiendo el IVA a unos precios de menú

IVA = 0.16

precios_en_menu = [1975, 1825, 275, 1500, 850, 675, 1175, 1600, 2175, 2175, 625, 1150, 1175, 350, 1125, 1250, 1875, 1275, 825, 1575, 300, 1275, 875, 1650, 875]

for precio in precios_en_menu:
    resultado = precio * (1+ IVA)
    resultado = round(resultado, 2)
    resultado_impreso = f'${precio} con IVA incluido: $ {resultado}'
    print(resultado_impreso)




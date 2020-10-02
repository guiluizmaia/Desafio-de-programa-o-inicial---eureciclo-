gal = float(input("Litros do Galão: "))
quant = int(input("Quantidade de garrafas: "))
garrafas = []
resposta = ""

for q in range(1, quant+1):
    cont = float(input(f"Litros da garrafa %i : " %q))    
    garrafas.append(cont)

garrafas.sort(reverse=True)

for garrafa in garrafas:
    if gal-garrafa >=0:
        gal = gal-garrafa
        resposta = resposta + f"%.2fL, " %garrafa

print (f"Usamos as garrafas de: %s" %resposta)
print (f"Sobrou: %.2fL" %gal)
print("Bem-vindo, informe seus dados abaixos")
basic = 30
silver = 20
gold = 10
platinum = 5
assinatura = input("Insira seu tipo de assinatura:")
faturamento_anual: int = int(input("Insira o seu faturamento anual:"))
if assinatura == "basic":
   porcentagem = (faturamento_anual * basic) / 100
   print("valor bonus a ser pago é {}".format(porcentagem))
elif assinatura == "silver":
   porcentagem = (faturamento_anual * silver) / 100
   print("valor bonus a ser pago é {}".format(porcentagem))
if assinatura == "gold":
   porcentagem = (faturamento_anual * gold) / 100
   print("valor bonus a ser pago é {}".format(porcentagem))
elif assinatura == "platinum":
   porcentagem = (faturamento_anual * platinum) / 100
   print("valor bonus a ser pago é {}".format(porcentagem))






































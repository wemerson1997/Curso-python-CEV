sexo = input("Digite seu sexo (M ou F): ").strip().upper()[0]

while sexo not in ["M", "F"]:
  print("Sexo inválido. Digite novamente.")
  sexo = input("Digite seu sexo (M ou F): ")

print("Seu sexo é:", sexo)

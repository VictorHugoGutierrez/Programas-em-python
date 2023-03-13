import os

equipamentos = []
valores = []
seriais = []
departamentos = []

#Cadastro de Itens
def cadastrarItens(resposta):
  os.system("cls")
  while resposta == "SIM":
    equipamentos.append(input("Equipamento: "))
    valores.append(float(input("Valor: ")))
    seriais.append(int(input("Número Serial: ")))
    departamentos.append(input("Departamento: "))
    resposta = input("\nDigite 'SIM' para continuar, caso não queira digite 'NÃO': ").upper()
    os.system("cls")
  listarItens(equipamentos)

#Busca de Itens
def buscarItens(equipamentos):
  equipamentos = equipamentos
  busca = input("\nDigite o nome do equipamento que deseja buscar: ")
  for indice in range(0,len(equipamentos)):
    if busca==equipamentos[indice]:
      print("Valor........: ", valores[indice])
      print("Serial.......: ", seriais[indice])
      print("Departamento.: ", departamentos[indice])

#Mudança de Valor de Itens
def mudarValor(equipamentos):
  valor=input("Digite o nome do equipamento que será alterado o valor: ")
  for indice in range(0,len(equipamentos)):
    if valor==equipamentos[indice]:
      print("Valor antigo: ", valores[indice])
      valores[indice] = input("Digite um novo valor: ")
      print("Novo valor: ", valores[indice])
  listarItens(equipamentos)

#Mudança de Nome dos Itens
def mudarNome(equipamentos):
  valor = input("Digite o nome do equipamento que será alterado o nome: ")
  for indice in range(0,len(equipamentos)):
    if valor == equipamentos[indice]:
      print("Nome antigo: ", equipamentos[indice])
      equipamentos[indice] = input("Digite um novo nome: ")
      print("Novo nome: ", equipamentos[indice])
  listarItens(equipamentos)

#Mudança de Serial
def mudarSerial(equipamentos):
  valor = input("Digite o nome do equipamento que será alterado o serial: ")
  for indice in range(0,len(equipamentos)):
    if valor == equipamentos[indice]:
      print("Serial antigo: ", seriais[indice])
      seriais[indice] = input("Digite um novo serial: ")
      print("Novo Serial: ", seriais[indice])
  listarItens(equipamentos)

#Mudança de Departamento
def mudarDepartamento(equipamentos):
  valor = input("Digite o nome do equipamento que será alterado o departamento: ")
  for indice in range(0,len(equipamentos)):
    if valor == equipamentos[indice]:
      print("Departamento antigo: ", departamentos[indice])
      departamentos[indice] = input("Digite um novo Departamento: ")
      print("Novo Departamento: ", departamentos[indice])
  listarItens(equipamentos)

#Excluir Itens
def excluirItens(serial):
  serial = serial
  serial = int(input("Digite o serial do equipamento que será excluido: "))
  for indice in range(0, len(departamentos)):
    if seriais[indice]==serial:
      del departamentos[indice]
      del equipamentos[indice]
      del seriais[indice]
      del valores[indice]
      break
  listarItens(equipamentos)

#Listar os Itens
def listarItens(equipamentos):
  os.system("cls")
  for indice in range(0,len(equipamentos)):
    print("\nEquipamento..: ", (indice+1))
    print("Nome.........: ", equipamentos[indice])
    print("Valor........: ", valores[indice])
    print("Serial.......: ", seriais[indice])
    print("Departamento.: ", departamentos[indice])

#Função Principal (menu)
def main():
  os.system("cls")
  while True:
    print("\nMenu de Opções:")
    print("(1) Cadastrar Itens")
    print("(2) Buscar Itens")
    print("(3) Editar Itens")
    print("(4) Excluir Item")
    print("(5) Listar Itens")
    print("(0) Sair.")

    entrada = int(input("Digite a opção desejada: "))
    if entrada == 1:
        resposta = "SIM"
        cadastrarItens(resposta)
        input("\nPressione Enter para continuar...")
        os.system("cls")

    elif entrada == 2:
      buscarItens(equipamentos)
      input("\nPressione Enter para continuar...")
      os.system("cls")

    elif entrada == 3:
      while True: 
        os.system("cls")
        print("\nOpções:")
        print("(1) Mudar Nome")
        print("(2) Mudar Valor")
        print("(3) Mudar Serial")
        print("(4) Mudar Departamento")
        print("(0) Sair")
        opçao = int(input("Digite a opção desejada: "))

        if opçao == 1:
          os.system("cls")
          mudarNome(equipamentos)
          input("\nPressione Enter para continuar...")
          os.system("cls")

        elif opçao == 2:
          os.system("cls")
          mudarValor(equipamentos)
          input("\nPressione Enter para continuar...")
          os.system("cls")

        elif opçao == 3:
          os.system("cls")
          mudarSerial(equipamentos)
          input("\nPressione Enter para continuar...")
          os.system("cls")

        elif opçao == 4:
          os.system("cls")
          mudarDepartamento(equipamentos)
          input("\nPressione Enter para continuar...")
          os.system("cls")

        elif opçao == 0:
          os.system("cls")
          break

    elif entrada == 4:
      os.system("cls")
      excluirItens(equipamentos)
      input("\nPressione Enter para continuar...")
      os.system("cls")

    elif entrada == 5:
      listarItens(equipamentos)
      input("\nPressione Enter para continuar...")
      os.system("cls")

    elif entrada == 0:
      os.system("cls")
      break

    else:
      print("Opção Invalida")
      main()

main()
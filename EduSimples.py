# Estrutura do código (Sugestão)

lista_alunos = []

def cadastrar():
  print("--------- Cadastro de Alunos ---------\n")

  nome = input("Digite o nome do aluno: ")
  matricula = input("Digite a matricula do aluno: ")
  while True:
    try:
        primeira_nota = float(input("Digite a nota da primeira unidade: "))
        segunda_nota = float(input("Digite a nota da segunda unidade: "))
        break
    except ValueError:
        print("O valor da nota tem que ser um numero")  
  media = (primeira_nota + segunda_nota) / 2
  situacao = None
  if media >= 7:
    situacao = "Aprovado"
  elif media >= 5:
    situacao = "Recuperação"
  else:
    situacao = "Reprovado"

  aluno = {"nome": nome, "matricula": matricula, "primeira_nota": primeira_nota, "segunda_nota": segunda_nota, "media": media, "situacao": situacao}
  lista_alunos.append(aluno)
  print(f'Nome: {aluno["nome"]} - Matricula: {aluno["matricula"]} - Media: {aluno["media"]:.2f} - Situacao: {aluno["situacao"]}\n')


def alterar():
  print("--------- Atualizar Aluno ---------\n")

  matricula_atualizacao = input("Digite a matricula do aluno que deseja atualizar: ")

  for aluno in lista_alunos:
    if aluno["matricula"] == matricula_atualizacao:
      escola_atualizacao = input(f'O que deseja alterar do aluno {aluno["nome"]}, 1 - nome, 2 - matricula, 3 - Primeira nota, 4 - Segunda nota\n')
    match escola_atualizacao:
        case "1":
            novo_nome = input("Qual nome deseja colocar: ")
            aluno["nome"] = novo_nome
        case "2":
            nova_matricula = input("Qual matricula deseja colocar: ")
            aluno["matricula"] = nova_matricula
        case "3":
          aluno["primeira_nota"] = float(input("Qual a nova nota da primeira unidade: "))
        case "4":
          aluno["segunda_nota"] = float(input("Qual a nova nota da segunda unidade: "))
        case _:
          print("Esse numero nao existe")

    aluno["media"] = (aluno["primeira_nota"] + aluno["segunda_nota"]) / 2

    if aluno["media"] >= 7:
      aluno["situacao"] = "Aprovado"
    elif aluno["media"] >= 5:
      aluno["situacao"] = "Recuperacao"
    else:
      aluno["situacao"] = "Reprovado"
    
    print(f'Nome: {aluno["nome"]} - Matricula: {aluno["matricula"]} - Media: {aluno["media"]:.2f} - Situacao: {aluno["situacao"]}\n')
      

def excluir():
  print("--------- Excluir Aluno ---------\n")
  matricula_exclusao = input("Digite o numero da matricula do aluno que deseja excluir: ")
  
  for aluno in lista_alunos:
    if aluno["matricula"] == matricula_exclusao:
      lista_alunos.remove(aluno)
      print(f'Aluno {aluno["nome"]} removido com sucesso\n')
    else:
      print("Essa matricula não existe, tente novamente\n")
      

def listar():
  print("--------- Lista dos Alunos ---------\n")

  if not lista_alunos:
    print("Nenhum aluno cadastrado\n")
    return

  
  for aluno in lista_alunos:
    print(f'Nome: {aluno["nome"]} - Matricula: {aluno["matricula"]} - Media: {aluno["media"]:.2f} - Situacao: {aluno["situacao"]}\n')


while True:
  print("--------- Bem-vindo ao EduSimples ---------\n")
  opcao = int(input('Digite: 1 - Cadastrar, 2 - Alterar, 3 - Excluir, 4 - Listar, 5 - Sair do Sistema: '))

  if opcao == 1:
    cadastrar()
  elif opcao == 2:
    alterar()
  elif opcao == 3:
    excluir()
  elif opcao == 4:
    listar()
  elif opcao == 5:
    break
  else:
    print('Erro\n')

print('Sistema finalizado com sucesso!!!!')
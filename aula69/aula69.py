lista = []
lista_desfazer = []


def adicionar(item):
    lista.append(item)


def desfazer():
    try:
        lista_desfazer.append(lista.pop())
    except IndexError:
        print('Nada a desfazer')


def refazer():
    try:
        lista.append(lista_desfazer.pop(-1))
    except IndexError:
        print('Nada a refazer')


while True:
    print('Lista de tarefas\n'
          '1 - Adicionar tarefa\n'
          '2 - Listar tarefas\n'
          '3 - Opção de desfazer\n'
          '4 - Opção de refazer\n'
          '5 - Sair')
    try:
        opcao = int(input('Digite o número da opção: '))
        if opcao <= 5:
            if opcao == 1:
                tarefa = input('Tarefa a adicionar: ')
                adicionar(tarefa)
            elif opcao == 2:
                print(lista)
            elif opcao == 3:
                desfazer()
            elif opcao == 4:
                refazer()
            elif opcao == 5:
                print('Saindo')
                break
        else:
            print('Opção inválida.')
    except ValueError:
        print('Apenas o número da opção.')


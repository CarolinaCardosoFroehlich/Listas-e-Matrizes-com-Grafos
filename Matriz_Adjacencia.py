def criar_grafo():
  matriz = []
  vertices = []
  return matriz, vertices


def inserir_vertice(matriz, vertices, vertice):
  if vertice not in vertices:
    vertices.append(vertice)
    for linha in matriz:
      linha.append(0)
    nova_linha = [0] * len(vertices)
    matriz.append(nova_linha)


def inserir_aresta(matriz, vertices, origem, destino, nao_direcionado=False):
  inserir_vertice(matriz, vertices, origem)
  inserir_vertice(matriz, vertices, destino)

  i = vertices.index(origem)
  j = vertices.index(destino)

  matriz[i][j] = 1
  if nao_direcionado:
    matriz[j][i] = 1


def remover_vertice(matriz, vertices, vertice):
  if vertice not in vertices:
    print(f"O vértice '{vertice}' não existe no grafo.")
    return

  idx = vertices.index(vertice)
  matriz.pop(idx)
  for linha in matriz:
    linha.pop(idx)
  vertices.pop(idx)
  print(f"Vértice '{vertice}' removido com sucesso.")


def remover_aresta(matriz, vertices, origem, destino, nao_direcionado=False):
  if origem in vertices and destino in vertices:
    i = vertices.index(origem)
    j = vertices.index(destino)
    matriz[i][j] = 0
    if nao_direcionado:
      matriz[j][i] = 0


def existe_aresta(matriz, vertices, origem, destino):
  if origem in vertices and destino in vertices:
    i = vertices.index(origem)
    j = vertices.index(destino)
    return matriz[i][j] == 1
  return False


def vizinhos(matriz, vertices, vertice):
  if vertice not in vertices:
    return []

  i = vertices.index(vertice)
  lista_vizinhos = []
  for j, val in enumerate(matriz[i]):
    if val == 1:
      lista_vizinhos.append(vertices[j])
  return lista_vizinhos


def grau_vertices(matriz, vertices):
  graus = {}
  n = len(vertices)

  for i in range(n):
    vertice = vertices[i]
    saida = sum(matriz[i])
    entrada = sum(matriz[j][i] for j in range(n))
    total = saida + entrada
    graus[vertice] = {"saida": saida, "entrada": entrada, "total": total}

  return graus


def percurso_valido(matriz, vertices, caminho):
  if not caminho or len(caminho) < 2:
    return True

  for i in range(len(caminho) - 1):
    u = caminho[i]
    v = caminho[i + 1]
    if not existe_aresta(matriz, vertices, u, v):
      return False
  return True


def listar_vizinhos(matriz, vertices, vertice):
  if vertice in vertices:
    lista = vizinhos(matriz, vertices, vertice)
    print(f"Vizinhos de '{vertice}': {lista}")
    return lista
  else:
    print(f"O vértice '{vertice}' não existe no grafo.")
    return []


def exibir_grafo(matriz, vertices):
  print("\n--- Matriz de Adjacência ---")
  if not vertices:
    print("O grafo está vazio.")
    return

  cabecalho = "      " + " ".join(f"{v:3}" for v in vertices)
  print(cabecalho)
  print("    " + "-" * (len(vertices) * 4 + 2))

  for i, vertice in enumerate(vertices):
    linha_str = f"{vertice:3} | " + " ".join(f"{val:3}" for val in matriz[i])
    print(linha_str)
  print("-" * 40)


def main():
  matriz, vertices = criar_grafo()
  nao_direcionado = True

  while True:
    print("1 - Exibir o Grafo")
    print("2 - Inserir Vértice")
    print("3 - Inserir Aresta")
    print("4 - Remover Vértice")
    print("5 - Remover Aresta")
    print("6 - Listar Vizinhos de um Vértice")
    print("7 - Verificar se Aresta Existe")
    print("8 - Calcular Graus dos Vértices")
    print("9 - Verificar Percurso Válido")
    print("0 - Sair")

    opcao = input("\nEscolha uma opção: ").strip()

    if opcao == "1":
      exibir_grafo(matriz, vertices)

    elif opcao == "2":
      v = input("Digite o nome do vértice a inserir: ").strip()
      inserir_vertice(matriz, vertices, v)
      print(f"Vértice '{v}' inserido (se já não existia).")

    elif opcao == "3":
      origem = input("Digite o vértice de origem: ").strip()
      destino = input("Digite o vértice de destino: ").strip()
      inserir_aresta(matriz, vertices, origem, destino, nao_direcionado)
      print(f"Aresta entre '{origem}' e '{destino}' inserida.")

    elif opcao == "4":
      v = input("Digite o vértice que deseja remover: ").strip()
      remover_vertice(matriz, vertices, v)

    elif opcao == "5":
      origem = input("Digite o vértice de origem da aresta: ").strip()
      destino = input("Digite o vértice de destino da aresta: ").strip()
      remover_aresta(matriz, vertices, origem, destino, nao_direcionado)
      print(f"Aresta entre '{origem}' e '{destino}' removida.")

    elif opcao == "6":
      v = input("Digite o vértice para ver os vizinhos: ").strip()
      listar_vizinhos(matriz, vertices, v)

    elif opcao == "7":
      origem = input("Vértice de origem: ").strip()
      destino = input("Vértice de destino: ").strip()
      existe = existe_aresta(matriz, vertices, origem, destino)
      if existe:
        print(f"-> SIM! Existe uma aresta de '{origem}' para '{destino}'.")
      else:
        print(f"-> NÃO existe aresta direta de '{origem}' para '{destino}'.")

    elif opcao == "8":
      graus = grau_vertices(matriz, vertices)
      print("\n--- Graus dos Vértices ---")
      for v, info in graus.items():
        print(
            f"Vértice '{v}': Entrada = {info['entrada']} | Saída ="
            f" {info['saida']} | Total = {info['total']}"
        )

    elif opcao == "9":
      entrada_caminho = input(
          "Digite o percurso separado por vírgulas (ex: A,B,C,D): "
      ).strip()
      if entrada_caminho:
        caminho = [n.strip() for n in entrada_caminho.split(",")]
        valido = percurso_valido(matriz, vertices, caminho)
        if valido:
          print(
              f"-> O percurso {' -> '.join(caminho)} é valido"
          )
        else:
          print(
              f"-> O percurso {' -> '.join(caminho)} é invalido!"
          )
      else:
        print("Caminho vazio.")

    elif opcao == "0":
      print("Saindo do programa. Bons estudos!")
      break
    else:
      print("Opção inválida! Tente novamente.")

    if opcao != "0":
      input("\nPressione ENTER para voltar ao menu...")


if __name__ == "__main__":
  main()

def criar_grafo():
  vertices = []
  arestas = []
  return vertices, arestas


def inserir_vertice(vertices, arestas, vertice):
  if vertice not in vertices:
    vertices.append(vertice)


def inserir_aresta(vertices, arestas, origem, destino, nao_direcionado=False):
  inserir_vertice(vertices, arestas, origem)
  inserir_vertice(vertices, arestas, destino)

  if nao_direcionado:
    # Evita duplicatas invertidas em grafos não direcionados
    if (origem, destino) not in arestas and (destino, origem) not in arestas:
      arestas.append((origem, destino))
  else:
    if (origem, destino) not in arestas:
      arestas.append((origem, destino))

def remover_vertice(vertices, arestas, vertice, nao_direcionado=True):
  """Remove um vértice e todas as arestas conectadas a ele."""
  if vertice not in vertices:
    print(f"O vértice '{vertice}' não existe no grafo.")
    return

  arestas[:] = [(u, v) for u, v in arestas if u != vertice and v != vertice]
  vertices.remove(vertice)
  print(f"Vértice '{vertice}' removido com sucesso.")


def remover_aresta(vertices, arestas, origem, destino, nao_direcionado=False):
  if nao_direcionado:
    if (origem, destino) in arestas:
      arestas.remove((origem, destino))
    elif (destino, origem) in arestas:
      arestas.remove((destino, origem))
  else:
    if (origem, destino) in arestas:
      arestas.remove((origem, destino))


def existe_aresta(vertices, arestas, origem, destino, nao_direcionado=False):
  if nao_direcionado:
    return (origem, destino) in arestas or (destino, origem) in arestas
  else:
    return (origem, destino) in arestas


def vizinhos(vertices, arestas, vertice, nao_direcionado=True):
  if vertice not in vertices:
    return []

  lista_vizinhos = []
  for u, v in arestas:
    if u == vertice:
      lista_vizinhos.append(v)
    elif nao_direcionado and v == vertice:
      lista_vizinhos.append(u)
  return lista_vizinhos


def grau_vertices(vertices, arestas, nao_direcionado=True):
  graus = {}
  for v in vertices:
    graus[v] = {"saida": 0, "entrada": 0, "total": 0}

  for u, v in arestas:
    if nao_direcionado:
      if u in graus:
        graus[u]["saida"] += 1
        graus[u]["total"] += 1
      if v in graus:
        graus[v]["saida"] += 1
        graus[v]["total"] += 1
    else:
      if u in graus:
        graus[u]["saida"] += 1
        graus[u]["total"] += 1
      if v in graus:
        graus[v]["entrada"] += 1
        graus[v]["total"] += 1
  return graus


def percurso_valido(vertices, arestas, caminho, nao_direcionado=True):
  """Verifica se um percurso (sequência de vértices) é válido."""
  if not caminho or len(caminho) < 2:
    return True

  for i in range(len(caminho) - 1):
    u = caminho[i]
    v = caminho[i + 1]
    if not existe_aresta(vertices, arestas, u, v, nao_direcionado):
      return False
  return True


def listar_vizinhos(vertices, arestas, vertice, nao_direcionado=True):
  """Exibe os vizinhos de um vértice."""
  if vertice in vertices:
    lista = vizinhos(vertices, arestas, vertice, nao_direcionado)
    print(f"Vizinhos de '{vertice}': {lista}")
    return lista
  else:
    print(f"O vértice '{vertice}' não existe no grafo.")
    return []


def exibir_grafo(vertices, arestas):
  print("\n--- Lista de Arestas ---")
  print(f"Vértices: {vertices}")
  print(f"Arestas: {arestas}")
  print("-" * 40)


def main():
  vertices, arestas = criar_grafo()
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
      exibir_grafo(vertices, arestas)

    elif opcao == "2":
      v = input("Digite o nome do vértice a inserir: ").strip()
      inserir_vertice(vertices, arestas, v)
      print(f"Vértice '{v}' inserido (se já não existia).")

    elif opcao == "3":
      origem = input("Digite o vértice de origem: ").strip()
      destino = input("Digite o vértice de destino: ").strip()
      inserir_aresta(vertices, arestas, origem, destino, nao_direcionado)
      print(f"Aresta entre '{origem}' e '{destino}' inserida.")

    elif opcao == "4":
      v = input("Digite o vértice que deseja remover: ").strip()
      remover_vertice(vertices, arestas, v, nao_direcionado)

    elif opcao == "5":
      origem = input("Digite o vértice de origem da aresta: ").strip()
      destino = input("Digite o vértice de destino da aresta: ").strip()
      remover_aresta(vertices, arestas, origem, destino, nao_direcionado)
      print(f"Aresta entre '{origem}' e '{destino}' removida.")

    elif opcao == "6":
      v = input("Digite o vértice para ver os vizinhos: ").strip()
      listar_vizinhos(vertices, arestas, v, nao_direcionado)

    elif opcao == "7":
      origem = input("Vértice de origem: ").strip()
      destino = input("Vértice de destino: ").strip()
      existe = existe_aresta(vertices, arestas, origem, destino, nao_direcionado)
      if existe:
        print(f"-> SIM! Existe uma aresta entre '{origem}' e '{destino}'.")
      else:
        print(f"-> NÃO existe aresta entre '{origem}' e '{destino}'.")

    elif opcao == "8":
      graus = grau_vertices(vertices, arestas, nao_direcionado)
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
        valido = percurso_valido(vertices, arestas, caminho, nao_direcionado)
        if valido:
          print(
              f"-> O percurso {' -> '.join(caminho)} é valido"
          )
        else:
          print(
              f"-> O percurso {' -> '.join(caminho)} é invalido"
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
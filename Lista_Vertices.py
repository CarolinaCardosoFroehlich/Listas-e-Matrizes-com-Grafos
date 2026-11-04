def criar_grafo():
  return {}


def inserir_vertice(grafo, vertice):
  if vertice not in grafo:
    grafo[vertice] = [] #insere vertices


def inserir_aresta(grafo, origem, destino, nao_direcionado=False):
  inserir_vertice(grafo, origem) #adiciona uma aresta entre os 2 vertices
  inserir_vertice(grafo, destino)

  if destino not in grafo[origem]:
    grafo[origem].append(destino)

  if nao_direcionado:
    if origem not in grafo[destino]:
      grafo[destino].append(origem)


def vizinhos(grafo, vertice):
  if vertice in grafo:
    return grafo[vertice] #descobre os adjacentes
  return []


def listar_vizinhos(grafo, vertice):
  lista = vizinhos(grafo, vertice)
  if vertice in grafo:
    print(f"Vizinhos de '{vertice}': {lista}") #retorna os adjacentes de determinado vertice
  else:
    print(f"O vértice '{vertice}' não existe no grafo.")
  return lista


def exibir_grafo(grafo):
  print("\n--- Lista de Adjacência do Grafo ---")
  if not grafo:
    print("O grafo está vazio.")
  for vertice in sorted(grafo.keys()):
    print(f"{vertice} -> {grafo[vertice]}")
  print("-" * 40)


def remover_aresta(grafo, origem, destino, nao_direcionado=False):
  if origem in grafo:
    if destino in grafo[origem]:
      grafo[origem].remove(destino)

  if nao_direcionado:
    if destino in grafo:
      if origem in grafo[destino]:
        grafo[destino].remove(origem)


def remover_vertice(grafo, vertice, nao_direcionado=True):
  if vertice not in grafo:
    print(f"O vértice '{vertice}' não existe no grafo.")
    return

  for outro in grafo:
    if vertice in grafo[outro]:
      grafo[outro].remove(vertice)

  del grafo[vertice]
  print(f"Vértice '{vertice}' removido com sucesso.")


def existe_aresta(grafo, origem, destino):
  if origem in grafo:
    return destino in grafo[origem]
  return False


def grau_vertices(grafo):
  graus = {} #inicializa grau e retorna o valor
  for vertice in grafo:
    graus[vertice] = {"in": 0, "out": 0, "total": 0}

  for u in grafo:
    graus[u]["out"] = len(grafo[u])
    for v in grafo:
      if u in grafo[v]:
        graus[u]["in"] += 1

  for u in graus:
    graus[u]["total"] = graus[u]["in"] + graus[u]["out"]

  return graus


def percurso_valido(grafo, caminho):
  if not caminho or len(caminho) < 2:
    return True

  for i in range(len(caminho) - 1): #percorre caminhi e ve se existe arestas ligando os vertices
    origem = caminho[i]
    destino = caminho[i + 1]
    if not existe_aresta(grafo, origem, destino):
      return False
  return True


def main():
  grafo = criar_grafo()
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

    opcao = input("\nEscolha uma opção: ")

    if opcao == "1":
      exibir_grafo(grafo)

    elif opcao == "2":
      v = input("Digite o nome do vértice a inserir: ").strip()
      inserir_vertice(grafo, v)
      print(f"Vértice '{v}' inserido (se já não existia).")

    elif opcao == "3":
      origem = input("Digite o vértice de origem: ").strip()
      destino = input("Digite o vértice de destino: ").strip()
      inserir_aresta(grafo, origem, destino, nao_direcionado)
      print(f"Aresta entre '{origem}' e '{destino}' inserida.")

    elif opcao == "4":
      v = input("Digite o vértice que deseja remover: ").strip()
      remover_vertice(grafo, v, nao_direcionado)

    elif opcao == "5":
      origem = input("Digite o vértice de origem da aresta: ").strip()
      destino = input("Digite o vértice de destino da aresta: ").strip()
      remover_aresta(grafo, origem, destino, nao_direcionado)
      print(f"Aresta entre '{origem}' e '{destino}' removida.")

    elif opcao == "6":
      v = input("Digite o vértice para ver os vizinhos: ").strip()
      listar_vizinhos(grafo, v)

    elif opcao == "7":
      origem = input("Vértice de origem: ").strip()
      destino = input("Vértice de destino: ").strip()
      existe = existe_aresta(grafo, origem, destino)
      if existe:
        print(f"-> SIM! Existe uma aresta de '{origem}' para '{destino}'.")
      else:
        print(f"-> NÃO existe aresta direta de '{origem}' para '{destino}'.")

    elif opcao == "8":
      graus = grau_vertices(grafo)
      print("\n--- Graus dos Vértices ---")
      for v, info in graus.items():
        print(
            f"Vértice '{v}': Entrada (In) = {info['in']} | Saída (Out) ="
            f" {info['out']} | Total = {info['total']}"
        )

    elif opcao == "9":
      entrada_caminho = input(
          "Digite o percurso separado por vírgulas (ex: A,B,C,D): "
      ).strip()
      if entrada_caminho:
        caminho = [n.strip() for n in entrada_caminho.split(",")]
        valido = percurso_valido(grafo, caminho)
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


if __name__ == "__main__":
  main()



  # --- BLOCO DE TESTE RÁPIDO ---
if __name__ == "__main__":
  g = criar_grafo()

  print("=== TESTANDO INSERÇÃO DE VÉRTICES E ARESTAS ===")
  inserir_aresta(g, "A", "B", nao_direcionado=True)
  inserir_aresta(g, "A", "C", nao_direcionado=True)
  inserir_aresta(g, "B", "D", nao_direcionado=True)
  inserir_aresta(g, "C", "D", nao_direcionado=True)
  exibir_grafo(g)

  print("=== TESTANDO VIZINHOS ===")
  listar_vizinhos(g, "A")  # Deve mostrar ['B', 'C']

  print("\n=== TESTANDO EXISTÊNCIA DE ARESTA ===")
  print("Existe A -> B?", existe_aresta(g, "A", "B"))  # True
  print("Existe A -> D?", existe_aresta(g, "A", "D"))  # False

  print("\n=== TESTANDO GRAUS ===")
  graus = grau_vertices(g)
  for v, info in graus.items():
    print(f"Vértice {v}: {info}")

  print("\n=== TESTANDO PERCURSO ===")
  caminho_valido = ["A", "B", "D"]
  caminho_invalido = ["A", "D"]
  print(
      f"Percurso {' -> '.join(caminho_valido)} é válido?",
      percurso_valido(g, caminho_valido),
  )  # True
  print(
      f"Percurso {' -> '.join(caminho_invalido)} é válido?",
      percurso_valido(g, caminho_invalido),
  )  # False

  print("\n=== TESTANDO REMOÇÃO DE ARESTA ===")
  remover_aresta(g, "A", "B", nao_direcionado=True)
  exibir_grafo(g)

  print("\n=== TESTANDO REMOÇÃO DE VÉRTICE ===")
  remover_vertice(g, "D", nao_direcionado=True)
  exibir_grafo(g)
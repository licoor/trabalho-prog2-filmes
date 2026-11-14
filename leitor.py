import csv
from titulo import Filme, Serie


def carregar_catalogo(caminho_arquivo: str = "filmes.csv") -> list:
    catalogo = []

    with open(caminho_arquivo, mode="r", encoding="utf-8-sig") as arquivo:
        amostra = arquivo.read(1024)
        arquivo.seek(0)
        separador = ";" if ";" in amostra else ","

        leitor = csv.DictReader(arquivo, delimiter=separador)

        for numero_linha, linha in enumerate(leitor, start=2):
            try:
                titulo = linha["titulo"].strip()
                if not titulo:
                    continue

                diretor = linha["diretor"].strip() or "Desconhecido"
                ano = int(float(linha["ano"]))
                genero = linha["genero"].strip() or "Sem gênero"

                nota = float(str(linha["nota"]).replace(",", "."))
                bilheteria = float(str(linha["bilheteria"] or 0).replace(",", "."))
                nota_critica = int(float(linha["nota_critica"] or 0))
                duracao_ou_temp = int(float(linha["duracao"]))

                tipo = linha["tipo"].strip().lower()

                if tipo == "serie" or tipo == "série":
                    item = Serie(titulo, diretor, ano, duracao_ou_temp, genero, nota, nota_critica, bilheteria)
                else:
                    item = Filme(titulo, diretor, ano, duracao_ou_temp, genero, nota, nota_critica, bilheteria)

                catalogo.append(item)

            except (ValueError, KeyError, TypeError) as erro:
                print(f"Aviso: linha {numero_linha} ignorada por dado inválido ({erro}).")

    return catalogo
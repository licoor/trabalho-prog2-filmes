class Titulo:
    def __init__(self, titulo: str, diretor: str, ano: int, genero: str, nota: float, nota_critica: int, bilheteria: float):
        self.titulo = titulo
        self.diretor = diretor
        self.ano = int(ano)
        self.genero = genero
        self.nota = float(nota)
        self.nota_critica = int(nota_critica)
        self.bilheteria = float(bilheteria)

    def __str__(self):
        return f"{self.titulo} ({self.ano}) | Dir.: {self.diretor} | Gênero: {self.genero} | Nota: {self.nota}"


class Filme(Titulo):
    def __init__(self, titulo: str, diretor: str, ano: int, duracao: int, genero: str, nota: float, nota_critica: int, bilheteria: float):
        super().__init__(titulo, diretor, ano, genero, nota, nota_critica, bilheteria)
        self.duracao = int(duracao)

    def __str__(self):
        return f"[Filme] {super().__str__()} | Duração: {self.duracao} min | Bilheteria: ${self.bilheteria}M"


class Serie(Titulo):
    def __init__(self, titulo: str, diretor: str, ano: int, temporadas: int, genero: str, nota: float, nota_critica: int, bilheteria: float):
        super().__init__(titulo, diretor, ano, genero, nota, nota_critica, bilheteria)
        self.temporadas = int(temporadas)

    def __str__(self):
        return f"[Série] {super().__str__()} | Temporadas: {self.temporadas}"
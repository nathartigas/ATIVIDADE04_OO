# questão 5
from modelos.livro import Livro

# questão 6
livro_biblioteca = Livro("Predador Americano",'Maureen Calahan',2019)
print(f'Antes de emprestar (biblioteca): Livro disponível? {livro_biblioteca.disponivel}')
livro_biblioteca.emprestar()
print(f'Depois de emprestar (biblioteca): Livro disponível? {livro_biblioteca.disponivel}')
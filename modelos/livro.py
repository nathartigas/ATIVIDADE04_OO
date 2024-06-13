# questão 1
class Livro:
    def __init__(self,titulo,autor,ano_publicacao):
        self.titulo=titulo
        self.autor=autor
        self.ano_publicacao=ano_publicacao
        self.disponivel=True
        
#  questão 2
    def __str__(self):
        return f'Livro: {self.titulo} | Autor: {self.autor} | Ano de publicação: {self.ano_publicacao}'
    
    
# livro1=Livro('A Seleção','Kiera Cass',2009)
# livro2=Livro('Predador Americano','Maureen Calahan',2019)

# print(livro1)
# print(livro2)

#  questão 3
    def emprestar(self):
        self.disponivel = False
        
# livro3=Livro('Python sem mistérios','Joel Saade',2020)
# print(f'Antes de emprestar: Livro disponível? {livro3.disponivel}')
# livro3.emprestar()
# print(f'Depois de emprestar: Livro disponível? {livro3.disponivel}')


# questão 4
    @staticmethod
    def verificar_disponibilidade(ano):
        livros_disponiveis=[livro for livro in Livro.livros if livro.ano_publicacao == ano and livro.disponivel]
        for livro in livros_disponiveis:
            print(f'Livros disponíveis em {ano}: {livro}')
            
livro1=Livro('A Seleção','Kiera Cass',2009)
livro2=Livro('Predador Americano','Maureen Calahan',2020)
livro3=Livro('Python sem mistérios','Joel Saade',2020)

Livro.livros=[livro1,livro2,livro3]
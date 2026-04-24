from django.db import models

# 1. Tabela Categorias
class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    class Meta:
        db_table = "categorias"
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        ordering = ["nome"]

    def __str__(self):
        return self.nome


# 2. Tabela Autores
class Autor(models.Model):
    nome = models.CharField(max_length=150)

    class Meta:
        db_table = "autores"
        verbose_name = "Autor"
        verbose_name_plural = "Autores"
        ordering = ["nome"]

    def __str__(self):
        return self.nome


# 3. Tabela Usuarios
class Usuario(models.Model):
    nome = models.CharField(max_length=150)
    email = models.EmailField(max_length=200, unique=True)

    class Meta:
        db_table = "usuarios"
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"
        ordering = ["nome"]

    def __str__(self):
        return self.nome


# 4. Tabela Livros
class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    ano_publicacao = models.IntegerField(null=True, blank=True)
    # Relações 1:N
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name="livros")
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name="livros")

    class Meta:
        db_table = "livros"
        verbose_name = "Livro"
        verbose_name_plural = "Livros"
        ordering = ["titulo"]

    def __str__(self):
        return self.titulo


# 5. Tabela Emprestimos
class Emprestimo(models.Model):
    # Relações 1:N
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="emprestimos")
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE, related_name="emprestimos")
    data_emprestimo = models.DateField()
    data_devolucao = models.DateField(null=True, blank=True)

    class Meta:
        db_table = "emprestimos"
        verbose_name = "Empréstimo"
        verbose_name_plural = "Empréstimos"
        ordering = ["-data_emprestimo"] # Ordena do mais recente para o mais antigo

    def __str__(self):
        return f"{self.livro.titulo} emprestado para {self.usuario.nome}"


from django.contrib import admin
from .models import Livro, Autor, Usuario, Emprestimo, livro_autor, livro_categoria, Categoria
admin.site.register(Livro)
admin.site.register(Autor)
admin.site.register(Usuario)
admin.site.register(Emprestimo)
admin.site.register(livro_autor)
admin.site.register(livro_categoria)
admin.site.register(Categoria)


# Register your models here.

from django.shortcuts import render, redirect
import requests

def index(request):
    response = requests.get('https://daniel51108.pythonanywhere.com/livros/')
    livros = response.json()
    context = {
        'livros': livros
    }
    return render(request, 'index.html', context)

def adicionar(request):
    if request.method == "POST":
        dados = request.POST
        imagem = request.FILES.get("imagem")

        novo_livro = {
            "titulo": dados["titulo"],
            "autor": dados["autor"],
            "ano_lancamento": dados["ano_lancamento"],
            "estado": dados["estado"],
            "paginas": dados["paginas"],
            "editora": dados["editora"],
        }

        files = {
            "imagem": imagem
        }

        post_response = requests.post('https://daniel51108.pythonanywhere.com/livros/', data=novo_livro, files=files)
        return redirect("index")

    context = {}
    return render(request, 'adicionar.html', context)

def editar(request, livro_id):
    if request.method == "GET":
        livro = requests.get(f'https://daniel51108.pythonanywhere.com/livros/{livro_id}/').json()
        context = {
            'livro': livro,
            'livro_id': livro_id
        }
        return render(request, 'editar.html', context)

    elif request.method == "POST":
        dados = request.POST
        imagem = request.FILES.get("imagem")

        livro_atualizado = {
            "titulo": dados.get("titulo"),
            "autor": dados.get("autor"),
            "ano_lancamento": dados.get("ano_lancamento"),
            "estado": dados.get("estado"),
            "paginas": dados.get("paginas"),
            "editora": dados.get("editora")
        }

        files = {
            "imagem": imagem
        }

        put_response = requests.put(f'https://daniel51108.pythonanywhere.com/livros/{livro_id}/', data=livro_atualizado, files=files)
        return redirect("index")

def excluir(request, livro_id):
    if request.method == "GET":
        delete_response = requests.delete(f'https://daniel51108.pythonanywhere.com/livros/{livro_id}/')
        return redirect("index")
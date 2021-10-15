from django.shortcuts import render, redirect
from .models import BlogPost
from .forms import BlogPostForm
from django.http import Http404
from django.contrib.auth.decorators import login_required


def index(request):
    """Página que exibe TODOS OS POSTS"""
    post = BlogPost.objects.order_by('-date_added')
    context = {'posts': post, 'page_name': 'home'}
    return render(request, 'blog_added/index.html', context)


@login_required
def new_post(request):
    """Página que dá o formulário a ser preenchido do NOVO POST"""
    if request.method != 'POST':
        # NOVO: Dá um formulário em branco para ser preenchido
        form = BlogPostForm()
    else:
        # EDITAR: Dá um formulário já existente para ser editado
        form = BlogPostForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.owner = request.user
            new_post.save()
            return redirect('index')

    context = {'form': form, 'page_name': 'new post'}
    return render(request, 'blog_added/new_post.html', context)


@login_required
def edit_posts(request):
    """Página que exibe todos os posts com a opção de EDITAR"""
    posts = BlogPost.objects.filter(owner=request.user).order_by('-date_added')
    context = {'posts': posts, 'page_name': 'my posts'}
    return render(request, 'blog_added/edit_posts.html', context)


@login_required
def edit_post(request, blogpost_id):
    """Página que dá a opção de EDITAR um post existente"""
    post = BlogPost.objects.get(id=blogpost_id)

    if post.owner != request.user:
        raise Http404

    if request.method != 'POST':
        form = BlogPostForm(instance=post)
    else:
        form = BlogPostForm(instance=post, data=request.POST)

        if form.is_valid():
            form.save()
            return redirect('edit_posts')

    context = {'post': post, 'form': form, 'page_name': 'edit'}
    return render(request, 'blog_added/edit_post.html', context)


def read_more(request, blogpost_id):
    post = BlogPost.objects.get(id=blogpost_id)
    context = {'post': post}
    return render(request, 'blog_added/read_more.html', context)

from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Post, Category
from .forms import PostForm, CategoryForm
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from django.core.paginator import Paginator
from django.db.models import Count, Q

def index(request):
    categories = Category.objects.annotate(no_of_posts=Count('post', filter=Q(post__published_date__isnull=False))).filter(published_date__isnull=False)
    return render(request, 'index.html', {'categories': categories})

@login_required
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('category','priority', '-published_date')  
    paginator = Paginator(posts, 25)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'post_list.html', {'page_obj': page_obj})

@login_required
def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('priority', '-created_date')
    paginator = Paginator(posts, 25)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'post_draft_list.html', {'page_obj': page_obj})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detail.html', {'post': post})

@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()            
            return redirect('post_draft_list')
    else:
        form = PostForm()
    return render(request, 'post_edit.html', {'form': form})

@login_required
def post_edit(request, pk):
     post = get_object_or_404(Post, pk=pk)
     if request.method == "POST":
         form = PostForm(request.POST, instance=post)
         if form.is_valid():
             post = form.save(commit=False)
             post.author = request.user
             post.save()
             if str(request.POST["next"]):
                return redirect(str(request.POST["next"]))
             else:
                return redirect('post_detail', pk=post.pk)             
     else:
         form = PostForm(instance=post)
     return render(request, 'post_edit.html', {'form': form, 'pk': post.pk, 'name': post.title})

def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()    
    return redirect('post_list')

def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_draft_list')

def post_unpublish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.unpublish()
    return redirect('post_list')

def post_priority_up(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.priority_up()
    return redirect('post_list')

def post_priority_down(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.priority_down()
    return redirect('post_list')

@login_required
def category_list(request):
    #categories = Category.objects.all().order_by('priority', '-created_date')
    categories = Category.objects.annotate(no_of_posts=Count('post', filter=Q(post__published_date__isnull=False))).filter(published_date__isnull=False).order_by('priority', '-created_date')
    return render(request, 'category_list.html', {'categories': categories})

@login_required
def category_draft_list(request):
    categories = Category.objects.annotate(no_of_posts=Count('post', filter=Q(post__published_date__isnull=False))).filter(published_date__isnull=True).order_by('priority', '-created_date')
    return render(request, 'category_draft_list.html', {'categories': categories})

def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    posts = Post.objects.filter(category=pk, published_date__isnull=False).order_by('priority', '-published_date')
    cnt = posts.count()
    paginator = Paginator(posts, 25)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'category_detail.html', {'category': category, 'count': cnt, 'page_obj': page_obj})

@login_required
def category_new(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.save()
            return redirect('category_draft_list')
    else:
        form = CategoryForm()
    return render(request, 'category_edit.html', {'form': form})

@login_required
def category_edit(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == "POST":
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            category = form.save(commit=False)
            category.save()
            return redirect('category_detail', pk=category.pk)
    else:
        form = CategoryForm(instance=category)
    return render(request, 'category_edit.html', {'form': form, 'pk': category.pk, 'name': category.name})

def category_remove(request, pk):
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    return redirect('category_list')

def category_publish(request, pk):
    category = get_object_or_404(Category, pk=pk)
    category.publish()
    return redirect('category_draft_list')

def category_unpublish(request, pk):
    category = get_object_or_404(Category, pk=pk)
    category.unpublish()
    return redirect('category_list')
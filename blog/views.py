from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Blogs, Comment
from django.db.models import Q
from .forms import CommentForm

def home(request):
    blogs = Blogs.objects.all()
    query = request.GET.get('query','')
    category_id = request.GET.get('category', 0)
    categorys = Category.objects.all()

    if(category_id):
        blogs = blogs.filter(category_id=category_id)

    if query:
        blogs = blogs.filter(Q(title__icontains=query))

    return render(request, 'blog/index.html', {
        'blogs':blogs,
        'categorys':categorys,
        'query':query,
        'category_id':int(category_id)
    })


def detail(request, pk):
    blog = get_object_or_404(Blogs, pk=pk)
    related = Blogs.objects.filter(category = blog.category).exclude(pk=pk)[0:4]
    comment = Comment.objects.filter(blog=pk)
    form = None

    if request.method == "POST" and request.user.is_authenticated:
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.blog = blog
            comment.user = request.user
            comment.save()

            return redirect('blog:detail', pk=blog.id)
            

    if request.user.is_authenticated:
        form = CommentForm()

    return render(request, 'blog/detail.html', {
        'blog':blog,
        'related':related,
        'form':form,
        'comment':comment
    })
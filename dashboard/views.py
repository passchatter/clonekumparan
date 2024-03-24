from django.shortcuts import render, redirect, get_object_or_404
from blog.models import Blogs
from django.contrib.auth.decorators import login_required
from .form import NewBlogForm
from blog.models import Blogs

@login_required
def dashboardBlog(request):
    blogs = Blogs.objects.filter(create_by = request.user)

    return render(request, 'dashboard/index.html',{
        'blogs':blogs
    })


@login_required
def newBlog(request):

    if request.method == 'POST':
        form = NewBlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.create_by = request.user
            blog.save()
            return redirect('/')
    
    else:
        form = NewBlogForm()

    return render(request, 'dashboard/newblog.html', {
        'form':form,
        'title':'add blog'
    })


@login_required
def updateBlog(request, pk):
    blog = get_object_or_404(Blogs, pk=pk, create_by = request.user)

    if request.method == 'POST':
        form = NewBlogForm(request.POST, request.FILES, instance=blog)

        if form.is_valid():
            form.save()
            return redirect('blog:detail', pk=blog.id)

    else:
        form = NewBlogForm(instance=blog)

    return render(request, 'dashboard/newblog.html', {
        'form':form,
        'title':'update blog'
    })

def deleteBlog(request, pk):
    blog = get_object_or_404(Blogs, pk=pk)
    blog.delete()

    return redirect('/')





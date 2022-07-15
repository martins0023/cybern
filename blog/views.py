#import all modules to be used
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import Post, Cyberspace, Link, Service
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect
from contact.forms import contact_us_name, contact_us_email, contact_us_subject, contact_us_message
  
#create function for the routing of the homepage
def home(request):
    if request.method == 'POST':
        form_name = contact_us_name(request.POST)
        form_email = contact_us_email(request.POST)
        form_subject = contact_us_subject(request.POST)
        form_message = contact_us_message(request.POST)
        if form_name.is_valid and form_email.is_valid and form_subject.is_valid and form_message.is_valid():
            form_name.save()
            form_email.save()
            form_subject.save()
            form_message.save()
            
            #username = form.cleaned_data.get('username')
            messages.success(request, f'Your message has been sent successfully, we\'ll get back to you asap with the info provided. Thanks !')
            return redirect('home')
    else:
        form_name = contact_us_name()
        form_email = contact_us_email()
        form_subject = contact_us_subject()
        form_message = contact_us_message()
    #create a dictionary for context to be displayed in the html page
    context = {
        'form_name': form_name,
        'form_email': form_email,
        'form_subject': form_subject,
        'form_message': form_message,
        'services': Service.objects.all(),
        'links': Link.objects.all(),
        'title': 'x_-_c'
    } 
    return render(request, 'blog/home.html', context)

#create function for the routing of the cyberspace page
def cyberspace(request):
    if request.method == 'POST':
        form_name = contact_us_name(request.POST)
        form_email = contact_us_email(request.POST)
        form_subject = contact_us_subject(request.POST)
        form_message = contact_us_message(request.POST)
        if form_name.is_valid and form_email.is_valid and form_subject.is_valid and form_message.is_valid():
            form_name.save()
            form_email.save()
            form_subject.save()
            form_message.save()
            
            #username = form.cleaned_data.get('username')
            messages.success(request, f'Your message has been sent successfully, we\'ll get back to you asap with the info provided. Thanks !')
            return redirect('cyberspace')
    else:
        form_name = contact_us_name()
        form_email = contact_us_email()
        form_subject = contact_us_subject()
        form_message = contact_us_message()
    context = {
        'form_name': form_name,
        'form_email': form_email,
        'form_subject': form_subject,
        'form_message': form_message,
        'cyberspaces': Cyberspace.objects.all(),
        'links': Link.objects.all(),
        'title': 'cyberspace'
    }
    return render(request, 'blog/cyberspace.html', context)

def discuss_space(request):
    context = {
        'title': 'Discussions',
        'posts': Post.objects.all(),
        'links': Link.objects.all()
    }
    return render(request, 'blog/discuss_space.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'blog/discuss_space.html'
    title = 'Discussions'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 10
    
    
    
class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 10
    
    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')
    
class PostDetailView(DetailView):
    model = Post
    
class CommentCreateView(CreateView, LoginRequiredMixin):
    model = Post
    fields = ['comment']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    def success_message(request):
        messages.success(request, f'post has been deleted $$%&^$#')
    model = Post
    success_url = '/'
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
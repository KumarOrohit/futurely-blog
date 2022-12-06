from django.http import HttpResponseRedirect
from .models import blog, comment
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.shortcuts import render


# Create your views here.

class BlogListView(LoginRequiredMixin, ListView):
    model = blog
    template_name = 'feed/home.html'
    ordering = ['-dateTime']
    paginate_by = 5


class BlogCreateView(LoginRequiredMixin, CreateView):
    model = blog

    fields = ['content']
    success_url = '/'

    def form_valid(self, form):
        form.instance.usrName = self.request.user
        return super().form_valid(form)


class BlogUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = blog

    fields = ['content']
    success_url = '/'

    def form_valid(self, form):
        form.instance.usrName = self.request.user
        return super().form_valid(form)

    def test_func(self):
        blogs = self.get_object()
        if self.request.user == blogs.usrName:
            return True
        return False


class BlogDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = blog
    success_url = '/'

    def test_func(self):
        blogs = self.get_object()
        if self.request.user == blogs.usrName:
            return True
        return False


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = comment

    fields = ['comment']
    success_url = '/'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        blog_obj = blog.objects.get(id=self.kwargs['blog'])
        self.object.blog = blog_obj
        self.object.save()
        return super().form_valid(form)


class CommentUpdateView(View):
    model = comment

    def get(self, request, *args, **kwargs):
        comment_obj = comment.objects.get(id=self.kwargs['pk'])
        comment_obj.like += 1
        comment_obj.save()
        return HttpResponseRedirect('/')


class ShareBlogView(View):
    model = blog

    def post(self, request, *args, **kwargs):
        blog_obj = blog.objects.get(id=self.kwargs['pk'])
        email_response = send_mail(
            'Blog shared by: ' + str(blog_obj.usrName.username),
            blog_obj.content,
            "rk9818235826@gmail.com",
            [request.POST["email_field"]],
            fail_silently=False,
        )
        if email_response == 1:
            messages.success(request, f'Account Created, Please Login')
        else:
            messages.error(request, f'Failed to send share')
        return HttpResponseRedirect('/')



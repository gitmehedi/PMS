from django.contrib.auth import authenticate,login,logout
from django.http import Http404,JsonResponse,HttpResponse
from django.core import serializers

from django.shortcuts import render,redirect,get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from pm_module import forms
from pm_module import models
from auth_module.msg import *





def index(request):
    lists = models.ProjectModel.objects.all()
    form = forms.ProjectForm(request.POST or None)
    query = request.GET.get('q')

    if query:
        lists = lists.filter(
            Q(name__contains=query) |
            Q(telephone_no__contains=query) |
            Q(available_time__contains=query)
        ).distinct()

        # lists = pagination(request, lists=lists)

        return render(request, 'project/create.html', {'form': form, 'lists': lists})

    return render(request, 'project/lists.html', {'form': form, 'lists': lists})


def create_project(request):
    lists = models.ProjectModel.objects.all()
    #     if not request.user.is_authenticated():
    #         return render(request, 'pages/login.html')
    #     else:
    form = forms.ProjectForm(request.POST or None, request.FILES or None)
    # lists = pagination(request, lists=lists)
    if form.is_valid():
        post_data = form.save(commit=False)
        if request.FILES:
            post_data.picture = request.FILES['picture']
            file_type = post_data.picture.url.split('.')[-1]
            file_type = file_type.lower()

            context = {
                'lists': lists,
                'form': form,
            }

            if file_type not in ['png', 'jpg', 'jpeg']:
                context['error_message'] = 'file type is not supprted'

            return render(request, 'project/lists.html', context)

        post_data.save()
        return redirect('create_project')

    else:
        return render(request, 'project/create.html', {'form': form, 'lists': lists})


def edit_project(request, pk=None):
    lists = models.ProjectModel.objects.all()
    instance = get_object_or_404(models.ProjectModel, pk=pk)
    form = forms.ProjectForm(request.POST or None, request.FILES or None, instance=instance)
    # lists = pagination(request, lists=lists)

    if request.method == "POST":
        if form.is_valid():
            post_data = form.save(commit=False)
            if request.FILES:
                post_data.picture = request.FILES['picture']
                file_type = post_data.picture.url.split('.')[-1]
                file_type = file_type.lower()

                if file_type not in ['png', 'jpg', 'jpeg']:
                    context = {
                        'lists': lists,
                        'form': form,
                        'error_message': 'file type is not supprted'
                    }

                return render(request, 'doctor/lists.html', context)

            post_data.save()
            return redirect('homepage')

    return render(request, 'project/edit.html', {'form': form, 'lists': lists, 'pk': pk})


def delete(request, pk):
    instance = get_object_or_404(models.ProjectModel, pk=pk)
    instance.delete()
    return redirect('homepage')

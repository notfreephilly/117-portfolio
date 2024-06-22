from django.shortcuts import render



def projects_list(request):
    return render(request, 'content/projects_list.html')

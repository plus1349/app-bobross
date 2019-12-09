from django.shortcuts import render, HttpResponse


def users(request):
    return HttpResponse('USERS')

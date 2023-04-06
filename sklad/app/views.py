from django.shortcuts import render, redirect

def home(response):
    return render(response, "index.html", {})
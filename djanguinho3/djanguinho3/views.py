from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import reverse

# Create your views here.
def index(request):
    htmlres = """
    " ๐  Olรก, seja bem vindo :) ๐  "<br>
    <ul>
    <li><a href='laguardia'> โ laguardia</a></li>
    <li><a href='RodrigoPintucci'> ๐ฆ RodrigoPintucci</a></li>
    <li><a href='treuke'> ๐ก treuke</a></li>
    <li><a href='Rian'> ๐คซ Rian</a></li>
    <li><a href='kayo'> โฐ๏ธ kayo</a></li>
    <li><a href='dominique'> ๐ dominique</a></li>
    <li><a href='iara'> ๐งโโ๏ธ iara</a></li>
    </ul>
    """
    return HttpResponse(htmlres)

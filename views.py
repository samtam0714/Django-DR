from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import pickle
from sklearn.externals import joblib
from .models import Document
from .forms import DocumentForm
from django.http import JsonResponse
from gensim.models.keyedvectors import KeyedVectors
from . import DocSim
from gensim import models


def home(request):
    documents = Document.objects.all()
    return render(request, 'files/home.html', {'documents': documents})


def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'files/simple_upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'files/simple_upload.html')


def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DocumentForm()
    return render(request, 'files/model_form_upload.html', {
        'form': form

    })

def abc(request):
    if request.method == 'GET':
        

        return render(request, 'files/abc.html')


def score(request):
    if request.method == 'GET':

        mdl=joblib.load("/Users/samantha/Desktop/New folder/load_model.pkl")
    

        return JsonResponse('Your score is {}'.format(mdl),safe=False)

def cosimscore(request):
    if request.method == "POST":
        googlenews_model_path = open('./files/GoogleNews-vectors-negative300.bin')
        stopwords_path = open('./files/SmartStoplist.txt')
        model = KeyedVectors.load_word2vec_format(googlenews_model_path, binary=True)
        with open(stopwords_path, 'r') as fh:
            stopwords = fh.read().split(",")
        ds = DocSim(model,stopwords=stopwords)

        source_doc = "hello world"
        target_docs = ['hello', 'world', "hello world"]

        sim_scores = ds.calculate_similarity(source_doc, target_docs)
        return JsonResponse({'sim_scores':str(sim_scores)})
        #return JsonResponse([1,2,3,4,5], safe=False)
        #return render(request, 'sim_scores')
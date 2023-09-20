import requests
from django.shortcuts import render
from PyDictionary import PyDictionary

def home(request):
    if request.method == 'POST':
        word = request.POST.get('word')
        dictionary = PyDictionary()

        try:
            meaning = dictionary.meaning(word)
            synonyms = dictionary.synonym(word)
            antonyms = dictionary.antonym(word)
        except:
            meaning = None
            synonyms = None
            antonyms = None

        context = {
            'word': word,
            'meaning': meaning,
            'synonyms': synonyms if synonyms else [],
            'antonyms': antonyms if antonyms else [],
        }
        return render(request, 'dictionary/home.html', context)

    return render(request, 'dictionary/home.html')

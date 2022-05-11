import random
import re

from django.shortcuts import render, redirect
from .models import Account, Attempt
from django.http import HttpResponse
from django.template import loader

# When they visit the page, send them to a new attempt
def index(request):
    if Attempt.objects.order_by("-datetime"):
        last_attempt = Attempt.objects.order_by('-datetime')[0]
        last_id = last_attempt.id if last_attempt else 1
        new_id = last_id + 1
    else:
        new_id = 1
    return redirect(f"/{new_id}/", [request, new_id])


def random_sentence(length):
    words = [word.strip() for word in list(open("pietype/words.txt", "r"))]
    return random.choices(words, k=length)


# This is the attempt view
def attempt(request, attempt_id):
    all = Attempt.objects.all()
    print(all)
    # Return them to the index if they try to go to an old attempt
    if attempt_id <= len(all) and all[attempt_id - 1]:
        attempt = all[attempt_id - 1]
        return load_attempt(request, attempt)

    # We need to procedurally generate a new, psuedo-random sentence
    # sentence = "a quick brown fox jumps over the fence, but it was too slow and so it got caught by the fast hunter."
    # sentence = sentence.split()
    length = int(request.GET.get('length', default=30))
    sentence = random_sentence(length)

    # This is where we will load JS and make it look pretty
    template = loader.get_template("pietype/index.html")
    context = {
        'sentence': sentence,
        'attemptID': attempt_id
    }
    return render(request, 'pietype/index.html', context)


def save(request):
    if request.method == "POST":
        print(request.POST)
        sentence = request.POST.get('sentence', [])
        rawWPM = int(request.POST.get('rawWPM', 0))
        wpm = int(request.POST.get('wpm', 0))
        accuracy = int(request.POST.get('accuracy', 0))
        attemptID = request.POST.get('attemptID', 0)
        time = request.POST.get('time', "00:00")

        context = {
            'sentence': sentence,
            'rawWPM': rawWPM,
            'wpm': wpm,
            'accuracy': accuracy,
            'attemptID': attemptID,
            'time': time
        }

        att = Attempt(sentence=sentence, raw_wpm=rawWPM, wpm=wpm, accuracy=accuracy, time=time)
        print(attemptID)
        att.save()

        return render(request, 'pietype/pastAttempt.html', context)

    return HttpResponse("Error")

def load_attempt(request, attempt):
    sentence = attempt.sentence
    # Need to turn <char,class> <char,class> ;<char, class> ;
    # Into [[[char, class], [char,class]], [[char,class]]]
    array = []
    words = sentence.split(";")
    for word in words:
        wordArray = []
        letters = word.split(" ")
        for letter in letters:
            if letter == "":
                continue

            letterArray = letter.split(",")
            wordArray.append(letterArray)

        array.append(wordArray)

    context = {
        'sentence': array,
        'wpm': attempt.wpm,
        'rawWPM': attempt.raw_wpm,
        'accuracy': attempt.accuracy,
        'time': attempt.time
    }

    return render(request, 'pietype/pastAttempt.html', context)

def about(request):
    return render(request, 'pietype/about.html')
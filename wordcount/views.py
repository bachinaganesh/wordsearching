from django.shortcuts import render
from .forms import WordCountForm
import os
from django.conf import settings

def count_word_in_file(uploaded_file, word):
    count = 0
    # Iterate over the lines in the uploaded file
    for line in uploaded_file:
        # Decode the line if it's bytes-like object
        if isinstance(line, bytes):
            line = line.decode('utf-8')
        # Count occurrences of the word in each line (case insensitive)
        count += line.lower().count(word.lower())
    return count


def word_count(request):
    if request.method == 'POST':
        form = WordCountForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['file']
            word = form.cleaned_data['word']
            count = count_word_in_file(uploaded_file, word)
            return render(request, 'wordcount/result.html', {'count': count, 'word': word})
    else:
        form = WordCountForm()
    return render(request, 'wordcount/upload.html', {'form': form})

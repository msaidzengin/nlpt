import string

def tr2eng(text):
    return text.translate(str.maketrans('ğĞıİöÖüÜşŞçÇ', 'gGiIoOuUsScC')).lower()

def clean_words(text):
    return text.translate(str.maketrans('', '', string.punctuation)).lower()

def clean_words_upper(text):
    text = text.translate(str.maketrans('ğĞıİöÖüÜşŞçÇ', 'gGiIoOuUsScC', string.punctuation)).upper()
    text = ' '.join(text.split())
    return ''.join([i if ord(i) < 128 else '' for i in text])

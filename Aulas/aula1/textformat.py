#!/usr/bin/env python

from sys import argv
import re

def format_text(text):
    # text = ' . '.join(text.split('.'))
    # text = ' '.join(re.split(r'(\.+|[.,!?;:])', text))
    text = re.sub(r'(\.+|[.,!?;:])',r" \1 ", text)
    acentos = {
            'ã': 'a',
            'á': 'a',
            'é': 'e',
            'í': 'i',
            'ó': 'o'
    }
    text = ''.join([acentos.get(letra, letra) for letra in text])
    return text

with open(argv[1]) as f:
    print(format_text(f.read()))

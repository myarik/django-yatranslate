#!/usr/bin/env python
# -*- coding: utf-8 -*-

from grab import Grab

URL_API = 'http://translate.yandex.net/api/v1/tr/translate'


def translate(text):
    g = Grab()
    translate_text = ''
    g.setup(post={'lang': 'ru', 'text': text})
    g.go(URL_API)
    for line in g.xpath_list('//text'):
        ru_str = line.text
        if ru_str:
            translate_text += ru_str
        else:
            translate_text += ''
    return translate_text

if __name__ == '__main__':
    print "Text: Hello, how are you?"
    print "Translate:", translate('Hello, how are you?')

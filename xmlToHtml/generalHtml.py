#!/usr/bin/python
# -*- coding: UTF-8 -*-

from bs4 import BeautifulSoup

if (__name__ == "__main__"):
    soup = BeautifulSoup(open('./王二小报告全集.html', encoding="utf-8"),features='html.parser')
    print(soup.prettify())
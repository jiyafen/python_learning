#!/usr/bin/python
# -*- coding: UTF-8 -*-
import xmltodict

if (__name__ == "__main__"):
    xml_file = open("./王小二.xml","r", encoding="utf-8")
    xml_str = xml_file.read()
    json = xmltodict.parse(xml_str)
    print(json)
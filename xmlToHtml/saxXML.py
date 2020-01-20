#!/usr/bin/python
# -*- coding: UTF-8 -*-

import xml.sax
import copy
from xmlKeyValue import *

class reportHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.CurrentData = ""
        self.reportHeadInfo = {}
        self.personalInfo = {}
        self.tempInfo = {}
        self.phoneInfoList = []
        self.spouseInfo = {}
        self.residentialInfoList = []
        self.workInfoList = []


    # 元素开始事件处理
    def startElement(self, tag, attributes):
        self.CurrentData = tag

    # 元素结束事件处理
    def endElement(self, tag):
        self.CurrentData = ""

    # 内容事件处理
    def characters(self, content):
        strTemp = ""
        if self.CurrentData in reportHeadDict.keys():
            strTemp = reportHeadDict[self.CurrentData]
            self.reportHeadInfo[strTemp] = content
        elif self.CurrentData in personalInfoDict.keys():
            strTemp = personalInfoDict[self.CurrentData]
            self.personalInfo[strTemp] = content
        elif self.CurrentData in phoneNumberInfoDict.keys():
            strTemp = phoneNumberInfoDict[self.CurrentData]
            self.tempInfo[strTemp] = content
            if len(self.tempInfo) == len(phoneNumberInfoDict):
                self.phoneInfoList.append(copy.deepcopy(self.tempInfo))
                self.tempInfo.clear()
        elif self.CurrentData in spouseInfoDict.keys():
            strTemp = spouseInfoDict[self.CurrentData]
            self.spouseInfo[strTemp] = content
        elif self.CurrentData in residentialInfoDict.keys():
            strTemp = residentialInfoDict[self.CurrentData]
            self.tempInfo[strTemp] = content
            if len(self.tempInfo) == len(residentialInfoDict):
                self.residentialInfoList.append(copy.deepcopy(self.tempInfo))
                self.tempInfo.clear()
        elif self.CurrentData in workInfoDict.keys():
            strTemp = workInfoDict[self.CurrentData]
            self.tempInfo[strTemp] = content
            if len(self.tempInfo) == len(workInfoDict):
                self.workInfoList.append(copy.deepcopy(self.tempInfo))
                self.tempInfo.clear()

if (__name__ == "__main__"):
    # 创建一个 XMLReader
    parser = xml.sax.make_parser()
    # turn off namepsaces
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)

    # 重写 ContextHandler
    Handler = reportHandler()
    parser.setContentHandler(Handler)

    parser.parse("./王小二.xml")
    # for key in Handler.reportHeadInfo:
    #     print(key + ':' + Handler.reportHeadInfo[key])
    # for key in Handler.personalInfo:
    #     print(key + ':' + Handler.personalInfo[key])
    # print(Handler.phoneInfoList)
    # for key in Handler.spouseInfo:
    #     print(key + ':' + Handler.spouseInfo[key])
    # print(Handler.residentialInfoList)
    # print(Handler.workInfoList)
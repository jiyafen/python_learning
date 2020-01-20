# coding:utf-8
import os
import re
import time
import xml
import xml.etree.ElementTree as ET
# 全局唯一标识
unique_id = 1

# 遍历所有的节点
def walkData(root_node, level, result_list):
    global unique_id
    #temp_list = [unique_id, level, root_node.tag, root_node.text, root_node.attrib]
    #result_list.append(temp_list)
    if (len(root_node.tag) == 8)and (root_node.tag.startswith("P")):
        temp_list = [root_node.tag, root_node.text]
        result_list.append(temp_list)

    # 遍历每个子节点
    children_node = root_node.getchildren()
    if len(children_node) == 0:
        return
    for child in children_node:
        walkData(child, level + 1, result_list)
    return


def getXmlData(file_name):
    level = 1  # 节点的深度从1开始
    result_list = []
    root = ET.parse(file_name).getroot()
    walkData(root, level, result_list)

    return result_list

def generationHtmlTemplate(htmlFilePath, newFilePath, result_list):
    # 更新html文件
    htmlFile = open(htmlFilePath, 'r', encoding='utf-8')
    newHtmlFile = open(newFilePath, 'w', encoding='utf-8')
    for line in htmlFile:
        for item in result_list:
            findStr = '>' + item[1] + '<'
            newStr = '{' + item[0] + '}'
            if findStr in line:
                newline = line.replace(item[1], newStr, 1)
                line = newline
                result_list.remove(item)
                break
        newHtmlFile.write(line)
    htmlFile.close()
    newHtmlFile.close()

def isVaildDate(date):
    try:
        time.strptime(date, "%Y-%m-%dT%H:%M:%S.000+08:00")
        return True
    except:
        return False

def is_number(str):
    try:
        float(str)
        return True
    except ValueError:
        return False

def intcomma(value):
    orig = str(value)
    new = re.sub("^(-?\d+)(\d{3})", '\g<1>,\g<2>', orig)
    if orig == new:
        return new
    else:
        return intcomma(new)

def dateInfoTransform(result_list):
    for item in result_list:
        if isVaildDate(item[1]):
            newDateStr = item[1].replace('-', '.', 3)
            dateList = newDateStr.split('T')
            newDateStr = dateList[0]
            item[1] = newDateStr
        elif is_number(item[1]):
            if item[0].endswith(('J01','J02','J03','J04','J05')):
                newMoneyStr = intcomma(item[1])
                item[1] = newMoneyStr

if __name__ == '__main__':
    #读取xml文件
    file_name = "./王小二.xml"
    result_list = getXmlData(file_name)
    dateInfoTransform(result_list)

    htmlPath = './王二小报告全集.html'
    generationPath = './template.html'
    os.path.exists(generationPath)
    os.remove(generationPath)
    generationHtmlTemplate(htmlPath, generationPath, result_list)
    # f = open('./output.txt', 'a')
    # for item in result_list:
    #     f.write('\n' + str(item))
    # f.close()
    # pass

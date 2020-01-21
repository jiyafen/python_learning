# encoding: utf-8

# 两数之和
def TwoNumSum(numList, target):
    for i in numList:
        findNum = target - i
        if findNum in numList:
            index1 = list.index(numList,i)
            index2 = list.index(numList,findNum)
            if index2 == index1:
                try:
                    index2 = list.index(numList,findNum,index2+1)
                except ValueError:
                    errstr = "%d is not double in list" % (findNum)
                    print(errstr)
            if index1 != index2:
                str1 = "find index are %d and %d, %d + %d = %d " % (index1, index2, i, findNum, target)
                print(str1)
                break


if __name__ == '__main__':
    numList = [1,2,4,5,7,9]
    target = 6
    TwoNumSum(numList, target)


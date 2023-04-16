import xml.etree.ElementTree as ET
from pathlib import Path
import re
mytree = ET.parse('sample.xml')
myroot = mytree.getroot()

def parameterCheck(path,xPath, paramName, paraValue):

    print("====================================")
    print("VERIFY XML PATH ::")
    xmlFile = Path(path)
    if xmlFile.is_file():
        print("XML Path Exist")
    else:
        print("XML Path Does not exist")
        exit()

    print("====================================")
    print("VERIFY XPATH  ::")
    xpathCheck = myroot.findall(xPath)
    if xpathCheck:
        print("Xpath Exist")
    else:
        print("Xpath does not exist")
        exit()

    print("====================================")
    print("VERIFY PARAMETER NAME ::")
    for item in myroot.findall(xPath):                    # Xpath == './food/price'
        if paramName in item.tag:                         # Parameter Name == price
            price = item.text
            print(item.tag ,  "Parameter Exists &" " Value is", price)
        else:
            print(item.tag ,  "parameter do not exist")

    print("====================================")
    print ("VERIFY ANY ONE PARAMETER VALUE PASS/FAIL ::")
    for item2 in myroot.findall(xPath):
        value = item2.text
        if value == paraValue :
            print("PASS")
        else:
            print("FAIL")


parameterCheck("C:/Users/naveen.kulkarni/PycharmProjects/practice_Test/sample.xml" ,"./food/price", "price", "$2.5")

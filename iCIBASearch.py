# -*- coding: utf-8 -*-

__author__ = 'Zichuan Wang'

import urllib2
import xml.dom.minidom

printCount = 0

theQuery = "{query}"
theQuery = "eliminate"
theQuery = theQuery.strip()
searchURL = 'http://dict-co.iciba.com/api/dictionary.php?key=920884E0432F63B57D8E982006557B06&w='
URLDoc = xml.dom.minidom.parse(urllib2.urlopen(searchURL + theQuery))

print searchURL + theQuery
    
def printItem(title, subTitle = ''):
    global printCount
    print "    <item uid=\"" + str(printCount) + "\" arg=\""+ theQuery +"\">"
    print "        <title>" + title.encode('utf-8').strip('\n') + "</title>"
    print "        <subtitle>" + subTitle.encode('utf-8').strip('\n') + "</subtitle>"
    print "        <icon type=\"fileicon\">/Applications/iTunes.app/</icon>"
    print "    </item>"
    printCount += 1


print "<?xml version=\"1.0\"?>\n<items>"

dict = URLDoc.getElementsByTagName('dict')[0]

pronunciations = dict.getElementsByTagName('ps')
for index in range(len(pronunciations)):
    pronunciation = pronunciations[index].firstChild.data
    if index == 0:
        printItem('[' + pronunciation + ']', u'英音')
    elif index == 1:
        printItem('[' + pronunciation + ']', u'美音')

acceptations = dict.getElementsByTagName('acceptation')
for index in range(len(acceptations)):
    acceptation = acceptations[index].firstChild.data.replace("<", "[").replace(">", "]")
    posRaw = pos = dict.getElementsByTagName('pos')[index].firstChild
    pos = ''
    if posRaw:
        pos = dict.getElementsByTagName('pos')[index].firstChild.data.replace("&", " and")
    printItem(acceptation, pos)
    
scentences = dict.getElementsByTagName('sent')
for scentence in scentences:
    orig = scentence.getElementsByTagName('orig')[0].firstChild.data
    trans = scentence.getElementsByTagName('trans')[0].firstChild.data
    printItem(orig, trans)
    
print "</items>\n"
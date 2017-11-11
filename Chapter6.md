# 第六章 csv，json，xml,excel高效解析与构建技巧训练
## 6-1 如何读写csv数据
![6-1.png](https://i.loli.net/2017/11/11/5a06d938544a3.png)
```
import csv
f = open('test.csv', 'rb')
reader = csv.reader(f)
for i in reader:
    print(i)
# 写
f = open('test.csv', 'wb')
w = csv.writer(f)
w.writerow('...')
```

## 6-2 如何读写json数据 
![6-2.png](https://i.loli.net/2017/11/11/5a06dbee1bb7b.png)
```
# 录音
from record import Record
record = Record(channels = 1)
audioData = record.record(2) # 2s
```
```
import json
l = [1, 2, 'abc', {'a':10, 'b':'abc'}]
```

## 6-3 如何解析简单的xml文档
![6-3.png](https://i.loli.net/2017/11/11/5a06ddb55c099.png)
```
from xml.etree.ElementTree import parse
f = open('demo.xml')
et = parse(f)
root = et.getroot()
root.tag
root.text
root.attrib
for child in root:
    print(child.get('name'))
root.findall('country')
for i in root.iterfind('country'):
    print(child.get('name'))
root.findall('country/*') # 寻找所有孙子节点
root.findall('country[@name='Singapore'])
```

## 6-4 如何构建xml文档
![6-4.png](https://i.loli.net/2017/11/11/5a06e35e9443b.png)
```
from xml.etree.ElementTree import Element, ElementTree, tostring
e = Element('Data')
e.tag # 'Data'
e.set('name', 'abc')
tostring(e) # "<Data name='abc' />"
e.text = '123'
tostring(e) # "<Data name='abc'>123</Data>"
e2 = Element('Row')
e3 = Element('Open')
e3.text = '123'
e2.append(e3)
tostring(e2) 3 '<Row><Open>123</Open></Row>'
e.text = None
e.append(e2)
et = ElementTree(e)
et.write('demo.xml')
```

## 6-5 如何读写excel文件
![6-5.png](https://i.loli.net/2017/11/11/5a06e35b9dd9e.png)
```
import xlrd
book = xlrd.open_workbook('demo.xlsx')
sheet = book.sheet_by_index(0)
sheet.nrows # 行
sheet.ncols # 列
cell = sheet.cell(0, 0)
cell.value
sheet.row(0)
sheet.row_values(1)
# sheet.putcell(row, col, ctype, value, xf_index)
sheet.putcell(0, sheet.ncols, xlrd.XL_CELL_TEXT, '总分', Null)
import xlwt
wbook = xlwt.Workbook()
wsheet = wbook.add_sheet(1)
```


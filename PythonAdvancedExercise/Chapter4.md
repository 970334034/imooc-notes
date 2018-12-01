# 第四章 字符串处理技巧训练

## 4-1 拆分字符串
![4-1.png](https://i.loli.net/2017/11/10/5a0598f2274bc.png)
#### 方法: 
- str.split() 每次处理一种分隔符
```
def mySplit(s, ds):
    res = [s]
    for d in ds:
        t = []
        map(lambda x:t.extend(x.split(d)), res)
        res = t
    return [x for x in res if x] # 不是直接返回res 是因为可能会有空格
s = 'dah,asdlajsd:asda|sadasdas;'
print(mySplit(s, ',:|;'))
```
- re.split() 正则表达式
```
re.split(r'[,:|;]+', s)
# 若是处理单个分隔符应该使用 s.split() 因为速度更快
```

## 4-2 如何判断字符串a是否以字符串b开头或结尾
![4-2.png](https://i.loli.net/2017/11/10/5a0594c2d04e1.png)
#### 方法: 
- 使用 str.startswith() 和 str.endswith()
```
s = 'index.py'
s.endswith('.py') # True
s.endswith(('.py', '.sh')) # True 参数只能是元组不能是列表
[name for name in os.listdir('.') if name.endswith(('.py', '.sh'))]
oct(os.stat('index.py').st_mode) # 将权限值转为8进制
os.chmod('index.py', os.stat('index.py').st_mode | stat.S_IXUSR)
```

## 4-3 如何调整字符串中文本的格式 
![4-3.png](https://i.loli.net/2017/11/10/5a0596dbabee8.png)
#### 方法: 
- 使用 re.sub() 替换
```
f = open('test.txt').read()
re.sub('(\d{4})-(\d{2})-(\d{2})', r'\2/\3/\1', f) # 后面的\1表示 re 匹配到的组
# re.sub('(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})', r'\g<month>/\g<day>/\g<year>', f)
```

## 4-4 如何将多个小字符串拼接成一个大的字符串
![4-4.png](https://i.loli.net/2017/11/10/5a059944818f3.png)
#### 方法: 
- 使用 '+' 拼接
```
s = ['adasda', 'asda', 'ewrer']
p = ''
for i in s:
    p += i
```
- str.join()
```
';'.join(['a', 'b', 'c']) # 'a;b;c'
s = ['adasda', 'asda', 'ewrer']
'.'join(s)

l = ['adasda', 123,'asda', 'ewrer']
''.join(str(i) for i in l) # 不要使用列表 ''.join([str(i) for i in l])
```

## 4-5 如何对字符串进行左, 右, 居中对齐
![4-5.png](https://i.loli.net/2017/11/10/5a059b2abf26c.png)
#### 方法: 
- 使用 str.ljust() str.rjust str.center() 进行左右对齐
```
s = 'abc'
s.ljust(10) # 'abd       '
s.ljust(10, '=') # 'abd======='
```
- format()
```
format(s, '<10') # 'abd       '
format(s, '>10') # '       abd'
format(s, '^10') # '   abd    '
```
```
d = {
    'a':123,
    'ba123asdd':345,
    'cfghf':67
}
w = max(map(len, d.keys()))
for k in d:
    print(k.ljust(w)+': '+str(d[k]))
# a        : 123
# ba123asdd: 345
# cfghf    : 67
```

## 4-6 如何去掉字符串中不需要的字符
![4-6.png](https://i.loli.net/2017/11/10/5a059d48a3ce1.png)
#### 方法:
- strip() 去掉两端空白 lstrip() 去掉左端  rstrip() 去掉右端 
```
s = '     asd   123    '
s.strip() # 'asd   123'
s = '+++    asd   123  +++'
s.strip('+') # '    asd   123  '
```
- 删除固定位置字符 可以使用切片 + 拼接的方法
```
s = 'ads:123'
s[:3] + s[4:]
```
- str.replace() 或者 re.sub()
```
s = '\t123\tasd\tuio'
s.replace('\t', '')
```
- str.translate()
```
s = 'abc123xyz'
import string
# string.maketrans('abcxyz', 'xyzabc') 生成一个映射表
s.translate(s.maketrans('abcxyz', 'xyzabc')) # 'xyz123abc'
```
![4-6-4.png](https://i.loli.net/2017/11/10/5a05a1e9146c2.png)






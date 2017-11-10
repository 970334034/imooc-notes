# Python高效编程技巧实战
![](http://img.mukewang.com/szimg/59f7e6c600014f2020000520.jpg)

> 人生苦短, 我用Python.

### 详细课程请往 [慕课网](http://coding.imooc.com/class/chapter/62.html) 学习 :wind_chime:

# 第二章 数据结构与算法进阶训练

## 2-1 如何在列表,字典, 集合中根据条件筛选数据
### 过滤列表的负数 
`data = [randint(-10, 10) for _ in range(10)] # [5, 5, -7, 4, 8, 8, 0, -8, 1, -6]`

#### 方法:
1. `filter(lambda x:x > 0, data)`
2. `[x for x in data if x >= 0]`

### 筛出字典某些元素
```
stu = {x : randint(60, 101) for x in range(1, 21)} 
# {1: 90, 2: 83, 3: 96, 4: 79, 5: 100, 6: 61, 7: 76, 8: 95, 9: 60, 10: 99, 11: 68, 12: 88, 13: 90, 14: 69, 15: 60, 16: 89, 17: 80, 18: 96, 19: 73, 20: 91}
```
#### 方法:
- `{k: v for k, v in stu.items() if v >= 90}`

### 筛出集合中某些元素
`s = set(data) # data为上面生成的列表`

#### 方法:
- `{x for x in s if s % 3 == 0}`

## 2-2 如何为元组中的每个元素命名, 提高程序可读性
`stu = ('Jim', 16, 'male', 'jim@gmail.com')`
#### 方法:
1. `name, age, sex, mail = range(4) # 访问: stu[name]`
2. collections.namedtuple
```
Student = namedtuple('Student', ['name', 'age', 'sex', 'mail'])
s = Student('Jim', 16, 'male', 'jim@gmail.com')
s.name # 'Jim'
isinstance(s, tuple) # True
```

## 2-3 如何统计序列中元素的出现频度
### 随机序列出现次数最多的3个数
#### 方法:
- collections.Counter
```
data = [randint(0, 10) for _ in range(30)] 
# [1, 9, 1, 9, 4, 7, 8, 3, 4, 6, 3, 9, 0, 9, 2, 2, 6, 9, 8, 1, 4, 5, 7, 0, 5, 8, 3, 9, 0, 9]
c  = Counter(data) 
c.most_common(3) # [(9, 7), (0, 3), (1, 3)]
```

### 对一英文文本进行单词词频统计, 找到频率最高的10个单词
#### 方法: 
- collections.Counter
```
txt = open('test.txt').read()
c = Counter(re.split('\W+', txt)) # 分割
c.most_common(10)
```

## 2-4 如何根据字典中值的大小, 对字典中的项排序
{'张三':89, '李四': 98, ...}
#### 方法: 
1. 利用 zip 函数, 将字典改成值在前, 键在后(即 成绩在前, 名字在后) 
```
d = {x:randint(60, 100) for x in 'xyzabc'}
sorted(zip(d.values(), d.keys()), reverse = True)
```

2. 传递 sorted 函数的 key 参数
```
sorted(d.items(), key = lambda x:x[1])
```

## 2-5 如何快速找到多个字典中的公共键(key) 
{'a':1, 'b':1}, {'b':1, 'c':2}, {'a':1, 'd':2}...
#### 方法:
- 利用集合(set)的交集操作
```
from random import randint, sample
s1 = {x: randint(1, 4) for x in sample('abcdefg', randint(3, 6))}
s2 = {x: randint(1, 4) for x in sample('abcdefg', randint(3, 6))}
s3 = {x: randint(1, 4) for x in sample('abcdefg', randint(3, 6))}
s1.keys() & s2.keys() & s3.keys() # 得到交集
# 若是有 n 个集合
map(dict.keys, [s1, s2, s3...]) 
from functools import reduce # python3
reduce(lambda a, b:a & b, map(dict.keys, [s1, s2, s3...]))
# m = map(dict.keys, [s1, s2, s3]) m 是 map 对象, list(m)对其访问
```

## 2-6 如何让字典保持有序
#### 方法:
- collections.OrderedDict
```
d = {}
d['Jim'] = (1, 35)
d['Tom'] = (2, 37)
d['Bob'] = (3, 42)
for k in d: print(k) 
# Jim  Bob  Tom 并不是按照进入字典序列打印
from collections import OrderedDict
d = OrderedDict()
d['Jim'] = (1, 35)
d['Tom'] = (2, 37)
d['Bob'] = (3, 42)
for k in d: print(k) 
# Jim Tom Bob
```

## 2-7 实现用户的历史记录功能
### 猜字游戏, 显示之前输入的数
#### 方法:
- collections.deque 双端循环队列, 使用pickle存储python对象, 以便下次加载
```
q = deque([], 5) # 容量为5
q.append(4)
import pickle
pickle.dump(q, open('history', 'w'))
q2 = pickle.load(open('history'))
```

# 第三章 对象迭代与反迭代技巧训练
## 3-2 如何实现可迭代对象和迭代器对象
### 从网络抓取城市气温信息并显示
#### 方法: 
- collections.Iterable, Iterator
```
class WeatherIterator(Iterator):
    def __init__(self, cities):
        self.cities = cities
        self.index = 0
    def getWeather(self, city):
        '''返回 city 城市天气信息'''
        '''如: 北京: 最高气温: xx°C, 最低气温: xx°C.'''
    def next(self):
        if self.index == len(self.cities):
            raise StopIteration
        city = slef.cities[self.index]
        self.index += 1
        return self.getWeather(city)
class WeatherIterable(Iterable):
    def __init__(self, cities):
        self.cities = cities
    def __iter__(self):
        return WeatherIterator(self.cities)
for x in WeatherIterable(['北京', '武汉', ...]):
    print(x)
```

## 3-3 如何使用生成器函数实现可迭代对象 
### 实现一个可迭代对象的类, 它能迭代出给定范围内所有素数
#### 方法:
- yield
```
class PrimeNumber:
    def __init__(self, start, end):
        self.start = start
        self.end = end
    def isPrime(self, k):
        for i in range(2, int(sqrt(k) + 1)): # math.sqrt
            if k % i == 0
                return False
            return True
    def __iter__(self):
        for k in range(self.start, self.end+1):
            if self.isPrime(k):
                yield k
for x in PrimeNumber(1, 100):
    print(x)
```

## 3-4 如何进行反向迭代以及如何实现反向迭代
### 实现一个连续的浮点数发生器, 根据给定的范围和步长产生一系列的浮点数(反向)
#### 方法:
- reversed()
```
class FloatRange:
    def __init__(self, start, end, step=0.1):
        self.start = start
        self.end = end
        self.step = step
    def __iter__(self):
        t = self.start
        while t <= self.end:
            yield t
            t += self.step
    def __reversed__(self):
        t = self.end
        while t >= self.start:
            yield t
            t -= self.step
for x in FloatRange(1, 5, 0.5):
    print(x)
```

## 3-5 如何对迭代器做切片操作
### 有某个文本文件, 我们想读取其中某范围的内容, 如100~300行之间的内容( python中文本文件是可迭代对象)
#### 方法:
- itertools.islice
```
f = open('test.txt')
islice(f, 100, 300) 
# islice(f, 100, -100) 不支持负索引
```

## 3-6 如何在一个 for 语句中迭代多个可迭代对象
### 学生各科成绩分别存储在各个对应列表中, 同时迭代这些列表, 计算每个学生的总成绩
#### 方法:
- 利用 zip() 将多个可迭代对象合并成一个列表, 每一项是一个元祖
```
total = []
chinese = [...]
math = [...]
english = [...]
for a, b, c in zip(chinese, math, english):
    total.append(a+b+c)
```

### 某年级4个班, 某次英语考试成绩存在4个列表中, 统计成绩高于90的人数
- itertools.chain
```
e1 = [...]
e2 = [...]
e3 = [...]
e4 = [...]
count = 0
for i in chain(e1, e2, e3, e4):
    if i > 90:
        count += 1
```










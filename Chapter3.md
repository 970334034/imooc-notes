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
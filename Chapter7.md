# 第7章 类与对象深度技术进阶训练
## 7-1 如何派生内置不可变类型并修其改实例化行为 
![7-1.png](https://ooo.0o0.ooo/2017/11/12/5a082c664e9cd.png)
```
class IntTuple(tuple):
    def __new__(clas, iterable):
        g = (x for x in iterable if isinstance(x, int))
        return super(IntTuple, clas).__new__(clas, g)
    def __init__(self, iterable):
        super(IntTuple, self).__init__()

a = IntTuple([1, 2, 'a', {'a':1}]) # (1, 2)
```
## 7-2 如何为创建大量实例节省内存 
![7-2.png](https://ooo.0o0.ooo/2017/11/12/5a082d29184ef.png)
```
class PLayer1(object):
    def __init__(self, uid, name, status = 0, level = 1):
        self.uid = uid
        ...
class PLayer2(object):
    __slots__ = ['uid', 'name', 'status', 'level']
    def __init__(self, uid, name, status = 0, level = 1):
        self.uid = uid
        ...
p1 = PLayer1(...)
p2 = PLayer2(...)
# p1占用更多内存空间是因为有 __dict__ 属性
# 这个属性是个字典, 保存了所有的属性, 同时也保证可以动态添加属性
# 定义了 __slots__ 就没有 __dict__ 属性 也就不能动态添加属性了
import sys
sys.getsizeof(p1)
sys.getsizeof(p2)

```

## 7-3 如何让对象支持上下文管理 
![7-3.png](https://ooo.0o0.ooo/2017/11/12/5a0830946e89d.png)
![7-3-su.png](https://ooo.0o0.ooo/2017/11/12/5a0830aaa2f3f.png)

## 7-4 如何创建可管理的对象属性 
![7-4.png](https://ooo.0o0.ooo/2017/11/12/5a083338a17aa.png)
```
class Cirle(object):
    def __init__(self, radius):
        self.radius = radius
        
    def getRadius(self):
        return self.radius

    def setRadius(self, val):
        if not isinstance(val, (int, long, float)):
            raise ValueError('wrong type.')
        self.radius = float(val)
    R = property(getRadius, setRadius)
```

## 7-5 如何让类支持比较操作 
![7-5.png](https://ooo.0o0.ooo/2017/11/12/5a0833ccd34f7.png)
```
class Rectangle(object):
    def __init__(self, w, h):
        self.w = w
        self.h = h
    def area(self):
        return self.w * self.h
    def __lt__(self, obj):
        return self.area() < obj.area()
    def __eq__(self, obj):
        return self.area() == obj.area()
    def __le__(self, obj):
        ...
t1 = (2, 3)
t2 = (5, 3)
t1 <= t2 # True
```
```
from functools import total_ording
@total_ording
class Rectangle(object):
    def __init__(self, w, h):
        self.w = w
        self.h = h
    def area(self):
        return self.w * self.h
    def __lt__(self, obj):
        return self.area() < obj.area()
    def __eq__(self, obj):
        return self.area() == obj.area()
t1 = (2, 3)
t2 = (5, 3)
t1 <= t2 # True
```

## 7-6 如何使用描述符对实例属性做类型检查 
![7-6.png](https://ooo.0o0.ooo/2017/11/12/5a08360608a5f.png)
![7-6-1.png](https://ooo.0o0.ooo/2017/11/12/5a08385ebe677.png)
![7-6-2.png](https://ooo.0o0.ooo/2017/11/12/5a0838571681a.png)

## 7-7 如何在环状数据结构中管理内存 
![7-7.png](https://ooo.0o0.ooo/2017/11/12/5a083a391ba5a.png)
![7-7-1.png](https://ooo.0o0.ooo/2017/11/12/5a083a389cad4.png)

## 7-8 如何通过实例方法名字的字符串调用方法
![7-8.png](https://ooo.0o0.ooo/2017/11/12/5a083af737ff4.png)
![7-8-1.png](https://ooo.0o0.ooo/2017/11/12/5a083b66b245d.png)
![7-8-2.png](https://ooo.0o0.ooo/2017/11/12/5a083b662a13a.png)
![7-8-3.png](https://ooo.0o0.ooo/2017/11/12/5a083bb992337.png)
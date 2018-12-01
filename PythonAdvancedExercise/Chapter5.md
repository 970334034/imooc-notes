# 第五章 文件I/O高效处理技巧训练

## 5-1 如何读写文本文件
![5-1.png](https://i.loli.net/2017/11/11/5a06ba44bfd71.png)

## 5-2 如何处理二进制文件
![5-2.png](https://i.loli.net/2017/11/11/5a06c21b3c35f.png)
#### wav格式说明: 
![wav](https://ss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/u=3372252489,759389733&fm=27&gp=0.jpg)
```
f = open('demo.wav', 'rb')
info = f.read(44)
import struct
struct.unpack('h', '\x01\x02') # 小端 513
struct.unpack('>h', '\x01\x02') # 大端 258
channels = struct.unpack('h', info[22:24]) # 2
import array
f.seek(0, 2)
n = (f.tell() - 44)/2 
buf = array.array('h', (0 for _ in range(n)))
f.seek(44)
f.readinto(buf)
f.close()
```
![seek.png](https://i.loli.net/2017/11/11/5a06bdd140738.png)
```
# 修改wav文件
for i in range(n):
    buf[i] /= 8
f2 = open('demo2.wav', 'wb')
f2.write(info)
buf.tofile(f2)
f2.close()
```

## 5-3 如何设置文件的缓冲
![5-3.png](https://i.loli.net/2017/11/11/5a06c34284016.png)
```
f = open('demo.txt', 'w', buffering = 2048) # 全缓冲
f.write('x' * 2050)

f = open('demo.txt', 'w', buffering = 1) # 行缓冲
f.write('abc')
f.write('\n')

f = open('demo.txt', 'w', buffering = 0) # 无缓冲
f.write('a')
```

## 5-4 如何将文件映射到内存
![5-4.png](https://i.loli.net/2017/11/11/5a06c4d920eca.png)
```
import mmap
f = open('demo.bin', 'r+b') # demo.bin 为一个大小为1m, 内容为全0的文件
m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
m[0] # '\x0'
m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE, offset = mmap.PAGESIZE*8)
m[:0x1000] = '\xaa' * 0x1000
```

## 5-5 如何访问文件的状态 
![5-5.PNG](https://i.loli.net/2017/11/11/5a06d5d954231.png)
```
import os
os.stat('a.txt')
os.lstat('a.txt')
f = open('a.txt')
os.fstat(f.fileno())
import stat
s = os.stat('a.txt')
stat.S_ISDIR(s.st_mode) # False
# 访问权限
s.st_mode & stat.S_IXUSR
s.st_mode & stat.S_IXGRP
s.st_mode & stat.S_IXOTH
# 三个时间
import time
time.localtime(s.st_atime) # s.st_mtime s.st_ctime
# 大小
s.st_size # 字节
```
```
import os
os.path.isdir('a.txt') # False
os.path.isfile('a.txt') # True
# 三个时间
os.path.getatime('a.txt') # getmtime getctime
```
## 5-6 如何使用临时文件
![5-6.png](https://i.loli.net/2017/11/11/5a06d609775c5.png)
```
f = TemporaryFile() # 在系统路径中找不到
f.write("abcd"*1000)
f.seek(0)
f.read(10)
f = NamedTemporaryFile() # 在系统路径中可找到
f.name
# 关闭之后自动删除
f = NamedTemporaryFile(delete = False) # 不自动删除
```











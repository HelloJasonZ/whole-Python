# -*- coding: utf-8 -*-
# @Author: 28906
# @Date:   2017-08-31 10:03:51
# @Last Modified by:   cbbfcd
# @Last Modified time: 2017-09-03 18:58:24

## 简单的一些标准库的使用

# 文件通配符
import glob
files = glob.glob('*.py')
print(files)
#['chapter1.py', 'chapter2.py', 'chapter3.py', 'chapter4.py', 'chapter5.py', 
#'chapter6.py', 'chapter7.py', 'chapter8.py', 'chapter9.py', 'hello.py', '__init__.py']

# 标准输入 输出 和错误
import sys
# 下面这货等价于print
sys.stdout.write('hello\n') # hello
# 从控制台打印到文件
# __console__ = sys.stdout # 先记录下原始输出
# handler_f = open(r'E:\Python\PythonNotes\python基础\files\test.txt','a',encoding='utf-8')
# sys.stdout = handler_f
# print('aaaaaaaaaaaaaa')
# sys.stdout = __console__
# sys.exit()

# 日期操作
from datetime import date, timedelta
import time

now = date.today()
print('今年:{}'.format(now.year)) # 今年:2017
print(now) # 2017-08-31
print(now.strftime('%Y/%m/%d')) # 2017/08/31
yesterday = now - timedelta(days=1)
print(yesterday) # 2017-08-30

print(time.strftime('%H:%M:%S')) # 10:30:42

print(time.asctime(time.localtime())) # Sun Sep  3 18:55:55 2017
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())) # 2017-09-03 18:57:00

# 月历
import calendar
print(calendar.month(2017,9))
#    September 2017
# Mo Tu We Th Fr Sa Su
#              1  2  3
#  4  5  6  7  8  9 10
# 11 12 13 14 15 16 17
# 18 19 20 21 22 23 24
# 25 26 27 28 29 30


# 数据打包和压缩
import gzip
content = b'hello every one!'
with gzip.open(r'E:\Python\PythonNotes\python基础\files\test3.txt.gz','wb') as f:
	f.write(content)


# 性能测试
from timeit import Timer

t1 = Timer('t=a; a=b; b=t', 'a=1;b=2').timeit()
t2 = Timer('a,b = b,a', 'a=1;b=2').timeit()
faster = 't1' if t1 < t2 else 't2'
print('faster:{}'.format(faster)) # faster:t2

# 一个方法供test.py 测试

def aver(*args):
	return sum(args)/len(args)
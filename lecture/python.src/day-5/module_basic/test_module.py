#!/usr/bin/env python
# coding: utf-8

# In[2]:


# 모듈 작성
PI = 3.141592

def number_input():
    output = input('숫자 입력 :')
    return float(output)

def get_circum(radius):
    return radius * 2 * PI

def get_circle_area(radius):
    return PI * radius * radius
if __name__ == '__main__':
    print('get_circum(5) : ', get_circum(5))
    print('get_circle_area(5) : ', get_circle_area(5))
print("모듈의 __name__ : ",__name__)


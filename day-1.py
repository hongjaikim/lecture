#!/usr/bin/env python
# coding: utf-8

# In[2]:


# 키워드 확인
import keyword

print(keyword.kwlist)


# In[3]:


keyword.kwlist = 10


# In[ ]:





# In[4]:


print("test", '20 + 30 =', 20+30)


# In[5]:


print("test", '20 + 30 =', 20+30, sep='\t')


# In[ ]:





# In[ ]:





# In[7]:


# 하나만 출력합니다.
print("# 하나만 출력합니다.")
print("Hello Python Programing")
print()

# 여러 개를 출력합니다.
print("# 여러 개를 출력합니다.")
print(10, 20, 30, 40, 50)
print("안녕하세요", "저의", "이름은", "김홍재입니다!")
print()

# 아무것도 입력하지 않으면 단순하게 줄바꿈합니다.
print("# 아무것도 출력하지 않습니다.")
print("--- 확인 전용선--- ")
print()
print()
print("--- 확인 전용선 ---")



# In[ ]:





# In[ ]:


# 키워드 import keyword -> keyword.keylist 에서 확인
# 식별자 : 문자 시작, _ 가능, 숫자 시작 안됨, 공백 안됨, 키워드 안됨
# 식별자들 작성 규칙 : 캐멀(클래스), 스네이크( 변수, 함수), 함수는 ()


# ## chaptor 02 자료형
# ### 01 자료형과 문자열

# In[15]:


# python의 자료형은 : 문자열, 숫자, 불(T/F) 타입으로 세가지만 존재
print('문자열의 데이터 타입 : ', type('문자열'))
print('숫자의 데이터 타입 정수/소수 : ', type(10), "/", type(10.4))
print('불리언의 데이터 타입 : ', type(True))


# In[ ]:





# In[19]:


# 이스케이프 문자를 활용하여 문자열 만들기 : \" -> 일반 문자 "
# \t : 탭, \n : 뉴라인
print('\' 안녕하세요 !! \'')
print("\\ \\ \\ ")
print("이름\t나이\t지역")
print("안녕\n안녕")


# In[20]:


# 여러 라인의 문자를 출력하기
print("1라인\n2라인")
print()
print('''1라인
2라인''')


# In[21]:


# 명령어가 1라인 이상으로 길어질 때 \
print('\' 안녕하세요 !! \'           ')


# In[ ]:


# 문자열 연산자, 문자열 자르기, 문자열 길이 구하기
# 문자열 + 문자열 -> 이어붙이기
# 문자열 * 숫자 -> 숫자만큼 문자열 반복


# In[22]:


print("안녕" + '하세요')


# In[23]:


print(3*'안녕하세요')


# In[ ]:





# In[34]:


# 문자열 자르기 : 문자열[시작인덱스 : 마지막인덱스] -> 시작은 포함, 마지막은 미포함
hello='안녕하세요'

#전체 문자열 길이 : len(hello)
print(len(hello))

#처음 문자와 마지막 문자 출력
print(hello[0], hello[-1])

#처음 2글자 출력
print(hello[:2])

#2번째 문자와 3번째 문자 출력
print(hello[1:3])

#3번째 문자부터 끝까지 출력
print(hello[3:])


# In[35]:


# 문자열의 길이를 구해서 마지막 문자 출력

hello="안녕하세요"
print(hello[len(hello)-1])


# ### 02 숫자

# In[ ]:


###
#숫자 연산자 // : 몫 (나머지 버림), % : 나머지, ** : 거듭제곱


# In[36]:


# 시프트L : 라인넘버 표시


# In[ ]:





# ### 3.변수의 활용

# In[45]:


var_a = 10
var_a

var_b = 20
var_b


# In[49]:


# 복합 대입 연산자
# += -= *= /= %= **= 활용
# a += b -> a = a + b
# 문자열도 가능
# 사칙연산자랑 대입연산자 사이에 띄어쓰기 불가


# In[52]:


# input() -> 사용자가 입력하는 함수 (문자로 인식)(괄호안에 설명문)


# In[58]:


# 숫자를 입력햇 변수에 저장 후 변수의 데이터 타입을 확인해 보세요
asd = input("숫자를 입력하세요 : ")
print(type(asd))
print(type(int(asd)))


# In[72]:


# 데이터 타입 변경 int(), float(), str()


# ### 4. 숫자와 문자열의 다양한 기능

# In[105]:


# 문자열.format()
# 중괄호로 형식을 만들고 포맷으로 문자열로 간단하게 대입
"{} {}".format(10,str)
"{} + {} = {}".format(1,2,3)


# In[106]:


#정수 출력에서 format() 함수 활용
print("{}".format(52))
print("{:d}".format(52))
print("{:5d}".format(52))
print("{:05d}".format(52))
print("{:05d}".format(-52))


# In[116]:


# 기호와 함께 출력
print("{:+d}".format(-52))
print("{:+d}".format(52))

print("{: d}".format(52))
print("{: d}".format(-52))

print("{:+5d}".format(-52))     # 부호와 함께 표현
print("{:+5d}".format(52))      

print("{:=+5d}".format(52))          #부호를 앞으로 밀기
print("{:=+5d}".format(-52))

print("{:5.2f}".format(52.12345))      #소수점 2자리 표현
print("{:10f}".format(52.12345))       #실수 표현

print("{:g}".format(52.0))       #의미없는 소수점 버리기


# In[124]:


# 두 개의 숫자를 입력 받아 두 수의 합과 곱, 차, 나머지 값을 다음의 형식으로 출력
# 1. 입력 받은 두 수는 10, 20
# 2. 입력 받은 두 수 10과 20의 합은 30
# 3. 입력 받은 두 수 10과 20의 곱은 200
# 4. 입력 받은 두 수 10과 20의 차는 -10
# 5. 입력 받은 두 수 10과 20의 나눈 나머지는 10
asd1 = int(input("첫 번째 수를 입력하세요"))
asd2 = int(input("두 번째 수를 입력하세요"))
qwe = "입력 받은 두 수"
print("{}는 {}, {}".format(qwe,asd1,asd2))
print("{} {}과 {}의 합은 {}".format(qwe,asd1,asd2,asd1+asd2))
print("{} {}과 {}의 곱은 {}".format(qwe,asd1,asd2,asd1*asd2))
print("{} {}과 {}의 차는 {}".format(qwe,asd1,asd2,asd1-asd2))
print("{} {}과 {}의 나눈 나머지는 {}".format(qwe,asd1,asd2,asd1%asd2))


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:






# coding: utf-8

# # 사칙연산 & 비교 연산

# In[ ]:


1+1


# In[4]:


7-4


# In[8]:


3*4


# In[1]:


3/2


# In[9]:


3/4 
# 파이썬 3부터는 실수 변환 할 필요 없다. 


# In[11]:


13%5


# In[12]:


1+2==3


# In[13]:


1+2!=3


# In[16]:


1+2<4


# In[15]:


1+2>4


# In[17]:


1+2<=4
1+2>=4


# In[18]:


10%2==0


# In[19]:


12%2 ==0 and 12% 3==0


# In[20]:


12%2 ==0 and 14% 3==0


# In[10]:


12%2 ==0 or 14% 3==0


# # 제곱

# In[13]:


a = 3
b = 4
a **b


# In[16]:


# 나눗셈 후 소수점 아랫자리 버리는 연산자 *음수 계산시 주의
print(7/4)
print(7//4)
print(-7/4)
print(-7//4)


# # 주석

# In[5]:


# 주석
"""파이썬의 확장자는 py"""


# ## 변수

# In[22]:


a=3
b=5
a+b


# In[24]:


a=3
a=a+1
a


# In[25]:


a,b = 1,2


# In[26]:


a


# In[27]:


b


# In[28]:


#int == integer ==정수형
# str == string == 문자열


# In[29]:


Hello World


# In[30]:


"Hello World"


# In[31]:


## 쌍따옴표를 쓰지 않으면 예약어(변수)로 인식..... 


# In[32]:


# 쌍따옴표, 홑따옴표....문자열안에 따옴표에 따라 에러. 


# In[33]:


"Shayne's Weight?"


# In[34]:


1=="1"


# In[36]:


'shayne\'s Weight?'


# # 숫자

# In[7]:


# 8진수
a = 0o117
# 16진수
b = 0x8ff


# In[9]:


#연습문제
sections = ["국어", "영어","수학"]
scores = [80, 75, 55]


for section in sections :
    print(section)
    
print("의 평균은")

sum = 0
for score in scores :
    sum = sum+score
    

print(sum / len(sections))


# # 문자형

# In[11]:


"a" 'b' """C"""'''D'''


# In[27]:


print("1. \힝""\\'힝 \n 힝")
print("""힝
힝
""")


# In[30]:


a = "Python" 
print(a*2)


# In[32]:


a = "="
b = "\n"
c="Python"  
print(a*20 +b +c+b+a*20)


# In[43]:


a = "abcdefg"

print(a[-3])
print(a[0:-3])
print(a[:])
print(a[:1])


# In[46]:


"I eat %d %s apples." % (5,"five")


# In[51]:


"I eat {0} apples, {1} cans and {aaa}".format("five", 6, aaa="others")


# In[54]:


print("{0:>10}".format("hi"))
print("{0:<10}".format("hi"))
print("{0:^10}".format("hi"))
print("{0:=^10}".format("hi"))


# In[55]:


"test".count("t")


# In[59]:


print("Python is the best choice".find('o'))
print("Python is the best choice".find('z')) #없을떄
print("Python is the best choice".index('o'))
print("Python is the best choice".index('z')) #없을떄


# In[61]:


a=",b"
a.join('abcd')


# In[64]:


print(a.upper())
a.upper().lower()


# In[68]:


a = "    hi  "
print(a.rstrip())
print(a.strip())
print(a.replace("hi", "hellow"))


# In[69]:


a = "Life is too short"
a.split()


# In[74]:


a = [1, 2, 3, ['a', 'b', 'c']]
print(a[3])
print(a[:4])
print(a*3)


# In[75]:


del a[0]
a


# In[79]:


A = [1,2,3,4]
A.insert(3,9)
print(A)
A.remove(3)
print(A)
print(A.pop())  


# In[83]:


a = [1,2,3]
a.extend([4,5])
print(a)
a += [6,7]
a


# ### 튜플

# In[85]:


# 리스트와 유사, 값이 변하지 않음
t1 =()
t2= (1, 2,3,)   # 항상 값이 변하지 않음
del t2[0]   # 오류


# ### 딕셔너리

# In[97]:


dic = {'name':'pey', 'phone':'0119993323', 'birth': '1118'}
print("1" , dic.keys())
print("2" ,dic.values())
print("3" ,dic.items())
print("4" ,dic.get("name"))
print("5" ,dic.get("name222")) #Nome
print("6" ,dic.clear())
print("7" ,"name" in dic)


# ### 집합자료형

# In[109]:


# 중복을 허용하지 않는다. 순서가 없다.  교집합, 합집합, 차집합으로 이용... 왜안되지??
s1 = set([1, 2])
print(set1)
list1 = list(set1)
print(liset1)
tuple1 = tuple(liset1)
print(tuple1)
# add , update, remove


# # 불(bool) - 직관적

# In[38]:


True


# In[39]:


False


# In[40]:


True ==1


# In[41]:


False ==0


# In[43]:


True =="True"


# In[44]:


#문자열 + 숫자는   에러
1+"2"


# In[48]:


#기본적으로 마지막게 출력
print(a)
b=3


# In[50]:


message = "Hello World!"
message


# In[51]:


message[0]


# message[2]

# In[57]:


# indexing
message[-2]


# In[59]:


# slicing 0~3
message[0:4]


# "H" in message
# 

# In[60]:


"H" in message


# In[62]:


#대소문자 반드시 구별
"h" in message


# In[63]:


#method
message.upper()


# In[64]:


message.lower()


# In[66]:


odd = [1,3,5,7,9]
odd


# In[69]:


print(odd[0])
print(odd[-1])
print(odd[0:4])
print(1 in odd)
print(2 in odd)


# In[71]:


# odd  + . + tab
odd.append(11)
odd


# In[78]:


odd.reverse()
odd


# In[81]:


odd.insert(2,6)
odd


# In[99]:


# 파이썬은 들여쓰기 중요 **   File "<ipython-input-82-9c2a722e5762>", line 5
# 반복문의 범위

age = 3

if age <5:
    print("아이")
else :
    print("어른")


# In[87]:


age = 10

if age < 5:
    print("아이")
elif age < 18:
    print("학생")
else :
    print("어른")


# ### 반복문

# In[90]:


basket = ['apple', 'banana', 'chicken', 'pineapple','cherry']


for product in basket : 
    print(product)

#print(basket[1])
#print(basket[2])
#print(basket[3])
#print(basket[4])


# In[93]:


for i in range(5):
    print(i)


# In[94]:


for i, product in enumerate(basket):
    print(i,product)


# In[98]:


for i in range(1,10):
    if i==5:
        print("bang!")
    print(i)


# In[101]:


# 뛰어쓰기 중요
for i in range(1,10):
    if i==5:
        print("bang!")
        print(i)
print("complete!")


# In[102]:


# break
for i in range(1,10):
    if i==5:
        print("bang!")
        break
    print(i)
print("complete!")


# In[104]:


#continue
for i in range(1,10):
    if i == 2:
        print("beep!")
        continue
    elif i== 5:
        print("bang!")
        break
    print(i)
print("complete!")


# In[108]:


double_list = []
for i in range(10):
    if i ==5:
        continue
    elif i == 8:
        break
        
    double = i * 2
    double_list.append(double)
    
double_list


# In[111]:


double_list = []
for i in range(1,11):
    if i ==5:
        continue
    elif i == 8:
        break
        
double = i * 2
double_list.append(double)
double_list


# In[112]:


i


# ### 함수

# In[113]:


# 코드 중복....
# def == define  함수 만들 떄 예약어
def multiply(a,b):
    c = a * b
    return c


# In[114]:


multiply(2,3)


# In[110]:


a = input()


# In[111]:


a


# In[112]:


number = input("숫자를 입력하세요: ")


# In[113]:


number


# In[114]:


print("life" "is" "too short") 
print("life", "is", "too short")


# In[ ]:


f = open("새파일.txt", 'w')  # w : 쓰기  , r : 읽기, a :마지막에 새로운내용 추가


f.readline()  # \n 포함 리스트

f.read()      # 파일전체를 문자열로 리턴

f.write("추가합니다. ")

f.close()


# In[ ]:


import sys


args = sys.argv[1:]

for i in args:

    print(i)


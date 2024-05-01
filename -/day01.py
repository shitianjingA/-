#!/usr/bin/env python
# coding: utf-8

# In[3]:


import random#随机数0-1
for i in [1,2,3,5,6,7,8,9,10]:
    m_i=random.random()
    print(m_i)


# In[4]:


import matplotlib#数据可视化


# In[5]:


x=[1,2,3,4,5,6]
y=[2,3,4,5,6,7]
print(x,y)


# In[9]:


from matplotlib import pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
figl=plt.figure(figsize=(5,5))#figure图形实例实例 figsize图形大小
plt.plot(x,y)
plt.title('y vs x')
plt.xlabel('x')
plt.ylabel('y')
plt.show()


# In[10]:


fig2=plt.figure(figsize=(5,5))#figure图形实例实例 figsize图形大小
plt.scatter(x,y)
plt.title('y vs x')
plt.xlabel('x')
plt.ylabel('y')
plt.show()


# In[11]:


import numpy as np#数组运算


# In[19]:


a=np.eye(5)#对角线为1的矩阵
print(type(a),a)


# In[20]:


b=np.ones(5)#默认一行
print(b)


# In[22]:


b=np.ones([5,5])
print(b)
print(b.shape)#查看维度


# In[23]:


c=a+b
print(c)


# In[4]:


import pandas as pd#DataFrame数据表格类型，打开表格pandas保存数据
data=pd.read_csv('text.csv')
print(type(data))
print(data)


# In[5]:


x=data.loc[:,'x']#所有行loc定位数据
print(x)
print(type(x))#Series序列类型   y同理


# In[6]:


d=data.loc[:,'y'][x < 10]#x < 10  y的值

print(d)


# In[41]:


data_array=np.array(data)
print(data_array)
print(data_array)#转化为数组


# In[7]:


data_new=data +10
print(data_new)
data_new.head()#部分数据


# In[8]:


#保存数据
data_new.to_csv('text1.csv',index=None)#index=None去掉索引


# In[ ]:





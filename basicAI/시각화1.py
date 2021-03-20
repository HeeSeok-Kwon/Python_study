#!/usr/bin/env python
# coding: utf-8

# In[1]:


a = [242, 256, 237, 223, 263, 81, 46]
print('A = ',a)


# In[2]:


n = len(a)
my_sum = 0
my_avg = 0
i = 0

for i in range(0,n):
    my_sum += a[i]
    
my_avg = my_sum/n
print('Total Sum:', my_sum)
print("Total Average:",my_avg)


# In[3]:


pip install matplotlib


# In[70]:


import matplotlib as mpl
from matplotlib import pyplot as plt
from matplotlib import font_manager, rc
import warnings
warnings.filterwarnings('ignore')
# f_path = './NanumGothic.ttf'
# font_name = font_manager.FontProperties(fname=f_path).get_name()
# rc('font', family=font_name)
# plt.rcParams["font.family"]='NanumGothic'

x_data = ['MON','TUE','WED','THR','FRI','SAT','SUN']
# plt.title("일주일간 유동 인구수 데이터", fontsize=16)
# plt.xlabel("요일", fontsize=12)
# plt.ylabel("유동 인구수", fontsize=12)

plt.title("1 week floating population data", fontsize=16)
plt.xlabel("Day of the week", fontsize=12)
plt.ylabel("Floating population", fontsize=12)

plt.scatter(x_data, a)
plt.plot(x_data, a)
plt.show


# In[22]:


print('설정파일 위치: ', mpl.matplotlib_fname())


# In[33]:


import matplotlib.font_manager as fm
font_list = fm.findSystemFonts(fontpaths = None, fontext='ttf')

print(len(font_list))


# In[46]:


font_list


# In[39]:


f = [f.name for f in fm.fontManager.ttflist]
print(len(font_list))
f[:10]


# In[59]:


[(f.name, f.fname) for f in fm.fontManager.ttflist if 'Nanum' in f.name]


# In[55]:


get_ipython().system('apt -qq -y install fonts-nanum > /dev/null')
 
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
 
fontpath = '/usr/share/fonts/truetype/nanum/NanumBarunGothic.ttf'
font = fm.FontProperties(fname=fontpath, size=10)
fm._rebuild()
 
# 그래프에 retina display 적용
get_ipython().run_line_magic('config', "InlineBackend.figure_format = 'retina'")
 
# Colab 의 한글 폰트 설정
plt.rc('font', family='NanumBarunGothic') 


# In[56]:


get_ipython().system('apt-get update -qq')
get_ipython().system('apt-ger install fonts-nanum* -qq')


# In[71]:


weekday_size = 5
weekday_sum = 0
weekday_avg = 0

for i in range(0, weekday_size):
    weekday_sum += a[i]
    
weekday_avg = weekday_sum/weekday_size

print("Weekday Data=",a[0:5])
print("Weekday Sum:",weekday_sum)
print("Weekday Average:",weekday_avg)

plt.title("Weekday floating population data",fontsize=16)
plt.xlabel("Day of the week",fontsize=12)
plt.ylabel("Floating population",fontsize=12)

plt.plot(x_data,a)
plt.scatter(x_data[0:weekday_size],a[0:weekday_size], c='red',edgecolor='none',s=50)
plt.show()


# In[ ]:





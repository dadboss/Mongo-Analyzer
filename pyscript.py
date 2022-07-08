#!/usr/bin/env python
# coding: utf-8

# In[101]:


import pandas as pd
import matplotlib.pyplot as plt
f = open('out.txt','r')


# In[102]:


raw=f.readlines()
metadata=[]
num=0
clmn=[]


# In[103]:


for idx in range(len(raw)):
    row=raw[idx].split(',')
    for index in range(len(row)):
        row[index]=row[index].replace('"','')
    #print(row[0])
    if(row[0]=="Date/Time"):
         #print(row)  
         row[-1] = row[-1][:-1]
         df = pd.DataFrame(columns = clmn,data = metadata)
         df.to_csv('opt{}.csv'.format(num),index=False)
         clmn=row   
         num=num+1
    elif (row[0]==""):
        pass
    elif(row[0][0]=='-'):
            metadata=[]
    else:
        metadata.append(row)
df = pd.DataFrame(columns = clmn,data = metadata)
df.to_csv('opt{}.csv'.format(num),index=False)
       


# In[104]:


#Disk IOPS
dfx = pd.read_csv('opt1.csv')
dfx['Date/Time'] = pd.to_datetime(dfx['Date/Time'])
x = dfx['Date/Time']
y = dfx['iops']
plt.figure(figsize = (7,7))
plt.plot(x,y,label = 'iops')
plt.legend()
plt.title('IOPS')
plt.xlabel('Date/Time')
plt.ylabel('Values')
plt.xticks(rotation = 45)
plt.savefig('iops.png')


# In[105]:


#Ops Counters - 1
dfx = pd.read_csv('opt1.csv')
dfx['Date/Time'] = pd.to_datetime(dfx['Date/Time'])
x = dfx['Date/Time']
z = dfx['Insert']
w = dfx['Update']
v = dfx['Delete']
u = dfx['Getmore']
plt.figure(figsize = (7,7))
#plt.plot(x,y,label = 'query')
plt.plot(x,z,c='b',label = 'insert')
plt.plot(x,w,c='r',label = 'update')
plt.plot(x,v,c='g',label = 'delete')
plt.plot(x,u,c='m',label = 'getmore')
#plt.plot(x,t,c='m',label = 'command')
plt.legend()
plt.xlabel('Date/Time')
plt.ylabel('Values')
plt.xticks(rotation = 45)
plt.title('Operations Counter')
plt.savefig('OpsCounters1.png')


# In[106]:


#Ops Counters - 2
dfx = pd.read_csv('opt1.csv')
dfx['Date/Time'] = pd.to_datetime(dfx['Date/Time'])
x = dfx['Date/Time']
z = dfx['Query']
w = dfx['Command']
plt.figure(figsize = (7,7))
plt.plot(x,z,label = 'query')
plt.plot(x,w,c='r',label = 'command')
plt.legend()
plt.xlabel('Date/Time')
plt.ylabel('Values')
plt.xticks(rotation = 45)
plt.title('Operations Counter')
plt.savefig('OpsCounters2.png')


# In[107]:


#Latency
dfx = pd.read_csv('opt3.csv')
dfx['Date/Time'] = pd.to_datetime(dfx['Date/Time'])
x = dfx['Date/Time']
y = dfx['reads']
w = dfx['writes']
v = dfx['commands']
plt.figure(figsize = (7,7))
plt.plot(x,y,label = 'reads')
plt.plot(x,w,c='y',label = 'writes')
plt.plot(x,v,c='r',label = 'commands')
plt.legend()
plt.xlabel('Date/Time')
plt.title('Latency')
plt.ylabel('milliseconds',fontsize=15)
plt.xticks(rotation = 45)
plt.savefig('Latency.png')


# In[108]:


#WiredTigerCache
pd.options.mode.chained_assignment = None
dfx = pd.read_csv('opt5.csv')
dfx['Date/Time'] = pd.to_datetime(dfx['Date/Time'])
x = dfx['Date/Time']
y = dfx['Configured']
w = dfx['InCache']
v = dfx['DirtyBytes']
for i in range(len(y)):
    y[i]=y[i]/1000000000
for i in range(len(w)):
    w[i]=w[i]/1000000000
for i in range(len(v)):
    v[i]=v[i]/1000000000
plt.figure(figsize = (7,7))
plt.plot(x,y,label = 'MaxBytes Configured')
plt.plot(x,w,c='y',label = 'Currently InCache')
plt.plot(x,v,c='r',label = 'Tracked DirtyBytes')
plt.legend()
plt.title('WiredTiger Cache')
plt.xlabel('Date/Time')
plt.ylabel('GB',fontsize=15)
plt.xticks(rotation = 45)
plt.savefig('WiredTigerCache.png')


# In[109]:


#bytes
dfx = pd.read_csv('opt5.csv')
dfx['Date/Time'] = pd.to_datetime(dfx['Date/Time'])
x = dfx['Date/Time']
y = dfx['per Minute.2']
w = dfx['per Minute.3']
for i in range(len(y)):
    y[i]=y[i]/1000000000
for i in range(len(w)):
    w[i]=w[i]/1000000000
plt.figure(figsize = (7,7))
plt.title("Cache")
plt.plot(x,y,label = 'GBytes read into cache per minute')
plt.plot(x,w,c='y',label = 'GBytes written from cache per minute')
plt.legend()
plt.xlabel('Date/Time')
plt.ylabel('GB',fontsize=15)
plt.xticks(rotation = 45)
plt.savefig('bytes.png')


# In[110]:


#pages evicted
dfx = pd.read_csv('opt5.csv')
dfx['Date/Time'] = pd.to_datetime(dfx['Date/Time'])
x = dfx['Date/Time']
y = dfx['per Minute']
w = dfx['per Minute.1']
plt.figure(figsize = (7,7))
plt.plot(x,y,label = 'Modified pages evicted per minute')
plt.plot(x,w,c='y',label = 'Unmodified pages evicted per minute')
plt.legend()
plt.title("WiredTiger Cache pages evicted")
plt.xlabel('Date/Time')
plt.ylabel('Values',fontsize=15)
plt.xticks(rotation = 45)
plt.savefig('pagesevicted.png')


# In[111]:


#Memory
dfx = pd.read_csv('opt1.csv')
dfx['Date/Time'] = pd.to_datetime(dfx['Date/Time'])
x = dfx['Date/Time']
y = dfx['res']
w = dfx['virt']
for i in range(len(y)):
    y[i]=y[i]/1000
for i in range(len(w)):
    w[i]=w[i]/1000
plt.figure(figsize = (7,7))
plt.plot(x,y,label = 'resident')
plt.plot(x,w,c='y',label = 'virtual')
plt.legend()
plt.xlabel('Date/Time')
plt.ylabel('GB',fontsize=12)
plt.xticks(rotation = 45)
plt.title("Memory")
plt.savefig('Memory.png')


# In[112]:


#PageFaults
dfx = pd.read_csv('opt1.csv')
dfx['Date/Time'] = pd.to_datetime(dfx['Date/Time'])
x = dfx['Date/Time']
y = dfx['fault']
plt.figure(figsize = (7,7))
plt.plot(x,y,label = 'page faults')
plt.legend()
plt.xlabel('Date/Time')
#plt.ylabel('',fontsize=15)
plt.xticks(rotation = 45)
plt.title('Page Faults')
plt.savefig('PageFaults.png')


# In[113]:


#tickets
dfx = pd.read_csv('opt6.csv')
dfx['Date/Time'] = pd.to_datetime(dfx['Date/Time'])
x = dfx['Date/Time']
y = dfx['Available']
w = dfx['Available.1']
plt.figure(figsize = (7,7))
plt.plot(x,y,label = 'read')
plt.plot(x,w,c='y',label = 'write')
plt.legend()
plt.title("WiredTiger tickets available")
plt.xlabel('Date/Time')
plt.ylabel('Values',fontsize=15)
plt.xticks(rotation = 45)
plt.savefig('tickets.png')


# In[114]:


import imageio
import numpy as np

img1 = imageio.imread('Memory.png')
img2 = imageio.imread('PageFaults.png')
img3 = imageio.imread('OpsCounters1.png')
img4 = imageio.imread('OpsCounters2.png')

row1 = np.concatenate((img1, img2), axis=1)
row2 = np.concatenate((img3, img4), axis=1)
new_image = np.concatenate((row1, row2))
imageio.imwrite('new1.png', new_image)


# In[115]:


img1 = imageio.imread('iops.png')
img2 = imageio.imread('Latency.png')
img3 = imageio.imread('WiredTigerCache.png')
img4 = imageio.imread('bytes.png')

row1 = np.concatenate((img1, img2), axis=1)
row2 = np.concatenate((img3, img4), axis=1)
new_image = np.concatenate((row1, row2))
imageio.imwrite('new2.png', new_image)


# In[116]:


img1 = imageio.imread('pagesevicted.png')
img2 = imageio.imread('tickets.png')

row1 = np.concatenate((img1, img2), axis=1)
new_image = row1
imageio.imwrite('new3.png', new_image)


# In[117]:


from PIL import Image
from glob import glob
import os

iml = []
files = []
files.append('new1.png')
#files.append('new2.png')
files.append('new3.png')
#print(files)
# rgba = Image.open(PNG_FILE)
# To avoid ValueError: cannot save mode RGBA 
rgba = Image.open(glob("*.png")[0])
rgb = Image.new('RGB', rgba.size, (255, 255, 255))  # white background
rgb.paste(rgba, mask=rgba.split()[3])               # paste using alpha channel as mask
for img in range(0,len(files)):
    rgba2 = Image.open(files[img])
    rgb2 = Image.new('RGB', rgba2.size, (255, 255, 255))  # white background
    rgb2.paste(rgba2, mask=rgba2.split()[3])               # paste using alpha channel as mask
    iml.append(rgb2)
pdf = "ALL.pdf"

rgb.save(pdf, "PDF" ,resolution=100.0, save_all=True, append_images=iml)


# In[118]:


from PyPDF2 import PdfFileMerger, PdfFileReader
mergedObject = PdfFileMerger()
mergedObject.append(PdfFileReader('Guide.pdf', 'rb'))
mergedObject.append(PdfFileReader('ALL.pdf', 'rb'))
mergedObject.write("Final.pdf")


# In[119]:


os.remove("opt0.csv")
os.remove("opt1.csv")
os.remove("opt2.csv")
os.remove("opt3.csv")
os.remove("opt4.csv")
os.remove("opt5.csv")
os.remove("opt6.csv")
os.remove("ALL.pdf")
os.remove("bytes.png")
os.remove("iops.png")
os.remove("Latency.png")
os.remove("Memory.png")
os.remove("new1.png")
os.remove("new2.png")
os.remove("new3.png")
os.remove("OpsCounters1.png")
os.remove("Opscounters2.png")
os.remove("out.txt")
os.remove("output.txt")
os.remove("PageFaults.png")
os.remove("pagesevicted.png")
os.remove("tickets.png")
os.remove("WiredTigerCache.png")


# In[120]:


#print("dasf")


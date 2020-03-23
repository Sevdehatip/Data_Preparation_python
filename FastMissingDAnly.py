# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/148LUHdGeeY7kHw6fTapTAT5jozjnPrkE
"""

###Eksik veri analizi hızlı çözüm
import numpy as np
import pandas as pd
V1=np.array([1,3,6,np.NaN,7,1,np.NaN,9,15])
V2=np.array([7,np.NaN,5,8,12,np.NaN,np.NaN,2,3])
V3=np.array([np.NaN,12,5,6,14,7,np.NaN,2,31])
df=pd.DataFrame(
    {"V1":V1,
     "V2":V2,
     "V3":V3})
df

df.isnull().sum()  #herbir değişkendeki eksik değer sayısını verir

df.notnull().sum() #eksik olmayanlar

df.isnull().sum().sum()

df.isnull()  #bu koşul

df[df.isnull().any(axis=1)]  #en az bir tane eksik değer varsa seç demek.

df[df.notnull().all(axis=1)]  #hepsi dolu olanları getirir.

####eksik değerlerin silinmesi

df.dropna()  #kalıcı bir değişiklik yapmaz

#df.dropna(inplace=True) #kalıcı siler
#df

####basit değer atama
df["V1"]

df["V1"].mean()

df["V1"].fillna(df["V1"].mean())   #değişkenler ortalama ile doldurma

df["V2"].fillna(0)

df.apply(lambda x:x.fillna(x.mean()),axis=0)
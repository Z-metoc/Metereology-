#!/usr/bin/env python
# coding: utf-8

#                           # BALANÇO DE JULHO DE 2019 NA CAPITAL PERNAMBUCANA #
# 

# In[35]:


import matplotlib.pyplot as plt  # importando libs iniciais
import pandas as pd
import numpy as np

get_ipython().run_line_magic('matplotlib', 'inline')


# In[36]:


# importando arquivo .csv da Est.Automática A301 referente ao mês de julho como DataFrame

df=pd.read_csv("Desktop/dados_recife")

dfmod=df

# Para eu nao esquecer:
#para resolver problema horario da estacao ,  passe "hora" para index e entao
#sort() , depois transforme data em index , entao sort novamente , e depois transforme index(0)


# In[37]:


# Verificando se há dados NaN ao logo do dataset
df.isnull().values.any() # Out = False -> sem valores NaN


# In[38]:


# Organizando os dados horariamente...
temp=dfmod.sort_values(["data","hora"])
temp["hora_corrida"]=range(0,719)
df=temp
df


# In[39]:


# Calculando a Temperatura media 
df["t_media"]= (df["temp_max"] + df["temp_min"])/2


# In[40]:


# PRECIPITACAO ACUMULADA MENSAL EM JULHO OBSERVADA

total_prep=sum(df["precipitacao"])
print(" Precipitacao mensal acumulada observada : " + str((round(total_prep) ))+ "mm")


# In[76]:


df_=df.pivot_table(values="precipitacao", index="data",aggfunc=np.sum)
df_tmax=df.pivot_table(values="temp_max",index="data",aggfunc=np.max)
df_tmin=df.pivot_table(values="temp_min",index="data",aggfunc=np.min)
df_tmedia=df.pivot_table(values="t_media",index="data",aggfunc=np.mean)

Resultados=[df_tmax.max(),df_tmax.mean(),df_tmin.min(),df_tmin.mean(),len(df_[df_["precipitacao"]==0])]
Resultados_2=[df_tmedia.mean()]
print(Resultados_2)
df_tmedia.sort_values("t_media")


# In[202]:


# amplitude termica
df_tmedia["amp"]=df_tmax["temp_max"] - df_tmin["temp_min"]
df_tmedia.sort_values("amp")


# In[75]:


#df_tmedia=(df_tmax["temp_max"] + df_tmin["temp_min"])/2
#df_tmedia.sort_values("t_media")
#df_tmedia=pd.DataFrame(df_tmedia)
#df_tmedia


# In[188]:


# Desenvolvimento Gráfico 01 #
fig,ax=plt.subplots(figsize=(12,8))
ax.bar(df_.index,df_["precipitacao"],color=(0.1, 0.1, 0.1,0.1),label="Chuva",edgecolor="b")
ax.legend(loc='upper center')
#ax.plot(200)

ax2 = ax.twinx()

ax2.plot(df_tmedia.index,df_tmedia["t_media"],label="T.Média Observada",linestyle='dashed', color="r")
ax2.plot(20)
#ax2.plot(df_tmax.index,df_tmax["temp_max"],linestyle='dashed',color="y",label="tmáx")
ax2.plot(df_.index,30*[24.1],label="T Média (1981-2010)",color="y")
#ax2.plot(df_.index,30*[27.7],label="tmín(1981-2010)")

ax2.set_ylabel(' TEMPERATURA (Celsius)')
ax.set_xticklabels(df_.index, rotation=90)
ax.set_ylabel("PRECIPITAÇÃO(mm)")
ax.set_title("Temperatura Média e Precipitação: JULHO 2019 / RECIFE A301")
ax2.legend()
plt.show()

  


# In[190]:


fig,ax=plt.subplots(figsize=(12,9))

ax.bar(df_tmedia.index,df_tmedia["amp"],color=(0.1, 0.1, 0.1, 0.1),label="Amplitude Térmica",edgecolor="r")
ax.plot(35)
ax.legend(loc='upper center')
ax2 = ax.twinx()

ax2.plot(df_tmax.index,df_tmax["temp_max"],linestyle='dashed',color="y",label="tmáx")
ax2.plot(df_.index,30*[27.7],label="tmax(1981-2010)")
ax2.plot(df_tmin.index,df_tmin["temp_min"],linestyle='dashed',color="g",label="tmin")
ax2.plot(df_.index,30*[21.1],label="tmín(1981-2010)")
ax2.plot(10)

ax.set_title("Temperaturas Máx-Mín: JULHO 2019 / RECIFE A301")
ax.set_ylabel("Amplitude Térmica (Celsius)")
ax.set_xticklabels(df_.index, rotation=90)
ax2.set_ylabel("Temperatura (Celsius)")
ax,ax2.legend()
plt.show()


# In[ ]:


# Importando Série Historia (10 anos) do BDMEP

serie_hist=pd.read_csv("/Users/thiagozamith/Desktop/serie_historica")
serie_hist=serie_hist.sort_values("PrecipitacaoTotal",ascending=False)
serie_hist[serie_hist["PrecipitacaoTotal"] > 400]


# In[45]:


serie_hist=serie_hist.sort_values("NumDiasPrecipitacao",ascending=False)
serie_hist[serie_hist["NumDiasPrecipitacao"] > 25]
serie_hist


# In[49]:


serie_hist=serie_hist.sort_values("TempMinimaMedia",ascending=False)
serie_hist[serie_hist["TempMinimaMedia"] > 20]
serie_hist


# In[57]:


serie_hist=serie_hist.sort_values("TempCompensadaMedia",ascending=False)
serie_hist[serie_hist["TempCompensadaMedia"] >= 24]
serie_hist


# In[201]:


serie_hist["amp"]= serie_hist["TempMaximaMedia"]-serie_hist["TempMinimaMedia"]
serie_hist["amp"].max()


# In[ ]:





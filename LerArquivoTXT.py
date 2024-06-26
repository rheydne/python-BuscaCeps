#!/usr/bin/env python
# coding: utf-8

# In[65]:


#Importando as bibliotecas
import pandas as pd


# In[66]:


def ReadFiles(path, name_file, year_date, type_file):
    
    file = f'{path}{name_file}{year_date}.{type_file}'

    colspecs = [
        (2,10),
        (10,12),
        (12,24),
        (27,39),
        (56,69),
        (69,82),
        (82,95),
        (108,121),
        (152,170),
        (170,188)
    ]

    names = [
        'data_pregao', 
        'codbdi',
        'sigla_acao',
        'nome_acao',
        'preco_abertura',
        'preco_maximo',
        'preco_minimo',
        'preco_fechamento',
        'qtd_negocios',
        'volume_negocios'
    ]

    df = pd.read_fwf(file, colspecs = colspecs, names = names, skiprows = 1)

    return df


# In[67]:


#filtrar acoes

def FilterStocks(df):
     
    df = df[df['codbdi'] == 2]
    df = df.drop(['codbdi'], 1)
  
    return df


# In[68]:


#ajuste campo de data

def ParseDate(df):
    
    df['data_pregao'] = pd.to_datetime(df['data_pregao'], format = '%Y%m%d')
    
    return df


# In[69]:


#ajustes dos campos numéricos

def ParseValues(df):
    
    df['preco_abertura'] = (df['preco_abertura'] / 100).astype(float)
    df['preco_maximo'] = (df['preco_maximo'] / 100).astype(float)
    df['preco_minimo'] = (df['preco_minimo'] / 100).astype(float)
    df['preco_fechamento'] = (df['preco_fechamento'] / 100).astype(float)

    return df


# In[70]:


#juntando arquivos

def ConcatFiles(path, name_file, year_date, type_file, final_file):
    
    for i, y in enumerate(year_date):
        
        df = ReadFiles(path, name_file, y, type_file)
        df = FilterStocks(df)
        df = ParseDate(df)
        df = ParseValues(df)
        
        if(i == 0):
            df_final = df
        else:
            df_final = pd.concat([df_final, df])
            
    df_final.to_csv(f'{path}//{final_file}', index = False)


# In[74]:


#executando o programa

year_date = ['2018', '2019', '2020']

path = f'I:/Crescimento/Temporário/Rheydne/Python/LeituraDeTXT/Arquivos/'

name_file = 'COTAHIST_A'

type_file = 'txt'

final_file = 'all_bovespa.csv'

ConcatFiles(path, name_file, year_date, type_file, final_file)

print('Finish')


# In[ ]:





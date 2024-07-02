#!/usr/bin/env python
# coding: utf-8

# In[6]:


#importando as bibliotecas

import pandas as pd
import os


# In[7]:


#lendo o arquivo .csv

def ReadFiles(path, name_file):
    
    file = f'{path}{name_file}'
    
    names = [
        'Cod_Envio',
        'Cpf',
        'Nome',
        'DataNascimento',
        'Nit',
        'NrBeneficio',
        'Especie',
        'NrRequerente',
        'Endereco',
        'Cep',
        'Municipio',
        'Uf',
        'Assunto',
        'Decisao',
        'Motivo',
        'FundamentoLegal',
        'ApresentadoEm',
        'ConcedidoAte',
        'MantidoAte',
        'ProrrogadoAte',
        'Emissaofundamentacaolegal',
        'Agenciaprevidencia',
        'ConsultadoEm',
        'AcessoEm',
        'Status'  ,
        'IdInterno',
        'IdBaseEnvio',
        'BaseEnvio'
    ]

    df = pd.read_csv(file, sep=';', names = names, header=None, skiprows = 1, index_col = False, encoding='ISO-8859-1')
    
    return df


# In[8]:


#deleta as colunas nao utilizadas

def DeleteColumns(df):
    
    df = df.drop(['FundamentoLegal', 'ProrrogadoAte'], axis=1)
    
    return df


# In[9]:


def ConcatFiles(path, name_file, final_file, path_final_file):
    
    for i, y in enumerate(name_file):
        
        df = ReadFiles(path, y)
        df = DeleteColumns(df)
        
            
        if(i == 0):
            df_final = df
        else:
            df_final = pd.concat([df_final, df])
            
    df_final.to_csv(f'{path_final_file}//{final_file}', index = False, sep=';', encoding='utf-8')


# In[10]:


#executando o programa

print('Iniciando')

path = f'I:/GDN/Plano de Acao/Estudos/Higienizacao/Benefíciários/DCB/Processar/3_RetornosFornecedor/Processar_Retornos/'

name_file = os.listdir(path)

final_file = 'retorno.csv'

path_final_file = f'I:/GDN/Plano de Acao/Estudos/Higienizacao/Benefíciários/DCB/Processar/3_RetornosFornecedor/'

ConcatFiles(path, name_file, final_file, path_final_file)

print ('Finalizado')


# In[ ]:





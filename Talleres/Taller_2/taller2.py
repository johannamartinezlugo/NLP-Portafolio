#!/usr/bin/env python
# coding: utf-8

# <img src='https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcQ-VfNtOyJbsaxu43Kztf_cv1mgBG6ZIQZEVw&usqp=CAU'>
# 
# # Procesamiento de Lenguage Natural
# 
# ## Taller #2: Adquisición de textos
# `Fecha de entrega: Marzo 4, 2021. (Antes del inicio de la próxima clase).`

# # Punto 1:
# 
# - `[18 pts]` Descomprimir el archivo `.zip` de `python_books`
# - `[22 pts]` Leer cada uno de sus archivos
# - `[10 pts]` Responder: ¿Cuál archivo tiene el mayor número de palabras?

# #  Descomprimir el archivo.zip #

# In[1]:


import os
from zipfile import ZipFile


# In[2]:


direccion ='E:/BASES/python_books_taller2.zip'


# In[15]:


# Descomprimir el archivo ZIP
with ZipFile(direccion) as archivo:
    archivo.extractall("E:/BASES")


# In[16]:


import shutil
shutil.rmtree("E:/BASES/__MACOSX/") 


# # Leer cada uno de sus archivos y responder: ¿Cuál archivo tiene el mayor número de palabras?#

# In[17]:


pip install PyMuPDF


# In[18]:


import fitz


# # PDF N°.1#

# In[97]:


doc= fitz.open("E:/BASES/python_books/Python - AWS.pdf")


# In[98]:


doc.pageCount
doc.metadata


# In[103]:


pagina = doc.loadPage(0)
texto = pagina.getText()
texto


# In[109]:


texto.split()


# In[108]:


len(texto.split())


# In[110]:


doc.close()


# # PDF N°.2#

# In[122]:


doc= fitz.open("E:/BASES/python_books/Python  Data Science Cookbook.pdf")


# In[123]:


doc.pageCount
doc.metadata


# In[124]:


pagina = doc.loadPage(0)
texto = pagina.getText()
texto


# In[125]:


texto.split()


# In[126]:


len(texto.split())


# In[127]:


doc.close()


# # PDF N°.3#

# In[128]:


doc= fitz.open("E:/BASES/python_books/Python - Finance.pdf")


# In[129]:


doc.pageCount
doc.metadata


# In[130]:


pagina = doc.loadPage(0)
texto = pagina.getText()
texto


# In[131]:


texto.split()


# In[132]:


len(texto.split())


#!/usr/bin/env python
# coding: utf-8

# ### 文章埋め込みを用いた教師なしキーフレーズ抽出
# #### https://buildersbox.corp-sansan.com/entry/2019/03/19/110000
# #### https://github.com/yagays/embedrank

# In[1]:


from gensim.models.doc2vec import Doc2Vec
from embedrank import EmbedRank
from nlp_uitl import tokenize
import pprint
import re


# In[2]:


print('loading model start ...')
model = Doc2Vec.load("model/jawiki.doc2vec.dbow300d.model")
print('loading model finish ...')


# In[18]:


DATA_PATH = '/home/seki/_seki/NLP/embedrank/data.lst'
with open(DATA_PATH) as f:
    lists = [buf.strip() for buf in f.readlines()]


# In[20]:


for i, text in enumerate(lists):
    
    i = i + 1
    embedrank = EmbedRank(model=model, tokenize=tokenize) # 毎回呼び出すのがいい
    ret = embedrank.extract_keyword(text)
    if len(ret) > 0:
        ret = str(ret)
        ret = re.sub(r'^\[', '', ret)
        ret = re.sub(r'\]$', '', ret)
        ret = re.sub(r'\), \(', ')\t(', ret)
        print('{}\t{}'.format(i, ret))
    else:
        print('{}\tno keyphrase'.format(i))


# In[ ]:





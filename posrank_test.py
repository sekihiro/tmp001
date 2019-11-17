#!/usr/bin/env python
# coding: utf-8

# ### PositionRankでキーフレーズ抽出
# #### https://qiita.com/ymym3412/items/bc3d90e9e1b51959649a<br>https://github.com/ymym3412/position-rank

# In[6]:


from position_rank import position_rank
from tokenizer import MecabTokenizer
import re


# In[7]:


#title = "重要メモ"
#abstract = "先週、新車を買ったけど、販売員の態度が非常に悪かったので、今後は行かないようにする。"


# In[8]:


DATA_PATH = '/home/seki/_seki/NLP/position-rank/data.lst'
with open(DATA_PATH) as f:
    lists = [buf.strip() for buf in f.readlines()]


# In[10]:


tokenizer = MecabTokenizer()
#position_rank(title + abstract, tokenizer, lang="ja")
#position_rank(abstract, tokenizer, lang="ja")

for i, text in enumerate(lists):
    
    i = i + 1
    ret = position_rank(text, tokenizer, alpha=0.06, window_size=4, num_keyphrase=10, lang="ja")
    if len(ret) > 0:
        ret = str(ret)
        ret = re.sub(r'^\[', '', ret)
        ret = re.sub(r'\]$', '', ret)
        ret = re.sub(r', ', '\t', ret)
        print('{}\t{}'.format(i, ret))
    else:
        print('{}\tno keyphrase'.format(i))
    


# In[ ]:





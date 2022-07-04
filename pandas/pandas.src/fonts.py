#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# matplotlib 한글 폰트 문제 해결
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from matplotlib import rc
import platform

if platform.system() == 'Darwin':         # mac
    plt.rc('font',family='AppleGothic')
elif platform.system() == 'Windows':
    rc('font',family='Malgun Gothic')
plt.rc('axes',unicode_minus=False)


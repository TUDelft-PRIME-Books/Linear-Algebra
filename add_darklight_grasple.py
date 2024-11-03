#!/usr/bin/env python
# coding: utf-8

# In[3]:


import os
import numpy as np
files = []
ignore = ['_build','_static','_ext','sphinx-grasple']
for dirpath, dirnames, filenames in os.walk('.'):
    if np.all([dirpath.find(x)<0 for x in ignore]):
        for filename in filenames:
            if filename.endswith('.md'):
                files.append(os.path.join(dirpath, filename.replace('.md','')))

for file in files:
    # load the relevant notebook as a text file
    with open(file+".md") as f:
        new_data = None
        if file not in ['.\\README']:
            data = f.read()
            datalines = np.array(data.split('\n'))
            new_datalines = []
            for li,line in enumerate(datalines):
                # add line to new lines
                new_datalines.append(line)
                grasple = line.find('{grasple}')
                if grasple>-1:
                    # grasple found
                    # check if next line is already dark-light
                    nextline = datalines[li+1]
                    if nextline!=':iframeclass: dark-light':
                        # add the line
                        new_datalines.append(':iframeclass: dark-light')
            new_data = '\n'.join(new_datalines)
    if not(new_data is None):
        with open(file+".md",'w') as f:
            f.write(new_data)


# In[ ]:





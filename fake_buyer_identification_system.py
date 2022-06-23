#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys
import pandas as pd
import math


# In[2]:


raw_data = pd.read_csv(r'orders_2020_2021_DataSet_Updated.csv')
raw_data.head()


# In[3]:


raw_data.columns


# In[4]:


raw_data.shape


# In[5]:


raw_data.info()


# In[7]:


raw_data.isna().sum()


# In[8]:


def input_value_option():
    print('Enter 1: to check if the shipping address differs from the billing address.')
    print('Enter 2: to check if there are multiple orders of the same item.')
    print('Enter 3: to check if there is an unusually large orders.')
    print('Enter 4: to check if there are multiple orders to the same address with different payment method.')
    print('Enter 5: to check if there is an unexpected international orders.')
input_value_option()


# In[15]:


def input_value():
    global i
    i = int(input('Enter the number to see the analysis of your choice'))
input_value()


# In[14]:


if i == 1:
    col = ['Billing Street Address', 'Billing Street Address 2', 'Billing City', 'Billing Zip', 'Billing State', 
           'Billing Country', 'Shipping Street Address', 'Shipping Street Address 2', 'Shipping City', 'Shipping Zip', 
           'Shipping State', 'Shipping Country']
    Data41 = raw_data[col].dropna()
    fake_order_index = []
    for p in list(Data41.index):
        if Data41['Billing Street Address'][p] != Data41['Shipping Street Address'][p] or Data41['Billing Street Address 2'][p] != Data41['Shipping Street Address 2'][p] or Data41['Billing City'][p] != Data41['Shipping City'][p] or Data41['Billing Zip'][p] != Data41['Shipping Zip'][p] or Data41['Billing State'][p] != Data41['Shipping State'][p] or Data41['Billing Country'][p] != Data41['Shipping Country'][p]:
            fake_order_index.append(p)
    fake_order41 = raw_data.iloc[fake_order_index, [0, 14, 15, 16, 18, 17, 13, 21, 22, 23, 25, 24, 20]]
    fake_order41.to_csv('fake_order41.csv')
    quit_choice = input("Press 'Q' to Quit or press 'C' to continue")
    if quit_choice.lower() == 'q':
        sys.exit(0)
    else:
        input_value()


# In[11]:


if i == 2:
    col = ['LineItem Name', 'Shipping Name']
    Data42 = raw_data[col]
    df_42 = pd.DataFrame()
    for p in list(Data42.index):
        multiple_order_index = []
        col_name = Data42['LineItem Name'][p]
        for q in list(Data42.index): 
            if Data42['LineItem Name'][p] == Data42['LineItem Name'][q]:
                if Data42['Shipping Name'][p] == Data42['Shipping Name'][q]:
                    multiple_order_index.append(q)
        dict_42 = {col_name: multiple_order_index}
        df_42 = pd.concat([df_42, pd.DataFrame(dict_42)], axis = 1)
    df_42 = df_42.T.drop_duplicates().T
    df_42 = df_42.dropna(axis=1, thresh=2)
    multiple_order_index = []
    for p in range(df_42.shape[1]):
        for q in range(df_42.shape[0]):
            if math.isnan(df_42.iat[q, p]):
                pass
            else:
                multiple_order_index.append(df_42.iat[q, p])
    multiple_order42 = raw_data.iloc[multiple_order_index, [0, 19, 30]]
    multiple_order42.to_csv('multiple_order42.csv')
    quit_choice = input("Press 'Q' to Quit or press 'C' to continue")
    if quit_choice.lower() == 'q':
        sys.exit(0)
    else:
        input_value()


# In[16]:


if i == 3:
    Data43 = raw_data[['LineItem Qty']]
    fake_order_index = []
    for p in list(Data43.index):
        if Data43['LineItem Qty'][p] > 50:
            fake_order_index.append(p)
    fake_order43 = raw_data.iloc[fake_order_index, [0, 34]]
    fake_order43.to_csv('fake_order43.csv')
    quit_choice = input("Press 'Q' to Quit or press 'C' to continue")
    if quit_choice.lower() == 'q':
        sys.exit(0)
    else:
        input_value()


# In[19]:


if i == 4:    
    col = ['Shipping Street Address', 'Shipping Street Address 2', 
           'Shipping City', 'Shipping Zip', 'Shipping State', 'Shipping Country', 'Payment Method']
    Data44 = raw_data[col].dropna()
    Data44['Payment Method Type'] = Data44['Payment Method'].str.split().apply(lambda ele: ele[0])
    multiple_order_index = []
    for p in list(Data44.index):
        for q in list(Data44.index):
            if Data44['Shipping Country'][p] == Data44['Shipping Country'][q] and Data44['Shipping Street Address'][p] == Data44['Shipping Street Address'][q] and Data44['Shipping Street Address 2'][p] == Data44['Shipping Street Address 2'][q] and Data44['Shipping City'][p] == Data44['Shipping City'][q] and Data44['Shipping State'][p] == Data44['Shipping State'][q] and Data44['Shipping Zip'][p] == Data44['Shipping Zip'][q]:
                if Data44['Payment Method Type'][p] != Data44['Payment Method Type'][q]:
                    multiple_order_index.append(p)
                    multiple_order_index.append(q)
    multiple_order44 = raw_data.iloc[multiple_order_index, [0, 21, 22, 23, 25, 24, 20, 27]]
    multiple_order44 = multiple_order44.drop_duplicates()
    multiple_order44.to_csv('multiple_order44.csv')
    quit_choice = input("Press 'Q' to Quit or press 'C' to continue")
    if quit_choice.lower() == 'q':
        sys.exit(0)
    else:
        input_value()


# In[20]:


if i == 5:
    Data45 = raw_data[['Shipping Country']]
    fake_order_index = []
    for p in list(Data45.index):
        if Data45['Shipping Country'][p] != 'IND':
            fake_order_index.append(p)
    fake_order45 = raw_data.iloc[fake_order_index, [0, 21, 22, 23, 25, 24, 20]]
    fake_order45.to_csv('fake_order45.csv')
    quit_choice = input("Press 'Q' to Quit or press 'C' to continue")
    if quit_choice.lower() == 'q':
        sys.exit(0)
    else:
        input_value()


# In[ ]:





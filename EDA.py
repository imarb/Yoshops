#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages


# In[3]:


dataset_order = pd.read_csv(r'orders_2016-2020_Dataset.csv')
dataset_order.head()


# In[4]:


dataset_order.shape


# In[5]:


dataset_order.info()


# In[6]:


dataset_order.isna().sum()


# In[7]:


dataset_review = pd.read_csv(r'review_dataset.csv')
dataset_review.head()


# In[8]:


for i in range(len(dataset_review['stars'])):
    typ_str = isinstance(dataset_review['stars'][i], str)
    if typ_str:
        dataset_review['stars'][i] = dataset_review['stars'][i][:3]
        dataset_review['stars'][i] = float(dataset_review['stars'][i])
for i in range(len(dataset_review['stars'])):
    if dataset_review['stars'][i] > 3.0:
        dataset_review['stars'][i] = 'Positive'
    elif dataset_review['stars'][i] > 0 and dataset_review['stars'][i] <= 3.0:
        dataset_review['stars'][i] = 'Negative'
    else:
        dataset_review['stars'][i] = 'Not Reviewed'
dataset_review[['stars']].sample(5)


# In[9]:


dataset_review.shape


# In[10]:


dataset_review.info()


# In[11]:


dataset_review.isna().sum()


# In[12]:


def input_value_info():
    print('Enter 1 to see the analysis of reviews given by customers')
    print('Enter 2 to see the analysis of different payment methods used by the customers')
    print('Enter 3 to see the analysis of top consumer states of india')
    print('Enter 4 to see the analysis of top consumer cities of india')
    print('Enter 5 to see the analysis of top selling product categories')
    print('Enter 6 to see the analysis of reviews for all product categories')
    print('Enter 7 to see the analysis of number of orders per month per year')
    print('Enter 9 to see the analysis of number of orders across parts of a day')
    print('Enter 10 to see the full report')
input_value_info()


# In[24]:


def input_value():
    global i
    i = int(input('Enter the number to see the analysis of your choice'))
input_value()


# In[14]:


#analysis of reviews given by customers
if i == 1:
    vals = list(dataset_review['stars'].value_counts().values)
    lbls = list(dataset_review['stars'].value_counts().index)
    xpld = [0, 0.1, 0]
    plt.pie(vals, labels = lbls, autopct = '%1.1f%%', shadow = True, explode = xpld, wedgeprops = {'edgecolor': 'black'})
    plt.title('Customer reviews')
    plt.savefig('E:/Yoshops/Task 2/Customer_reviews.pdf')
    plt.show()
    quit_choice = input("Press 'Q' to Quit or press 'C' to continue")
    if quit_choice.lower() == 'q':
        sys.exit(0)
    else:
        input_value()


# In[15]:


#analysis of different payment methods used by the customers
if i == 2:
    vals = list(dataset_order['Payment Method'].dropna().str.split().apply(lambda ele: ele[0]).value_counts().values)
    lbls = list(dataset_order['Payment Method'].dropna().str.split().apply(lambda ele: ele[0]).value_counts().index)
    xpld = [0.1, 0]
    plt.pie(vals, labels = lbls, autopct = '%1.1f%%', shadow = True, explode = xpld, wedgeprops = {'edgecolor': 'black'})
    plt.title('Customer payment methods')
    plt.savefig('E:/Yoshops/Task 2/Customer_payment_methods.pdf')
    plt.show()
    quit_choice = input("Press 'Q' to Quit or press 'C' to continue")
    if quit_choice.lower() == 'q':
        sys.exit(0)
    else:
        input_value()


# In[16]:


#analysis of top consumer states of india
if i == 3:
    vals = list(dataset_order['Shipping State'].str.split('-').value_counts()[0:5].values)
    lbls = list(dataset_order['Shipping State'].str.split('-').value_counts()[0:5].index)
    lbls_new = []
    for i in lbls:
        lbls_new.append(i[1])
    xpld = [0.1, 0, 0, 0, 0]
    plt.pie(vals, labels = lbls_new, autopct = '%1.1f%%', shadow = True, explode = xpld, wedgeprops = {'edgecolor': 'black'})
    plt.title('Top 5 consumer states of india')
    plt.savefig('E:/Yoshops/Task 2/Top_consumer_states.pdf')
    plt.show()
    quit_choice = input("Press 'Q' to Quit or press 'C' to continue")
    if quit_choice.lower() == 'q':
        sys.exit(0)
    else:
        input_value()


# In[17]:


#analysis of top consumer cities of india
if i == 4:
    vals = list(dataset_order['Shipping City'].value_counts()[0:5].values)
    lbls = list(dataset_order['Shipping City'].value_counts()[0:5].index)
    xpld = [0.1, 0, 0, 0, 0]
    plt.pie(vals, labels = lbls, autopct = '%1.1f%%', shadow = True, explode = xpld, wedgeprops = {'edgecolor': 'black'})
    plt.title('Top 5 consumer cities of india')
    plt.savefig('E:/Yoshops/Task 2/Top_consumer_cities.pdf')
    plt.show()
    quit_choice = input("Press 'Q' to Quit or press 'C' to continue")
    if quit_choice.lower() == 'q':
        sys.exit(0)
    else:
        input_value()


# In[18]:


#analysis of top selling product categories
if i == 5:
    vals = list(dataset_review['category'].value_counts()[0:5].values)
    lbls = list(dataset_review['category'].value_counts()[0:5].index)
    xpld = [0.1, 0, 0, 0, 0]
    plt.pie(vals, labels = lbls, autopct = '%1.1f%%', shadow = True, explode = xpld, wedgeprops = {'edgecolor': 'black'})
    plt.title('Top 5 selling product categories')
    plt.savefig('E:/Yoshops/Task 2/Top_selling_product_categories.pdf')
    plt.show()
    quit_choice = input("Press 'Q' to Quit or press 'C' to continue")
    if quit_choice.lower() == 'q':
        sys.exit(0)
    else:
        input_value()


# In[25]:


#analysis of reviews for all product categories
pdf_file = PdfPages('E:/Yoshops/Task 2/Product_category_reviews.pdf')
if i == 6:
    grp_cat = dataset_review.groupby('category')
    for cat, cat_df in grp_cat:
        vals = list(cat_df['stars'].value_counts().values)
        lbls = list(cat_df['stars'].value_counts().index)
        fig = plt.figure()
        plt.pie(vals, labels = lbls, autopct = '%1.1f%%', shadow = True, wedgeprops = {'edgecolor': 'black'})
        plt.title(' '.join(['Product category:', cat]))
        pdf_file.savefig(fig)
        plt.show()
    quit_choice = input("Press 'Q' to Quit or press 'C' to continue")
    if quit_choice.lower() == 'q':
        sys.exit(0)
    else:
        input_value()
pdf_file.close()


# In[20]:


dataset_order['Order Date and Time Stamp'] = pd.to_datetime(dataset_order['Order Date and Time Stamp'])


# In[21]:


#analysis of number of orders per month per year
pdf_file = PdfPages('E:/Yoshops/Task 2/Orders_per_month_per_year.pdf')
if i == 7:
    grp_yr = dataset_order.groupby(dataset_order['Order Date and Time Stamp'].dt.year)
    for yr, yr_df in grp_yr:
        cnt = list(yr_df['Order Date and Time Stamp'].dt.month.value_counts().values)
        mon = list(yr_df['Order Date and Time Stamp'].dt.month.value_counts().index)
        fig = plt.figure()
        plt.bar(mon, cnt, edgecolor = 'black')  
        plt.title(' '.join(['Year:', str(yr)]))
        plt.xlabel('Month')
        plt.ylabel('Number of order')
        pdf_file.savefig(fig)
        plt.show()
    quit_choice = input("Press 'Q' to Quit or press 'C' to continue")
    if quit_choice.lower() == 'q':
        sys.exit(0)
    else:
        input_value()
pdf_file.close()


# In[22]:


#analysis of number of orders across parts of a day
if i == 9:
    grp_hr = dataset_order.groupby(dataset_order['Order Date and Time Stamp'].dt.hour)
    h = []
    cnt = []
    for hr, hr_df in grp_hr:
        h.append(hr)
        cnt.append(hr_df['Order Date and Time Stamp'].count())
    plt.bar(h, cnt, edgecolor = 'black')
    plt.title('Orders across parts of a day')
    plt.xlabel('Hour')
    plt.ylabel('Number of order')
    plt.savefig('E:/Yoshops/Task 2/Orders_across_parts_of_a_day.pdf')
    plt.show() 
    quit_choice = input("Press 'Q' to Quit or press 'C' to continue")
    if quit_choice.lower() == 'q':
        sys.exit(0)
    else:
        input_value()


# In[23]:


#full report
pdf_file = PdfPages('E:/Yoshops/Task 2/Full_report.pdf')
if i == 10:
    vals = list(dataset_review['stars'].value_counts().values)
    lbls = list(dataset_review['stars'].value_counts().index)
    xpld = [0, 0.1, 0]
    fig = plt.figure()
    plt.pie(vals, labels = lbls, autopct = '%1.1f%%', shadow = True, explode = xpld, wedgeprops = {'edgecolor': 'black'})
    plt.title('Customer reviews')
    pdf_file.savefig(fig)
    plt.show()
        
    vals = list(dataset_order['Payment Method'].dropna().str.split().apply(lambda ele: ele[0]).value_counts().values)
    lbls = list(dataset_order['Payment Method'].dropna().str.split().apply(lambda ele: ele[0]).value_counts().index)
    xpld = [0.1, 0]
    fig = plt.figure()
    plt.pie(vals, labels = lbls, autopct = '%1.1f%%', shadow = True, explode = xpld, wedgeprops = {'edgecolor': 'black'})
    plt.title('Customer payment methods')
    pdf_file.savefig(fig)
    plt.show()
      
    vals = list(dataset_order['Shipping State'].str.split('-').value_counts()[0:5].values)
    lbls = list(dataset_order['Shipping State'].str.split('-').value_counts()[0:5].index)
    lbls_new = []
    for i in lbls:
        lbls_new.append(i[1])
    xpld = [0.1, 0, 0, 0, 0]
    fig = plt.figure()
    plt.pie(vals, labels = lbls_new, autopct = '%1.1f%%', shadow = True, explode = xpld, wedgeprops = {'edgecolor': 'black'})
    plt.title('Top 5 consumer states of india')
    pdf_file.savefig(fig)
    plt.show()
    
    vals = list(dataset_order['Shipping City'].value_counts()[0:5].values)
    lbls = list(dataset_order['Shipping City'].value_counts()[0:5].index)
    xpld = [0.1, 0, 0, 0, 0]
    fig = plt.figure()
    plt.pie(vals, labels = lbls, autopct = '%1.1f%%', shadow = True, explode = xpld, wedgeprops = {'edgecolor': 'black'})
    plt.title('Top 5 consumer cities of india')
    pdf_file.savefig(fig)
    plt.show()
    
    vals = list(dataset_review['category'].value_counts()[0:5].values)
    lbls = list(dataset_review['category'].value_counts()[0:5].index)
    xpld = [0.1, 0, 0, 0, 0]
    fig = plt.figure()
    plt.pie(vals, labels = lbls, autopct = '%1.1f%%', shadow = True, explode = xpld, wedgeprops = {'edgecolor': 'black'})
    plt.title('Top 5 selling product categories')
    pdf_file.savefig(fig)
    plt.show()
    
    grp_cat = dataset_review.groupby('category')
    for cat, cat_df in grp_cat:
        vals = list(cat_df['stars'].value_counts().values)
        lbls = list(cat_df['stars'].value_counts().index)
        fig = plt.figure()
        plt.pie(vals, labels = lbls, autopct = '%1.1f%%', shadow = True, wedgeprops = {'edgecolor': 'black'})
        plt.title(' '.join(['Product category:', cat]))
        pdf_file.savefig(fig)
        plt.show()
    
    grp_yr = dataset_order.groupby(dataset_order['Order Date and Time Stamp'].dt.year)
    for yr, yr_df in grp_yr:
        cnt = list(yr_df['Order Date and Time Stamp'].dt.month.value_counts().values)
        mon = list(yr_df['Order Date and Time Stamp'].dt.month.value_counts().index)
        fig = plt.figure()
        plt.bar(mon, cnt, edgecolor = 'black')  
        plt.title(' '.join(['Year:', str(yr)]))
        plt.xlabel('Month')
        plt.ylabel('Number of order')
        pdf_file.savefig(fig)
        plt.show()
    
    grp_hr = dataset_order.groupby(dataset_order['Order Date and Time Stamp'].dt.hour)
    h = []
    cnt = []
    for hr, hr_df in grp_hr:
        h.append(hr)
        cnt.append(hr_df['Order Date and Time Stamp'].count())
    fig = plt.figure()
    plt.bar(h, cnt, edgecolor = 'black')
    plt.title('Orders across parts of a day')
    plt.xlabel('Hour')
    plt.ylabel('Number of order')
    pdf_file.savefig(fig)
    plt.show() 
    quit_choice = input("Press 'Q' to Quit or press 'C' to continue")
    if quit_choice.lower() == 'q':
        sys.exit(0)
    else:
        input_value()
pdf_file.close()


# In[ ]:





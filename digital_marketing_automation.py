#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from urllib.request import urlopen
from urllib.request import urlretrieve
from bs4 import BeautifulSoup
import re


# In[2]:


def input_value():
    global bg_img, stkr, tg_ln, url
    print('Select Background')
    bg_img = input('Enter any number from 1 to 3: ')
    print('Select Sticker')
    stkr = input('Enter any number from 1 to 3: ')
    tg_ln = input('Enter Tagline: ')
    url = input('Enter URL: ')
input_value()


# In[3]:


res = urlopen(url)
soup = BeautifulSoup(res.read())


# In[4]:


price = soup.select('.single-product-price')
pattern = '\d*,\d*\.\d*|\d*\.\d*'
match = re.findall(pattern, price[0].getText())


# In[5]:


image = soup.select('.single-product-img')
img_name = 'E:/Yoshops/Task_4/logo.png'
urlretrieve(image[0]['src'], img_name)


# In[6]:


filename_bg_img = ''.join(['background_image_', bg_img, '.jpg'])
img = Image.open(filename_bg_img)
img = img.resize((int(img.width/8), int(img.height/8)), resample = Image.LANCZOS)


# In[7]:


filename_stkr = ''.join(['offer_sticker_', stkr, '.png'])
img_1 = Image.open(filename_stkr)
img_1 = img_1.resize((int(img_1.width/2), int(img_1.height/2)), resample = Image.LANCZOS)


# In[8]:


filename_logo = 'logo.png'
img_2 = Image.open(filename_logo)
img_2 = img_2.resize((int(img_2.width/2), int(img_2.height/2)), resample = Image.LANCZOS)


# In[9]:


Image.Image.paste(img, img_1, img_1)


# In[10]:


Image.Image.paste(img, img_2, box = (112, 150, 344, 391), mask = img_2)


# In[11]:


draw = ImageDraw.Draw(img)
my_font = ImageFont.truetype(r'‪C:\Windows\Fonts\PRISTINA.TTF', 40)
draw.text((img.width/ 2, img.height - 50), tg_ln, font = my_font, fill = (255, 0, 0))


# In[12]:


draw = ImageDraw.Draw(img)
my_font = ImageFont.truetype(r'‪‪‪‪C:\Windows\Fonts\Gabriola.ttf', 30)
draw.text((img.width/ 2 - 100, img.height/ 2 + 100), ' '.join(['Original Price:', match[0]]), font = my_font, fill = (0, 0, 0))


# In[13]:


draw = ImageDraw.Draw(img)
my_font = ImageFont.truetype(r'‪C:\Windows\Fonts\Gabriola.ttf', 30)
draw.text((img.width/ 2 - 100, img.height/ 2 + 150), ' '.join(['Offer Price:', match[1]]), font = my_font, fill = (0, 0, 0))


# In[14]:


img.save('banner.png')


# In[15]:


quit_choice = input("Press 'Q' to Quit or press 'C' to continue")
if quit_choice.lower() == 'q':
    sys.exit(0)
else:
    input_value()


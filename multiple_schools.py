# -*- coding: utf-8 -*-
"""Copy of secrets.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1uQsmnXEczI9Pn6OduZzvrJeZ5qvBelEi
"""

import os

#Web scraping libraries
import csv
from bs4 import BeautifulSoup
import re
!pip install selenium
from selenium import webdriver
import time

!apt-get update # to update ubuntu to correctly run apt install
!apt install chromium-chromedriver
!cp /usr/lib/chromium-browser/chromedriver /usr/bin
import sys

# Imports the Google Cloud client library
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

#Data manupulation libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

#Libraries to manipulate dates
!pip install datetime
import datetime

#Date and dependencies are in a google drive folder
#Connect google drive to this notebook
from google.colab import drive
drive.mount('/content/gdrive')

#ensure the file is accessible
!ls /content/gdrive/'My Drive'/'Colab Notebooks'/'secrets hackathon'/dependencies

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/content/gdrive/My Drive/Colab Notebooks/secrets hackathon/dependencies/creds.json"

#ensure the path is set correctly
!echo $GOOGLE_APPLICATION_CREDENTIALS

#print token
!gcloud auth application-default print-access-token

#unzipping our google cloud sdk file
!tar -xvf "/content/gdrive/My Drive/Colab Notebooks/secrets hackathon/dependencies/google-cloud-sdk-280.0.0-linux-x86_64.tar.gz" 

#installing google cloud language
!pip install --upgrade google-cloud-language

sys.path.insert(0,'/usr/lib/chromium-browser/chromedriver')

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
browser_uchicago = webdriver.Chrome('chromedriver',chrome_options=chrome_options)
browser_uchicago.get('https://www.facebook.com/pg/secretsuchicago/posts/?ref=page_internal/')
SCROLL_PAUSE_TIME = 2

# Get scroll height
last_height = browser_uchicago.execute_script("return document.body.scrollHeight")
while True:
    #Scroll down to bottom
    browser_uchicago.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    #Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)
    #Calculate new scroll height and compare with last scroll height
    new_height = browser_uchicago.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height
html = browser_uchicago.page_source

soup = BeautifulSoup(html,'lxml')

file = open('uchicagosecrets.csv','w',encoding='utf-8')
writer = csv.writer(file)

writer.writerow(['PostText UChicago','Date'])

for userContentWrapper in soup.find_all('div',class_='userContentWrapper'):
    content = userContentWrapper.find(class_='userContent').find('p').findNext('p').text
    date = userContentWrapper.find('abbr')['title']
    writer.writerow([content,date])

file.close()
browser_uchicago.close()

browser_columbia = webdriver.Chrome('chromedriver',chrome_options=chrome_options)
browser_columbia.get('https://www.facebook.com/pg/columbiaconfessionz/posts/?ref=page_internal/')
SCROLL_PAUSE_TIME = 2
# Get scroll height
last_height = browser_columbia.execute_script("return document.body.scrollHeight")
while True:
    #Scroll down to bottom
    browser_columbia.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    #Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)
    #Calculate new scroll height and compare with last scroll height
    new_height = browser_columbia.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height
#browser.execute_script("window.scrollTo(0,10000000)")
html = browser_columbia.page_source

soup = BeautifulSoup(html,'lxml')

file = open('columbiasecrets.csv','w',encoding='utf-8')
writer = csv.writer(file)

writer.writerow(['PostText Columbia','Date'])

for userContentWrapper in soup.find_all('div',class_='userContentWrapper'):
    content = userContentWrapper.find(class_='userContent').find('p').text
    date = userContentWrapper.find('abbr')['title']

    writer.writerow([content,date])

file.close()
browser_columbia.close()

browser_mit = webdriver.Chrome('chromedriver',chrome_options=chrome_options)
browser_mit.get('https://www.facebook.com/pg/beaverconfessions/posts/?ref=page_internal/')
SCROLL_PAUSE_TIME = 2
# Get scroll height
last_height = browser_mit.execute_script("return document.body.scrollHeight")

counter = 0
while True:
  while counter < 300:
    print(counter)
    counter = counter + 1
    #Scroll down to bottom
    browser_mit.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    #Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)
    #Calculate new scroll height and compare with last scroll height
    new_height = browser_mit.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height
  break

#browser.execute_script("window.scrollTo(0,10000000)")
html = browser_mit.page_source

soup = BeautifulSoup(html,'lxml')

file = open('mitsecrets.csv','w',encoding='utf-8')
writer = csv.writer(file)

writer.writerow(['PostText MIT','Date'])

for userContentWrapper in soup.find_all('div',class_='userContentWrapper'):
  content = userContentWrapper.find(class_='userContent').find('p').text
  date = userContentWrapper.find('abbr')['title']

  writer.writerow([content,date])

file.close()
browser_mit.close()

browser_harvard = webdriver.Chrome('chromedriver',chrome_options=chrome_options)
browser_harvard.get('https://www.facebook.com/pg/theharvardconfessions/posts/?ref=page_internal/')
SCROLL_PAUSE_TIME = 2
# Get scroll height
last_height = browser_harvard.execute_script("return document.body.scrollHeight")
counter = 0
while True:
  while counter < 300:
    print(counter)
    counter = counter + 1
    #Scroll down to bottom
    browser_harvard.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    #Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)
    #Calculate new scroll height and compare with last scroll height
    new_height = browser_harvard.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height
  break
#browser.execute_script("window.scrollTo(0,10000000)")
html = browser_harvard.page_source

soup = BeautifulSoup(html,'lxml')

file = open('harvardsecrets.csv','w',encoding='utf-8')
writer = csv.writer(file)

writer.writerow(['PostText Harvard','Date'])

for userContentWrapper in soup.find_all('div',class_='userContentWrapper'):
    content = userContentWrapper.find(class_='userContent').find('p').text
    date = userContentWrapper.find('abbr')['title']

    writer.writerow([content,date])

file.close()
browser_harvard.close()

browser_stanford = webdriver.Chrome('chromedriver',chrome_options=chrome_options)
browser_stanford.get('https://www.facebook.com/pg/cardinalconfessions/posts/?ref=page_internal/')
SCROLL_PAUSE_TIME = 1
# Get scroll height
last_height = browser_stanford.execute_script("return document.body.scrollHeight")
while True:
    #Scroll down to bottom
    browser_stanford.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    #Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)
    #Calculate new scroll height and compare with last scroll height
    new_height = browser_stanford.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height
#browser.execute_script("window.scrollTo(0,10000000)")
html = browser_stanford.page_source

soup = BeautifulSoup(html,'lxml')

file = open('stanfordsecrets.csv','w',encoding='utf-8')
writer = csv.writer(file)

writer.writerow(['PostText Stanford','Date'])

for userContentWrapper in soup.find_all('div',class_='userContentWrapper'):
    content = userContentWrapper.find(class_='userContent').find('p').text
    date = userContentWrapper.find('abbr')['title']

    writer.writerow([content,date])

file.close()
browser_stanford.close()

browser_caltech = webdriver.Chrome('chromedriver',chrome_options=chrome_options)
browser_caltech.get('https://www.facebook.com/pg/caltechconfessions/posts/?ref=page_internal/')
SCROLL_PAUSE_TIME = 2
# Get scroll height
last_height = browser_caltech.execute_script("return document.body.scrollHeight")
counter = 0
while True:
  while counter < 200:
    print(counter)
    counter = counter + 1
    #Scroll down to bottom
    browser_caltech.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    #Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)
    #Calculate new scroll height and compare with last scroll height
    new_height = browser_caltech.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height
  break
#browser.execute_script("window.scrollTo(0,10000000)")
html = browser_caltech.page_source

soup = BeautifulSoup(html,'lxml')

file = open('caltechsecrets.csv','w',encoding='utf-8')
writer = csv.writer(file)

writer.writerow(['PostText Caltech','Date'])

for userContentWrapper in soup.find_all('div',class_='userContentWrapper'):
    content = userContentWrapper.find(class_='userContent').find('p').text
    date = userContentWrapper.find('abbr')['title']

    writer.writerow([content,date])

file.close()
browser_caltech.close()

autumn_start = datetime.date(2019, 9, 1).month
winter_start = datetime.date(2019, 12, 1).month
spring_start = datetime.date(2019, 3, 1).month
summer_start = datetime.date(2019, 6, 1).month

#Convert our strings to categorical date-data
def date_to_data(string):
  post_date = datetime.datetime.strptime(string, '%m/%d/%y, %I:%M %p')
  post_year = post_date.year
  
  loc_win_begin_year = datetime.datetime(post_year, 1, 1)
  loc_spring_start = datetime.datetime(post_year, spring_start, 1)
  loc_summer_start = datetime.datetime(post_year, summer_start, 1)
  loc_autumn_start = datetime.datetime(post_year, autumn_start, 1)
  loc_win_end_year = datetime.datetime(post_year, winter_start, 1)

  if (loc_win_begin_year <= post_date < loc_spring_start):
    return 'Winter ' + str(post_year)
  elif (loc_spring_start <= post_date < loc_summer_start):
    return 'Spring ' + str(post_year)
  elif (loc_summer_start <= post_date < loc_autumn_start):
    return 'Summer ' + str(post_year)
  elif (loc_autumn_start <= post_date < loc_win_end_year):
    return 'Autumn ' + str(post_year)
  else:
    return 'Winter ' + str(post_year + 1)

post_to_date("2/16/20, 6:59 AM")

#reading in our data
df_uofc = pd.read_csv (r'/content/uchicagosecrets.csv')
posts_uofc = df_uofc["PostText UChicago"]
dates_uofc = df_uofc["Date"]


#Make new dataframe
graph_data_uchicago = pd.DataFrame(np.zeros((len(df_uofc.index),2)))

for i in range(len(posts_uofc)):
  
  # Instantiates a client
  client = language.LanguageServiceClient()

  # The text to analyze
  text = posts_uofc[i]
  document = types.Document(
      content=text,
      type=enums.Document.Type.PLAIN_TEXT)

  # Detects the sentiment of the text
  sentiment = client.analyze_sentiment(document=document).document_sentiment

  print('Text: {}'.format(text))
  print('Sentiment: {}, {}'.format(sentiment.score, sentiment.magnitude))
  
  value = (sentiment.score*sentiment.magnitude*10)
  post_date = date_to_data(dates_uofc[i])
  graph_data_uchicago.loc[i] = pd.Series({0:value, 1:post_date})

df_columbia = pd.read_csv (r'/content/columbiasecrets.csv')
posts_columbia = df_columbia["PostText Columbia"]
dates_columbia = df_columbia["Date"]

graph_data_columbia = pd.DataFrame(np.zeros((len(df_columbia.index),2)))

for i in range(len(posts_columbia)):
  client = language.LanguageServiceClient()
  text = posts_columbia[i]
  document = types.Document(
    content=text,
    type=enums.Document.Type.PLAIN_TEXT)
  sentiment = client.analyze_sentiment(document = document).document_sentiment
  print('Text: {}'.format(text))
  print('Sentiment:{},{}'.format(sentiment.score,sentiment.magnitude))
  value = (sentiment.score*sentiment.magnitude*10)
  post_date = date_to_data(dates_columbia[i])
  graph_data_columbia.loc[i] = pd.Series({0:value, 1:post_date})

df_mit = pd.read_csv (r'/content/mitsecrets.csv')
posts_mit = df_mit["PostText MIT"]
dates_mit = df_mit["Date"]

graph_data_mit = pd.DataFrame(np.zeros((len(df_mit.index),2)))

for i in range(len(posts_mit)):
  client = language.LanguageServiceClient()
  text = posts_mit[i]
  document = types.Document(
    content=text,
    type=enums.Document.Type.PLAIN_TEXT)
  sentiment = client.analyze_sentiment(document = document).document_sentiment
  print('Text: {}'.format(text))
  print('Sentiment:{},{}'.format(sentiment.score,sentiment.magnitude))
  value = (sentiment.score*sentiment.magnitude*10)
  post_date = date_to_data(dates_mit[i])
  graph_data_mit.loc[i] = pd.Series({0:value, 1:post_date})

df_harvard = pd.read_csv (r'/content/harvardsecrets.csv')
posts_harvard = df_harvard["PostText Harvard"]
dates_harvard = df_harvard["Date"]

graph_data_harvard = pd.DataFrame(np.zeros((len(df_harvard.index),2)))

for i in range(len(posts_harvard)):
  client = language.LanguageServiceClient()
  text = posts_harvard[i]
  document = types.Document(
    content=text,
    type=enums.Document.Type.PLAIN_TEXT)
  sentiment = client.analyze_sentiment(document = document).document_sentiment
  print('Text: {}'.format(text))
  print('Sentiment:{},{}'.format(sentiment.score,sentiment.magnitude))
  value = (sentiment.score*sentiment.magnitude*10)
  post_date = date_to_data(dates_harvard[i])
  graph_data_harvard.loc[i] = pd.Series({0:value, 1:post_date})

df_stanford = pd.read_csv (r'/content/stanfordsecrets.csv')
posts_stanford = df_stanford["PostText Stanford"]
dates_stanford = df_stanford["Date"]

graph_data_stanford = pd.DataFrame(np.zeros((len(df_stanford.index),2)))

for i in range(len(posts_stanford)):
  client = language.LanguageServiceClient()
  text = posts_stanford[i]
  document = types.Document(
    content=text,
    type=enums.Document.Type.PLAIN_TEXT)
  sentiment = client.analyze_sentiment(document = document).document_sentiment
  print('Text: {}'.format(text))
  print('Sentiment:{},{}'.format(sentiment.score,sentiment.magnitude))
  value = (sentiment.score*sentiment.magnitude*10)
  post_date = date_to_data(dates_stanford[i])
  graph_data_stanford.loc[i] = pd.Series({0:value, 1:post_date})

df_caltech = pd.read_csv (r'/content/caltechsecrets.csv')
posts_caltech = df_caltech["PostText Caltech"]
dates_caltech = df_caltech["Date"]

graph_data_caltech = pd.DataFrame(np.zeros((len(df_caltech.index),2)))

for i in range(len(posts_caltech)):
  client = language.LanguageServiceClient()
  text = posts_caltech[i]
  document = types.Document(
    content=text,
    type=enums.Document.Type.PLAIN_TEXT)
  sentiment = client.analyze_sentiment(document = document).document_sentiment
  print('Text: {}'.format(text))
  print('Sentiment:{},{}'.format(sentiment.score,sentiment.magnitude))
  value = (sentiment.score*sentiment.magnitude*10)
  post_date = date_to_data(dates_caltech[i])
  graph_data_caltech.loc[i] = pd.Series({0:value, 1:post_date})

final_graph_uchicago =  pd.DataFrame(np.zeros((6, 2)))

winter_20_uchicago = graph_data_uchicago.loc[graph_data_uchicago[1] == 'Winter 2020']
autumn_19_uchicago = graph_data_uchicago.loc[graph_data_uchicago[1] == 'Autumn 2019']
spring_19_uchicago = graph_data_uchicago.loc[graph_data_uchicago[1] == 'Spring 2019']
winter_19_uchicago = graph_data_uchicago.loc[graph_data_uchicago[1] == 'Winter 2019']
autumn_18_uchicago = graph_data_uchicago.loc[graph_data_uchicago[1] == 'Autumn 2018']
spring_18_uchicago = graph_data_uchicago.loc[graph_data_uchicago[1] == 'Spring 2018']

final_graph_uchicago.loc[5] = pd.Series({0:'Winter 20', 1:winter_20_uchicago[[0]].mean(axis=0)})
final_graph_uchicago.loc[4] = pd.Series({0: 'Autumn 19', 1:autumn_19_uchicago[[0]].mean(axis=0)})
final_graph_uchicago.loc[3] = pd.Series({0:'Spring 19', 1:spring_19_uchicago[[0]].mean(axis=0)})
final_graph_uchicago.loc[2] = pd.Series({0:'Winter 19', 1:winter_19_uchicago[[0]].mean(axis=0)})
final_graph_uchicago.loc[1] = pd.Series({0:'Autumn 18', 1:autumn_18_uchicago[[0]].mean(axis=0)})
final_graph_uchicago.loc[0] = pd.Series({0:'Spring 18', 1:spring_18_uchicago[[0]].mean(axis=0)})

final_graph_columbia =  pd.DataFrame(np.zeros((6, 2)))

winter_20_columbia = graph_data_columbia.loc[graph_data_columbia[1] == 'Winter 2020']
autumn_19_columbia = graph_data_columbia.loc[graph_data_columbia[1] == 'Autumn 2019']
spring_19_columbia = graph_data_columbia.loc[graph_data_columbia[1] == 'Spring 2019']
winter_19_columbia = graph_data_columbia.loc[graph_data_columbia[1] == 'Winter 2019']
autumn_18_columbia = graph_data_columbia.loc[graph_data_columbia[1] == 'Autumn 2018']
spring_18_columbia = graph_data_columbia.loc[graph_data_columbia[1] == 'Spring 2018']

final_graph_columbia.loc[5] = pd.Series({0:'Winter 20', 1:winter_20_columbia[[0]].mean(axis=0)})
final_graph_columbia.loc[4] = pd.Series({0: 'Autumn 19', 1:autumn_19_columbia[[0]].mean(axis=0)})
final_graph_columbia.loc[3] = pd.Series({0:'Spring 19', 1:spring_19_columbia[[0]].mean(axis=0)})
final_graph_columbia.loc[2] = pd.Series({0:'Winter 19', 1:winter_19_columbia[[0]].mean(axis=0)})
final_graph_columbia.loc[1] = pd.Series({0:'Autumn 18', 1:autumn_18_columbia[[0]].mean(axis=0)})
final_graph_columbia.loc[0] = pd.Series({0:'Spring 18', 1:spring_18_columbia[[0]].mean(axis=0)})

final_graph_mit =  pd.DataFrame(np.zeros((6, 2)))

winter_20_mit = graph_data_mit.loc[graph_data_mit[1] == 'Winter 2020']
autumn_19_mit = graph_data_mit.loc[graph_data_mit[1] == 'Autumn 2019']
spring_19_mit = graph_data_mit.loc[graph_data_mit[1] == 'Spring 2019']
winter_19_mit = graph_data_mit.loc[graph_data_mit[1] == 'Winter 2019']
autumn_18_mit = graph_data_mit.loc[graph_data_mit[1] == 'Autumn 2018']
spring_18_mit = graph_data_mit.loc[graph_data_mit[1] == 'Spring 2018']

final_graph_mit.loc[5] = pd.Series({0:'Winter 20', 1:winter_20_mit[[0]].mean(axis=0)})
final_graph_mit.loc[4] = pd.Series({0: 'Autumn 19', 1:autumn_19_mit[[0]].mean(axis=0)})
final_graph_mit.loc[3] = pd.Series({0:'Spring 19', 1:spring_19_mit[[0]].mean(axis=0)})
final_graph_mit.loc[2] = pd.Series({0:'Winter 19', 1:winter_19_mit[[0]].mean(axis=0)})
final_graph_mit.loc[1] = pd.Series({0:'Autumn 18', 1:autumn_18_mit[[0]].mean(axis=0)})
final_graph_mit.loc[0] = pd.Series({0:'Spring 18', 1:spring_18_mit[[0]].mean(axis=0)})

final_graph_harvard =  pd.DataFrame(np.zeros((6, 2)))

winter_20_harvard = graph_data_harvard.loc[graph_data_harvard[1] == 'Winter 2020']
autumn_19_harvard = graph_data_harvard.loc[graph_data_harvard[1] == 'Autumn 2019']
spring_19_harvard = graph_data_harvard.loc[graph_data_harvard[1] == 'Spring 2019']
winter_19_harvard = graph_data_harvard.loc[graph_data_harvard[1] == 'Winter 2019']
autumn_18_harvard = graph_data_harvard.loc[graph_data_harvard[1] == 'Autumn 2018']
spring_18_harvard = graph_data_harvard.loc[graph_data_harvard[1] == 'Spring 2018']

print(graph_data_harvard)

final_graph_harvard.loc[5] = pd.Series({0:'Winter 20', 1:winter_20_harvard[[0]].mean(axis=0)})
final_graph_harvard.loc[4] = pd.Series({0: 'Autumn 19', 1:autumn_19_harvard[[0]].mean(axis=0)})
final_graph_harvard.loc[3] = pd.Series({0:'Spring 19', 1:spring_19_harvard[[0]].mean(axis=0)})
final_graph_harvard.loc[2] = pd.Series({0:'Winter 19', 1:winter_19_harvard[[0]].mean(axis=0)})
final_graph_harvard.loc[1] = pd.Series({0:'Autumn 18', 1:autumn_18_harvard[[0]].mean(axis=0)})
final_graph_harvard.loc[0] = pd.Series({0:'Spring 18', 1:spring_18_harvard[[0]].mean(axis=0)})

final_graph_stanford =  pd.DataFrame(np.zeros((6, 2)))

winter_20_stanford = graph_data_stanford.loc[graph_data_stanford[1] == 'Winter 2020']
autumn_19_stanford = graph_data_stanford.loc[graph_data_stanford[1] == 'Autumn 2019']
spring_19_stanford = graph_data_stanford.loc[graph_data_stanford[1] == 'Spring 2019']
winter_19_stanford = graph_data_stanford.loc[graph_data_stanford[1] == 'Winter 2019']
autumn_18_stanford = graph_data_stanford.loc[graph_data_stanford[1] == 'Autumn 2018']
spring_18_stanford = graph_data_stanford.loc[graph_data_stanford[1] == 'Spring 2018']

print(graph_data_stanford)

final_graph_stanford.loc[5] = pd.Series({0:'Winter 20', 1:winter_20_stanford[[0]].mean(axis=0)})
final_graph_stanford.loc[4] = pd.Series({0: 'Autumn 19', 1:autumn_19_stanford[[0]].mean(axis=0)})
final_graph_stanford.loc[3] = pd.Series({0:'Spring 19', 1:spring_19_stanford[[0]].mean(axis=0)})
final_graph_stanford.loc[2] = pd.Series({0:'Winter 19', 1:winter_19_stanford[[0]].mean(axis=0)})
final_graph_stanford.loc[1] = pd.Series({0:'Autumn 18', 1:autumn_18_stanford[[0]].mean(axis=0)})
final_graph_stanford.loc[0] = pd.Series({0:'Spring 18', 1:spring_18_stanford[[0]].mean(axis=0)})

final_graph_caltech =  pd.DataFrame(np.zeros((6, 2)))

winter_20_caltech = graph_data_caltech.loc[graph_data_caltech[1] == 'Winter 2020']
autumn_19_caltech = graph_data_caltech.loc[graph_data_caltech[1] == 'Autumn 2019']
spring_19_caltech = graph_data_caltech.loc[graph_data_caltech[1] == 'Spring 2019']
winter_19_caltech = graph_data_caltech.loc[graph_data_caltech[1] == 'Winter 2019']
autumn_18_caltech = graph_data_caltech.loc[graph_data_caltech[1] == 'Autumn 2018']
spring_18_caltech = graph_data_caltech.loc[graph_data_caltech[1] == 'Spring 2018']

print(graph_data_caltech)

final_graph_caltech.loc[5] = pd.Series({0:'Winter 20', 1:winter_20_caltech[[0]].mean(axis=0)})
final_graph_caltech.loc[4] = pd.Series({0: 'Autumn 19', 1:autumn_19_caltech[[0]].mean(axis=0)})
final_graph_caltech.loc[3] = pd.Series({0:'Spring 19', 1:spring_19_caltech[[0]].mean(axis=0)})
final_graph_caltech.loc[2] = pd.Series({0:'Winter 19', 1:winter_19_caltech[[0]].mean(axis=0)})
final_graph_caltech.loc[1] = pd.Series({0:'Autumn 18', 1:autumn_18_caltech[[0]].mean(axis=0)})
final_graph_caltech.loc[0] = pd.Series({0:'Spring 18', 1:spring_18_caltech[[0]].mean(axis=0)})

#plotting our results
plt.scatter(final_graph_uchicago[0], final_graph_uchicago[1])
uchicago_plot = plt.plot(final_graph_uchicago[0], final_graph_uchicago[1], label='UChicago')
plt.scatter(final_graph_columbia[0], final_graph_columbia[1])
columbia_plot = plt.plot(final_graph_columbia[0], final_graph_columbia[1], label='Columbia')
plt.scatter(final_graph_mit[0], final_graph_mit[1])
mit_plot = plt.plot(final_graph_mit[0], final_graph_mit[1], label='MIT')
plt.scatter(final_graph_stanford[0], final_graph_stanford[1])
stanford_plot = plt.plot(final_graph_stanford[0], final_graph_stanford[1], label='Stanford')
plt.scatter(final_graph_caltech[0], final_graph_caltech[1])
caltech_plot = plt.plot(final_graph_caltech[0], final_graph_caltech[1], label='Caltech')

purple = mpatches.Patch(color='purple', label='UChicago')
cyan = mpatches.Patch(color = 'orange', label='Columbia')
red = mpatches.Patch(color = 'red', label = 'MIT')
green = mpatches.Patch(color = 'green', label='Stanford')
blue = mpatches.Patch(color='blue', label='Caltech')
plt.legend(handles=[blue, green, red, cyan, purple])
plt.show()
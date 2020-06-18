# uchicagosecrets
uchicagosecrets was a submission for the UChicago Hackathon which involved webscraping from facebook and natural language processing. Initially posts from the UChicago facebook page was webscraped and sentiment analysis was performed on each post to yield a seasonal chart showing student sentiment. This was then extended across the facebook pages of other colleges.

## What it does

We decided to carry out a sentiment analysis on the "Uchicago Secrets" Facebook page. This is a student-run Facebook page wherein students throw their opinions, reflections, secret confessions about their daily lives on campus. Analysing the sentiments in these Facebook posts gave us a general sense of the mood on campus. We compared the mood of the winter quarter with other quarters and saw many interesting features.

## How I built it

First, we used Selenium and BeautifulSoup to web scrap the Facebook page and clean up the data. Next, we set up a Google Cloud Platform on Google Colab and set up a Sentiment Analysis Model. We fed the cleaned data to the model and used Pandas and Numpy to make a data frame of the average sentiment and the corresponding time of the year. Lastly, we used MatPlotLib to graph our data and make valid conclusions. Next, we scaled this to other colleges and their seasonal sentiments. 

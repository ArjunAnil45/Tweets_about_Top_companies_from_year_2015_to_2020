
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt

#copying the current directory and assigning to pwd
pwd = os.getcwd()

#reading the csv files and saving into dataframes
company_data_frame = pd.read_csv(pwd+'/company.csv')
company_tweet_data_frame = pd.read_csv(pwd+'/company_tweet.csv')
tweets_data_frame = pd.read_csv(pwd+'/tweet.csv')


#looking for any duplicated values in each dataframe
company_data_frame.duplicated()
company_tweet_data_frame.loc[company_tweet_data_frame.duplicated(),:]
tweets_data_frame.loc[tweets_data_frame.duplicated(),:]

#trying to understand what kind of columns are we dealing with
company_data_frame.columns
company_tweet_data_frame.columns
tweets_data_frame.columns

#creating duplicate dataframe for working with so that if something goes wrong we can always go back
company_tweet_data_frame_mod = company_tweet_data_frame.copy()
company_data_frame_mod = company_data_frame.copy()
tweets_data_frame_mod = tweets_data_frame.copy()

#checking if everything worked correctly
company_data_frame
company_tweet_data_frame_mod

#joining 2 dataframes together based on common key
company_tweet_id = pd.merge(left=company_tweet_data_frame_mod,right=company_data_frame_mod,how="left",left_on="ticker_symbol",right_on="ticker_symbol")
company_tweet_id

#Checking if the merged data frame size match with the orginal data frame size
print("Orginal",len(company_data_frame))
print("Orginal",len(company_tweet_data_frame))
print("merged",len(company_tweet_id))

tweets_data_frame_mod

#joining 2 dataframes together based on common key
tweets_for_company = pd.merge(left=company_tweet_id,right=tweets_data_frame_mod,how="left",left_on="tweet_id",right_on="tweet_id")

tweets_for_company

#creating csv for the final work. 
tweets_for_company.to_csv(pwd+"/Final.csv",index=False)
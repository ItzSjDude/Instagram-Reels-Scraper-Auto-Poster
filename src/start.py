import streamlit as st
import os
import sys
import config as mainConfig
from db import Session, Config
import helpers as Helper
from datetime import datetime
import auth

# Define the Streamlit layout
st.title("Configuration Setup")

# Function to handle configuration setup
def configure():
    if st.checkbox("Start Configuration"):
        setup = st.radio("Do you want to run the configuration (To update config values)?", ('Yes', 'No'))
        if setup == 'Yes':
            # Add configuration prompts
            mainConfig.IS_REMOVE_FILES = st.radio("Turn On File Remover After Posting? 1=On;0=Off :", ('1', '0'))
            Helper.save_config('IS_REMOVE_FILES', mainConfig.IS_REMOVE_FILES)
            if mainConfig.IS_REMOVE_FILES == "1":
                mainConfig.REMOVE_FILE_AFTER_MINS = st.number_input("Define the interval in minutes to remove uploaded files:", value=0)
                Helper.save_config('REMOVE_FILE_AFTER_MINS', mainConfig.REMOVE_FILE_AFTER_MINS)

            mainConfig.IS_ENABLED_REELS_SCRAPER = st.radio("Turn On Reels Scraper? 1=On;0=Off :", ('1', '0'))
            Helper.save_config('IS_ENABLED_REELS_SCRAPER', mainConfig.IS_ENABLED_REELS_SCRAPER)
            if mainConfig.IS_ENABLED_REELS_SCRAPER == "1":
                mainConfig.FETCH_LIMIT = st.number_input("Screper fetch limit in number Ex. 50", value=50)
                Helper.save_config('FETCH_LIMIT', mainConfig.FETCH_LIMIT)
                mainConfig.SCRAPER_INTERVAL_IN_MIN = st.number_input("Reels scraping interval in minutes Ex. 120: For every 2 hours", value=120)
                Helper.save_config('SCRAPER_INTERVAL_IN_MIN', mainConfig.SCRAPER_INTERVAL_IN_MIN)

            mainConfig.IS_ENABLED_AUTO_POSTER = st.radio("Turn On Reels Autoposter? 1=On;0=Off :", ('1', '0'))
            Helper.save_config('IS_ENABLED_AUTO_POSTER', mainConfig.IS_ENABLED_AUTO_POSTER)
            if mainConfig.IS_ENABLED_AUTO_POSTER == "1":
                mainConfig.POSTING_INTERVAL_IN_MIN = st.number_input("Reels posting interval in minutes Ex. 10: For every 10 minutes", value=10)
                Helper.save_config('POSTING_INTERVAL_IN_MIN', mainConfig.POSTING_INTERVAL_IN_MIN)

            mainConfig.IS_POST_TO_STORY = st.radio("Turn On post reels into story? 1=On;0=Off :", ('1', '0'))
            Helper.save_config('IS_POST_TO_STORY', mainConfig.IS_POST_TO_STORY)

            mainConfig.USERNAME = st.text_input("Enter Instagram Username:")
            Helper.save_config('USERNAME', mainConfig.USERNAME)

            mainConfig.PASSWORD = st.text_input("Enter Instagram Password:", type="password")
            Helper.save_config('PASSWORD', mainConfig.PASSWORD)

            mainConfig.ACCOUNTS = st.text_input("Enter list of accounts which you want to scrape (comma separated):")
            Helper.save_config('ACCOUNTS', mainConfig.ACCOUNTS)

            mainConfig.HASTAGS = st.text_input("Enter hashtags which you want to add while posting:")
            Helper.save_config('HASTAGS', mainConfig.HASTAGS)

            mainConfig.LIKE_AND_VIEW_COUNTS_DISABLED = st.radio("Like and view counts disabled? 1=Disabled;0=Enabled :", ('1', '0'))
            Helper.save_config('LIKE_AND_VIEW_COUNTS_DISABLED', mainConfig.LIKE_AND_VIEW_COUNTS_DISABLED)

            mainConfig.DISABLE_COMMENTS = st.radio("Comments disabled? 1=Disabled;0=Enabled :", ('1', '0'))
            Helper.save_config('DISABLE_COMMENTS', mainConfig.DISABLE_COMMENTS)

            mainConfig.IS_ENABLED_YOUTUBE_SCRAPING = st.radio("Turn On YouTube Shorts Scraper? 1=On;0=Off :", ('1', '0'))
            Helper.save_config('IS_ENABLED_YOUTUBE_SCRAPING', mainConfig.IS_ENABLED_YOUTUBE_SCRAPING)
            if mainConfig.IS_ENABLED_YOUTUBE_SCRAPING == "1":
                mainConfig.YOUTUBE_API_KEY = st.text_input("Enter Youtube API KEY:")
                Helper.save_config('YOUTUBE_API_KEY', mainConfig.YOUTUBE_API_KEY)
                mainConfig.CHANNEL_LINKS = st.text_input("Enter channel links to scrape (comma separated):")
                Helper.save_config('CHANNEL_LINKS', mainConfig.CHANNEL_LINKS)

            st.write("Configuration setup completed.")
            st.write("Launching the application...")
            launch_app()
        else:
            st.write("Configuration setup cancelled.")

# Function to launch the application
def launch_app():
    python_executable_path = sys.executable
    os.system(python_executable_path + " app.py 1")

# Run the configuration setup
configure()

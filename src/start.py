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
    start_config = st.button("Start Configuration")
    if start_config:
        setup = st.button("Yes")
        if setup:
            # Add configuration prompts
            mainConfig.IS_REMOVE_FILES = st.radio("Turn On File Remover After Posting? 1=On;0=Off :", ('1', '0'))
            if mainConfig.IS_REMOVE_FILES == "1":
                mainConfig.REMOVE_FILE_AFTER_MINS = st.number_input("Define the interval in minutes to remove uploaded files:", value=0)

            mainConfig.IS_ENABLED_REELS_SCRAPER = st.radio("Turn On Reels Scraper? 1=On;0=Off :", ('1', '0'))
            if mainConfig.IS_ENABLED_REELS_SCRAPER == "1":
                mainConfig.FETCH_LIMIT = st.number_input("Screper fetch limit in number Ex. 50", value=50)
                mainConfig.SCRAPER_INTERVAL_IN_MIN = st.number_input("Reels scraping interval in minutes Ex. 120: For every 2 hours", value=120)

            mainConfig.IS_ENABLED_AUTO_POSTER = st.radio("Turn On Reels Autoposter? 1=On;0=Off :", ('1', '0'))
            if mainConfig.IS_ENABLED_AUTO_POSTER == "1":
                mainConfig.POSTING_INTERVAL_IN_MIN = st.number_input("Reels posting interval in minutes Ex. 10: For every 10 minutes", value=10)

            mainConfig.IS_POST_TO_STORY = st.radio("Turn On post reels into story? 1=On;0=Off :", ('1', '0'))

            mainConfig.USERNAME = st.text_input("Enter Instagram Username:")
            mainConfig.PASSWORD = st.text_input("Enter Instagram Password:", type="password")

            mainConfig.ACCOUNTS = st.text_input("Enter list of accounts which you want to scrape (comma separated):")
            mainConfig.HASTAGS = st.text_input("Enter hashtags which you want to add while posting:")

            mainConfig.LIKE_AND_VIEW_COUNTS_DISABLED = st.radio("Like and view counts disabled? 1=Disabled;0=Enabled :", ('1', '0'))
            mainConfig.DISABLE_COMMENTS = st.radio("Comments disabled? 1=Disabled;0=Enabled :", ('1', '0'))

            mainConfig.IS_ENABLED_YOUTUBE_SCRAPING = st.radio("Turn On YouTube Shorts Scraper? 1=On;0=Off :", ('1', '0'))
            if mainConfig.IS_ENABLED_YOUTUBE_SCRAPING == "1":
                mainConfig.YOUTUBE_API_KEY = st.text_input("Enter Youtube API KEY:")
                mainConfig.CHANNEL_LINKS = st.text_input("Enter channel links to scrape (comma separated):")

            save_config = st.button("Save Configuration")
            if save_config:
                # Save configuration and launch the application
                Helper.save_configurations()
                st.write("Configuration saved successfully.")
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

import streamlit as st
import os
import sys
import config as mainConfig
from db import Session, Config
import helpers as Helper
from datetime import datetime
import auth

# Define the Streamlit layout
def main():
    st.title("Terminal Configuration Setup")
    st.write("Welcome to the Configuration Setup!")
    st.write("Type 'help' to see available commands.")

    command = st.text_input(">>")

    if command.lower() == "help":
        st.write("Available commands:")
        st.write("1. start - Begin the configuration setup.")
        st.write("2. launch - Directly launch the application.")
    elif command.lower() == "start":
        start_configuration()
    elif command.lower() == "launch":
        st.write("Launching the application...")
        launch_app()
    elif command.strip():  # Check if the command is not empty
        st.write("Invalid command. Type 'help' to see available commands.")

# Generator function to handle the configuration steps
def start_configuration():
    st.write("Follow the prompts to configure your settings.")
    
    # Step 1: File Remover Configuration
    st.write("Step 1: File Remover Configuration")
    mainConfig.IS_REMOVE_FILES = st.text_input("Turn On File Remover After Posting? 1=On;0=Off :")
    Helper.save_config('IS_REMOVE_FILES', mainConfig.IS_REMOVE_FILES)
    if mainConfig.IS_REMOVE_FILES == "1":
        mainConfig.REMOVE_FILE_AFTER_MINS = st.number_input("Define the interval in minutes to remove uploaded files:")
        Helper.save_config('REMOVE_FILE_AFTER_MINS', mainConfig.REMOVE_FILE_AFTER_MINS)

    # Step 2: Reels Scraper Configuration
    st.write("Step 2: Reels Scraper Configuration")
    mainConfig.IS_ENABLED_REELS_SCRAPER = st.text_input("Turn On Reels Scraper? 1=On;0=Off :")
    Helper.save_config('IS_ENABLED_REELS_SCRAPER', mainConfig.IS_ENABLED_REELS_SCRAPER)
    if mainConfig.IS_ENABLED_REELS_SCRAPER == "1":
        mainConfig.FETCH_LIMIT = st.number_input("Screper fetch limit in number Ex. 50")
        Helper.save_config('FETCH_LIMIT', mainConfig.FETCH_LIMIT)
        mainConfig.SCRAPER_INTERVAL_IN_MIN = st.number_input("Reels scraping interval in minutes Ex. 120: For every 2 hours")
        Helper.save_config('SCRAPER_INTERVAL_IN_MIN', mainConfig.SCRAPER_INTERVAL_IN_MIN)

    # Step 3: Reels Autoposter Configuration
    st.write("Step 3: Reels Autoposter Configuration")
    mainConfig.IS_ENABLED_AUTO_POSTER = st.text_input("Turn On Reels Autoposter? 1=On;0=Off :")
    Helper.save_config('IS_ENABLED_AUTO_POSTER', mainConfig.IS_ENABLED_AUTO_POSTER)
    if mainConfig.IS_ENABLED_AUTO_POSTER == "1":
        mainConfig.POSTING_INTERVAL_IN_MIN = st.number_input("Reels posting interval in minutes Ex. 10: For every 10 minutes")
        Helper.save_config('POSTING_INTERVAL_IN_MIN', mainConfig.POSTING_INTERVAL_IN_MIN)

    # Step 4: Post Reels to Story Configuration
    st.write("Step 4: Post Reels to Story Configuration")
    mainConfig.IS_POST_TO_STORY = st.text_input("Turn On post reels into story? 1=On;0=Off :")
    Helper.save_config('IS_POST_TO_STORY', mainConfig.IS_POST_TO_STORY)

    # Step 5: Instagram Account Configuration
    st.write("Step 5: Instagram Account Configuration")
    mainConfig.USERNAME = st.text_input("Enter Instagram Username:")
    Helper.save_config('USERNAME', mainConfig.USERNAME)

    mainConfig.PASSWORD = st.text_input("Enter Instagram Password:", type="password")
    Helper.save_config('PASSWORD', mainConfig.PASSWORD)

    # Step 6: Additional Configuration
    st.write("Step 6: Additional Configuration")
    mainConfig.ACCOUNTS = st.text_input("Enter list of accounts which you want to scrape (comma separated):")
    Helper.save_config('ACCOUNTS', mainConfig.ACCOUNTS)

    mainConfig.HASTAGS = st.text_input("Enter hashtags which you want to add while posting:")
    Helper.save_config('HASTAGS', mainConfig.HASTAGS)

    mainConfig.LIKE_AND_VIEW_COUNTS_DISABLED = st.text_input("Like and view counts disabled? 1=Disabled;0=Enabled :")
    Helper.save_config('LIKE_AND_VIEW_COUNTS_DISABLED', mainConfig.LIKE_AND_VIEW_COUNTS_DISABLED)

    mainConfig.DISABLE_COMMENTS = st.text_input("Comments disabled? 1=Disabled;0=Enabled :")
    Helper.save_config('DISABLE_COMMENTS', mainConfig.DISABLE_COMMENTS)

    # Step 7: YouTube Shorts Scraper Configuration
    st.write("Step 7: YouTube Shorts Scraper Configuration")
    mainConfig.IS_ENABLED_YOUTUBE_SCRAPING = st.text_input("Turn On YouTube Shorts Scraper? 1=On;0=Off :")
    Helper.save_config('IS_ENABLED_YOUTUBE_SCRAPING', mainConfig.IS_ENABLED_YOUTUBE_SCRAPING)
    if mainConfig.IS_ENABLED_YOUTUBE_SCRAPING == "1":
        mainConfig.YOUTUBE_API_KEY = st.text_input("Enter Youtube API KEY:")
        Helper.save_config('YOUTUBE_API_KEY', mainConfig.YOUTUBE_API_KEY)
        mainConfig.CHANNEL_LINKS = st.text_input("Enter channel links to scrape (comma separated):")
        Helper.save_config('CHANNEL_LINKS', mainConfig.CHANNEL_LINKS)

    st.write("Configuration setup completed.")
    st.write("Launching the application...")
    launch_app()

# Function to launch the application
def launch_app():
    python_executable_path = sys.executable
    os.system(python_executable_path + " app.py 1")

# Run the Streamlit app
if __name__ == "__main__":
    main()

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
    st.write("Press the button below to start the configuration setup.")
    if st.button("Start Configuration"):
        setup = st.radio("Do you want to run the configuration (To update config values)?", ('Yes', 'No'))
        if setup == 'Yes':
            # Add your configuration prompts here
            # Example:
            mainConfig.IS_REMOVE_FILES = st.radio("Turn On File Remover After Posting? 1=On;0=Off :", ('1', '0'))
            Helper.save_config('IS_REMOVE_FILES', mainConfig.IS_REMOVE_FILES)
            if mainConfig.IS_REMOVE_FILES == "1":
                mainConfig.REMOVE_FILE_AFTER_MINS = st.number_input("Define the interval in minutes to remove uploaded files:", value=0)
                Helper.save_config('REMOVE_FILE_AFTER_MINS', mainConfig.REMOVE_FILE_AFTER_MINS)
            # Continue with other configuration prompts

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

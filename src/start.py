import streamlit as st
import os
import sys
import json
import config as mainConfig
import helpers as Helper

# Define the Streamlit layout
def main():
    st.title("Terminal Configuration Setup")
    st.write("Welcome to the Configuration Setup!")
    st.write("Type 'help' to see available commands.")

    command = st.text_input(">>")

    if command.lower() == "help":
        st.write("Available commands:")
        st.write("1. start - Begin the configuration setup.")
        st.write("2. config - Load configuration from a JSON file.")
        st.write("3. launch - Directly launch the application.")
    elif command.lower() == "start":
        start_configuration()
    elif command.lower() == "config":
        config_from_file()
    elif command.lower() == "launch":
        st.write("Launching the application...")
        launch_app()
    elif command.strip():  # Check if the command is not empty
        st.write("Invalid command. Type 'help' to see available commands.")

# Function to load configuration from JSON file
def config_from_file():
    uploaded_file = st.file_uploader("Upload JSON file with configuration", type="json")
    if uploaded_file is not None:
        try:
            config_data = json.load(uploaded_file)
            st.write("Configurations loaded from file:")
            st.write(config_data)
            # Apply configuration from JSON file
            apply_config_from_file(config_data)
            st.write("Configuration applied.")
        except json.JSONDecodeError:
            st.write("Invalid JSON file.")

# Function to apply configuration from JSON file
def apply_config_from_file(config_data):
    for key, value in config_data.items():
        # Save each configuration value using Helper.save_config()
        Helper.save_config(key, value)

# Function to start configuration setup
def start_configuration():
    st.write("Starting configuration setup...")
    st.write("This option is not available when loading configuration from file.")

# Function to launch the application
def launch_app():
    python_executable_path = sys.executable
    os.system(python_executable_path + "../app.py 1")

# Run the Streamlit app
if __name__ == "__main__":
    main()

import configparser
import os
import platform
from datetime import date
import configparser
import os
import platform
from datetime import date

CONFIG = configparser.ConfigParser()
VERSION = "0.3.1"
YEAR = date.today().strftime("%Y")


# Check the location of the configuration file, default to the home directory
filename = "autotest.cfg"
config_location = ""

def get_config(dirname):
    global config_location
    config_location = os.path.join(dirname, filename)

    if not os.path.exists(config_location): 
        print(f"Config file not found. Creating default config at {config_location}")
        CONFIG["DEFAULT"] = {
            "screen shot index": "0",
            "test cases count": "0",
        }
        save_config() 

    try:
        CONFIG.read(config_location) 
    except Exception as e:
        print(f"Error reading config file: {e}")



def save_config():
    """Saves the current config to file."""
    try:
        with open(config_location, "w") as config_file:
            CONFIG.write(config_file)
        print(f"Config saved at {config_location}")
    except Exception as e:
        print(f"Error saving config: {e}")
from configparser import ConfigParser
import sys

config_read = ConfigParser()
config_read.read("config.ini")


# Error handling
try:
    months = int(config_read["USER TIME"]["MONTHS"])
    years = int(config_read["USER TIME"]["YEARS"])
    total_time = years * 12 + months
except ValueError:
    print("There is a ValueError, please input in numerical values")
    sys.exit(0)

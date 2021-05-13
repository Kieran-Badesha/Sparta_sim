from configparser import ConfigParser
import sys
import os

directory = os.path.dirname(__file__)
filename = os.path.join(directory, 'config.ini')
config_read = ConfigParser()
config_read.read(filename)


# Error handling
try:
    months = int(config_read["USER TIME"]["MONTHS"])
    years = int(config_read["USER TIME"]["YEARS"])
    min_trainees = int(config_read["TRAINEES"]["MIN_TRAINEES"])
    max_trainees = int(config_read["TRAINEES"]["MAX_TRAINEES"])
    total_time = years * 12 + months
except ValueError:
    print("There is a ValueError, please input in numerical values")
    sys.exit(0)


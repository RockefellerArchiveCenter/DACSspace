#!/usr/bin/env python

import os
import sys

current_dir = os.path.dirname(__file__)

file_path = os.path.join(current_dir, "local_settings.cfg")


def start_section(section_name):
    cfg_file.write("\n[{}]\n".format(section_name))


def write_value(name, default, value=None):
    if value:
        line = ("{}: {}\n".format(name, value))
    else:
        line = ("{}: {}\n".format(name, default))
    cfg_file.write(line)



def main():
    global cfg_file
    print("This script will create a configuration file with settings to connect and download JSON files from ArchivesSpace.\nYou\'ll need to know a few things in order to do this:\n\n1. The base URL of the backend of your ArchivesSpace installation, including the port number.\n2. The ID for the ArchivesSpace repository from which you want to export JSON files.\n3. A user name and password for a user with read writes to the ArchivesSpace repository.\n")
    response = input("Do you want to continue? (y/n): ")
    check_response(response, "y")

    if os.path.isfile(file_path):
        print("\nIt looks like a configuration file already exists. This script will replace that file.\n")
        response = input("Do you want to continue? (y/n): ")
        check_response(response, "y")

    cfg_file = open(file_path, 'w+')
    print("\nOK, let's create this file! I\'ll ask you to enter a bunch of values. If you want to use the default value you can just hit the Enter key.\n")
    start_section("ArchivesSpace")
    print("We\'ll start with some values for your ArchivesSpace instance.")
    baseURL = input(
        "Enter the base URL of your ArchivesSpace installation (default is 'http://localhost:8089'): ")
    write_value("baseURL", "http://localhost:8089", baseURL)
    repoId = input(
        "Enter the repository ID for your ArchivesSpace installation (default is '2'): ")
    write_value("repository", "2", repoId)
    username = input(
        "Enter the username for your ArchivesSpace installation (default is 'admin'): ")
    write_value("user", "admin", username)
    password = input(
        "Enter the password associated with this username (default is 'admin'): ")
    write_value("password", "admin", password)

    start_section("Destinations")
    print("\nNow you need to tell me where you want to save the spreadsheet that will be created. Unless you know what you\'re doing, you should probably leave the defaults in place.\n")
    directory = input(
        "Enter the directory in which you want to save the spreadsheet (default is the current directory): ")
    write_value("directory", "", directory)
    filename = input(
        "Now tell me the filename of the CSV spreadsheet you want to create (default is 'dacs_singlelevel_report.csv'): ")
    write_value("filename", "dacs_singlelevel_report.csv", filename)

    cfg_file.close()

    print("You\'re all set! I created a configuration file at {}. You can edit that file at any time, or run this script again if you want to replace those configurations.".format(file_path))

    sys.exit()


main()

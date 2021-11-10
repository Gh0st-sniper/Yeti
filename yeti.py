#!/usr/bin/python3 

from colorama import Fore
import requests
import sys
import time

url = input("Enter URL")
wordlist = input("Wordlist path")

print("\t\t\t\t ###### YETI \t\t\t")
print("\t\t\t\t ##### by surya-bug \t\t\t")
time.sleep(2)


def finder(url):
    try:
        resp = requests.get(url)
        return resp
    except requests.exceptions.ConnectionError:
        pass

file = open(wordlist,'r')

for line in file:
    word = line.strip()
    f_url = url + "/" + word
    response = finder(f_url)
    if(response):
        print(Fore.GREEN + "[++] Discovery::  {}".format(f_url))
    else:
        print(Fore.RED + "MISSED : {}".format(f_url))








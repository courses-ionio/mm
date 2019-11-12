#!/usr/bin/env python3
# Created by Selva <selva@selvasoft.in>
# © Selva
import requests
import argparse
import sys
from bs4 import BeautifulSoup
from terminaltables import SingleTable
from textwrap import wrap

baseURL = 'https://www.skytorrents.to/rss?search='

# Using in-built argparse library to parse the command line arguments 
parser = argparse.ArgumentParser(description="Search torrents from the command line easily.")
parser.add_argument('-i','--items',default=5,help='Number of items to display ( default: 5 )')
parser.add_argument('searchTerm',type=str,help='Search term to search for torrent')
args = parser.parse_args()
# Replacing the blank space(" ") with "+", since the URL doesnt have any blank space
searchTerm = args.searchTerm.replace(' ','+')
num = args.items
r = requests.get(baseURL+searchTerm)
soup = BeautifulSoup(r.text,'xml')
items = soup.find_all('item')
if len(items)==0:
    print('Item not found!!!')
    sys.exit()

def convertSize(size):
    size = round(size / 1024,2)
    suffix = 'KB'
    if size > 1000:
        size = round(size / 1024,2)
        suffix = 'MB'
    if size > 1000:
        size = round(size / 1024,2)
        suffix = 'GB'    
    if size > 1000:
        size = round(size / 1024,2)
        suffix = 'TB'
    return ( str(size) + ' ' + suffix )

list1 = [ ]
mgntList = [ ]
list1.append(['Index','Title','Date Added','Size','Seeders','Leechers'])
for i in range(int(num)):
    item = items[i]
    tempList = [ ]
    tempList.append(str(i+1))
    tempList.append(item.title.text)
    mgntList.append(item.magneturl.text)
    tempList.append(item.pubDate.text[5:16])
    tempList.append(convertSize(int(item.size.text)))
    seeders = item.find(attrs={'name':'seeders'})
    tempList.append(seeders['value'])
    peers = item.find(attrs={'name':'peers'})
    tempList.append(peers['value'])
    list1.append(tempList)


cuteTable = SingleTable(list1)
max_width = cuteTable.column_max_width(1)
for i in range(1,len(list1)):
    row = list1[i]
    wrappedString = '\n'.join(wrap(row[1], max_width))
    cuteTable.table_data[i][1] = wrappedString +'\n'
    
print(cuteTable.table)
choice = int(input('\nEnter the index--->'))
print('\nThe magnet link is :\n')
print(mgntList[choice])

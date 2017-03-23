import urllib.request as ul
import re
#uncomment below if working on python 2.x
#but then you need to change the student search code as well using python 2.x urllib2 instead of urllib.reqest
#from BeautifulSoup import *
from bs4 import BeautifulSoup
#import the file from different directory
import sys
sys.path.insert(0, 'Student_Search')
import st_search as ss
import web_scraper_linked as wsl

# make predictive.(i.e can handle common errors)
key = input('Enter the search query: ')
# for reg ex : we take key to be independent word
key = r'[\A\s]'+re.escape(key)+r'\s'
roll = 150001
limit_roll = 170000
url = 'http://home.iitk.ac.in/~'
#make a dictionary of all the links encountered having key
links_dic={}
to_visit=[]
max_entries = 100           #limit max entries for searches , we aren't using databses now so need to do this

while roll < limit_roll:
    while True:
        try:
            stud_data = ss.getStudentData(str(roll))
            # if program is not present as a key then we are done with this year student
            if 'Program: ' not in stud_data.keys():
                break
            user = stud_data[' E-Mail: '].split('@')[0]
        except:
            roll+=1
            continue
        end_url = url + str(user)
        #try to open the site
        try:
            data = ul.urlopen(end_url).read()
        except:
            roll+=1
            continue
        soup = BeautifulSoup(data, 'html.parser')
        #print(soup.prettify())
        #find key
        all_text = soup.get_text()
        # here rather than looking for the exact match i need to implement comment line #12
        if re.search(key,all_text,re.IGNORECASE):
            if end_url in links_dic.keys():
                links_dic[end_url]+=1
            else:
                links_dic[end_url]=1

        #find all links on that page containing the key
        links_to = wsl.scan_all_links(soup, key)
        #all_links = soup.find_all('a')
        print (roll, user)
        roll+=1
    roll=((roll//10000)+1)*10000+1

print (links_dic)
#CURRENTLY the code is able to access each person's account and look for 'a' tags and the key itself
#the process is rather slow, also the links on page may contain links that link back to same page so we need to avoid those.

import re
import urllib.request as ul
from bs4 import BeautifulSoup
#the arguments to be passed , soup  and key
def scan_all_links():
    url = 'http://home.iitk.ac.in/~rmanish/'
    data = ul.urlopen(url).read()
    soup = BeautifulSoup(data, 'html.parser')
    do_not_visit_these = ['#','facebook','linkedin','plus.google','instagram']
    all_links = soup.find_all('a')
    ln = []
    for lk in all_links:
        flag2 = False
        the_url = lk.get('href')
        if the_url == None or not the_url:
            continue
        for dn in do_not_visit_these:
            if re.search(dn,the_url,re.IGNORECASE):
                flag2=True
                break
        if flag2: continue
        ln.append(the_url)
    #remove duplicates
    ln=list(set(ln))
    print (ln)
    #print (all_links)

if __name__ == '__main__':
    scan_all_links()

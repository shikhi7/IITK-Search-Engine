import re
import urllib.request as ul
from bs4 import BeautifulSoup

MAX_DEPTH = 10
ln_with_key = []
#key = r'[\A\s]'+re.escape('esc101')+r'\s'
iterations = 0
#the arguments to be passed , soup  and key
def scan_all_links(url_list,key):
    global iterations
    if not url_list or iterations>MAX_DEPTH: return
    url = url_list[0]
    del url_list[0]
    data=''
    iterations+=1
    try:
        data = ul.urlopen(url).read()
    except:
        scan_all_links(url_list,key)
    soup = BeautifulSoup(data, 'html.parser')
    #although its possible to crawl qoura i am not doing that here
    do_not_visit_these = ['#','facebook','linkedin','plus.google','instagram','quora']
    #get all links on this page
    all_links = soup.find_all('a')
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
        url_list.append(the_url)

    #check if the current 'url' contains the key
    all_text = soup.get_text()
    if re.search(key, all_text, re.IGNORECASE):
        ln_with_key.append(url)
    scan_all_links(url_list,key)

def getRelatedList(url_list, key):
    global iterations, ln_with_key
    iterations = 0
    ln_with_key = []
    scan_all_links(url_list,key)
    return list(set(ln_with_key))[:]

#if __name__ == '__main__':
#    scan_all_links(['http://home.iitk.ac.in/~rmanish/'])
#    print (ln_with_key)

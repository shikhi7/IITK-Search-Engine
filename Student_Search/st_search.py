import urllib.request as ul
import urllib.parse
import re

x =input()
the_url = 'http://oa.cc.iitk.ac.in/Oa/Jsp/OAServices/IITk_SrchRes.jsp?sbm=Y'
values= {'numtxt':x,'typ':'stud'}

data = urllib.parse.urlencode(values)
data = data.encode('utf-8')

req = ul.Request(the_url,data)
resp = ul.urlopen(req)

respData = resp.read()
#readData has source code of result

fields = re.findall(r'<b>(.*?)</b>',str(respData))
result = re.findall(r'\\t([A-Za-z0-9]+[\w\.\d\s&\+\-,@]*)\\r',str(respData))
result.insert(5,re.findall(r'mailto:(.*?)\"',str(respData))[0])
del fields[0]
del fields[7]

student_dic={}
for x in range(len(result)):
            student_dic[fields[x]]=result[x]

print (student_dic)

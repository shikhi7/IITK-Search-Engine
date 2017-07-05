import urllib.request as ul
import urllib.parse
import re

# x is the roll no of the student about whom you want to gather info
def getStudentData(x):
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

    # for mail
    mail = re.findall(r'mailto:(.*?)\"',str(respData))
    if len(mail):
        result.insert(5,mail[0])
    else:
        result.insert(5,'Not Available')
    del fields[0]
    del fields[7]
    # for img
    img = re.findall(r'img src=\"http:(.*?)\"',str(respData))
    img[0]='http:'+img[0]

    student_dic={}
    for x in range(len(result)):
            student_dic[fields[x]]=result[x]
    student_dic['image']=img[0]
    #return student_dic[' E-Mail: ']
    return (student_dic)

shikhar=getStudentData(150669)
for keys,values in shikhar.items():
    print(keys)
    print(values)

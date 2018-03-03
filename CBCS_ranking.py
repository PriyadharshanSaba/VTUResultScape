#PD_SubsRETR : Fetch Movies Subtitles with One click!
#Creator / Developer Name : Priyadharshan Saba
#Script : Shell Script, Python, Apple Scripts
#Python Dependencis: mechanize, requests, beautifulSoup4, numpy (>=1.10), pandas
#Runtime : Python2


import sys
sys.path.append("/usr/local/lib/python2.7/site-packages")
import requests
import mechanize
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd



br = mechanize.Browser()
br.set_handle_robots(False)

def colist(x):
    college_list = ['1MV']

def getGrade(n):
    if n >= 90 :
        return 'S+',10
    elif n>=80 and n<90:
        return 'S',9
    elif n>=70 and n<80:
        return 'A',8
    elif n>=60 and n<70:
        return 'B',7
    elif n>=50 and n<60:
        return 'C',6
    elif n>=45 and n<50:
        return 'D',5
    elif n>=40 and n<45:
        return 'E',4
    else:
        return 'F',0

def fetch(branch):
    hashcheck=0
    check_notnull=False
    usns , names, gpas, level_flag = [], [], [], []

    for usn_i in range(1,130):
        try:
            if usn_i<10:
                fusn_i="00"+str(usn_i)
            elif usn_i>=10 and usn_i<100:
                fusn_i="0"+str(usn_i)
            elif usn_i>=100:
                fusn_i=str(usn_i)

            uid="1MV15"+str(branch)+str(fusn_i)
            level_flag.append('u')
            usns.append(uid)
            br.open("http://results.vtu.ac.in/vitaviresultcbcs/index.php")
            br.select_form(nr=0)
            br.form['lns'] = uid
            sub = br.submit()
            soup = BeautifulSoup(sub.read(),"lxml")

            for td in soup.findAll('td',{'style':'padding-left:15px;text-transform:uppercase'}):
                student_usn = td.text[3:].upper()

                if student_usn!=None and hashcheck<5:
                    hashcheck=0
                    check_notnull=True

                elif hashcheck>=5:
                    break

                else:
                    hashcheck=hashcheck+1
                    check_notnull=False

            if check_notnull==True:
                flag=0
                for i in soup.findAll('td'):
                    if i.text.strip(' ') == "Student Name":
                        flag+=1
                    elif flag==1:
                        student_name = i.text.strip(" : ")
                        flag=0
                level_flag.append('n')
                names.append(capitalize(student_name))
                mar = ['mark']
                print student_usn,student_name
                for div in soup.findAll('div',{'style':'text-align: left;width: 400px;'}):
                    i=1
                    j=1
                    k=6
                    l=1
                    for div in soup.findAll('div',{'class':'divTableCell'}):
                        if i==6:
                            if j % k ==0:
                                mar.append(div.text)
                                k=k+1
                                l+=1
                            else:
                                j+=1
                        else:
                            i+=1
                finalm = [mar[1]]
                for i in xrange(4,len(mar),3):
                    if i <=24:
                        finalm.append(mar[i])
                    else:
                        break
                grad = ['g']
                gp = [-1]
                for i in finalm:
                    gx=getGrade(int(i))
                    grad.append(gx[0])
                    gp.append(gx[1])

                sum=0
                grad.remove('g')
                gp.remove(-1)
                for i in range(0,len(gp)):
                    if i==1 or i==3:
                        sum += gp[i]*3.0
                    elif i>=6:
                        sum+=gp[i]*2.0
                    else:
                        sum+=gp[i]*4.0
                level_flag.append('g')
                gpas.append(str(sum/26)[:4])
                print sum/26,"\n\n"
                del finalm[:]
                del mar[:]
                sum=0
                del level_flag[:]
        except:
            del mar[:]
            print level_flag
            for i in level_flag:
                if i=='u':
                    del usns[-1]
                elif i=='n':
                    del names[-1]
                else:
                    del gpas[-1]
            del level_flag[:]
            try:
                del finalm[:]
                continue
            except:
                continue

    # Creating Dataframes
    df = pd.DataFrame({'usn':usns,'name':names,'gpa':gpas})
    df.to_csv('dataset.csv', sep='\t', encoding='utf-8')
    print df

def capitalize(name):
    sname=''
    for i in name.split(' '):
        sname=sname+(i[:1].upper()+i[1:].lower())+" "
    return sname


#Main
branch_list = ['CS','IS','EE','EC','ME','BT','CV']
for i in branch_list:
    fetch(i)



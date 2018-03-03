#http://results.vtu.ac.in/cbcs_17/result_page.php?usn=1mv15cs088

from bs4 import BeautifulSoup
import requests
import csv


subCode=[None]*10
subName=[None]*10
subInternal=[None]*10
subExternal=[None]*10
subPass=[None]*10


"""
college_code=['VA','RN']    #'MV','AY','BI','BY','DS','VA']
college_region=['1','2','3','4']
batch_year="15"
batch_course="CS"
"""

"""with open('cs_blr_iv.csv', 'wb') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',',quotechar=' ', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(['USN','Name','Subcode1','Subname1','Internalmarks1','Externalmarks1','Subpass1','Subcode2','Subname2','Internalmarks2','Externalmarks2','Subpass2','Subcode3','Subname3','Internalmarks3','Externalmarks3','Subpass3','Subcode4','Subname4','Internalmarks4','Externalmarks4','Subpass4','Subcode5','Subname5','Internalmarks5','Externalmarks5','Subpass5','Subcode6','Subname6','Internalmarks6','Externalmarks6','Subpass6','Lab1','Labname1','Internalmarksl1','Externalmarksl1','Subpassl1','Lab2','Labname2','Internalmarksl2','Externalmarksl2','Subpassl2'])"""



for hashcc in range(0,1):

    hashcheck=0
    check_notnull=False

    for usn_i in range(98,131):
        if usn_i<10:
            fusn_i="00"+str(usn_i)
        elif usn_i>=10 and usn_i<100:
            fusn_i="0"+str(usn_i)
        elif usn_i>=100:
            fusn_i=str(usn_i)

#        final_url = "http://results.vtu.ac.in/cbcs_17/result_page.php?usn="+college_region[0]+college_code[hashcc]+batch_year+batch_course+fusn_i
        final_url="http://results.vtu.ac.in/cbcs_17/result_page.php?usn=1MV15CS"+fusn_i
        url=final_url
        print url
        #url = "http://results.vtu.ac.in/cbcs_17/result_page.php?usn=1mv15cs088"
        re = requests.get(url)
        soup = BeautifulSoup(re.content,"lxml")

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
            for td in soup.findAll('td',{'style':'padding-left:15px'}):
                student_name = td.text[2:].upper()
                print student_name

            for td in soup.findAll('table',{'class':'table table-bordered'}):
                mark_meta=td.text.split("\n")
                try:
                    for mar_i in range(0,8):
                        subCode[mar_i]=mark_meta[((mar_i+1)*10)+3]
                        subName[mar_i]=mark_meta[((mar_i+1)*10)+4]
                        subInternal[mar_i]=int(mark_meta[((mar_i+1)*10)+5])
                        subExternal[mar_i]=int(mark_meta[((mar_i+1)*10)+6])
                        subPass[mar_i]=mark_meta[((mar_i+1)*10)+8]
                    with open('cs_blr_iv.csv', 'a') as csvfile:
                        spamwriter = csv.writer(csvfile, delimiter=',',quotechar=' ', quoting=csv.QUOTE_MINIMAL)
                        spamwriter.writerow([student_usn,student_name,subCode[0],subName[0],subInternal[0],subExternal[0],subPass[0],subCode[1],subName[1],subInternal[1],subExternal[1],subPass[1],subCode[2],subName[2],subInternal[2],subExternal[2],subPass[2],subCode[3],subName[3],subInternal[3],subExternal[3],subPass[3],subCode[4],subName[4],subInternal[4],subExternal[4],subPass[4],subCode[5],subName[5],subInternal[5],subExternal[5],subPass[5],subCode[6],subName[6],subInternal[6],subExternal[6],subPass[6],subCode[7],subName[7],subInternal[7],subExternal[7],subPass[7],subCode[8],subName[8],subInternal[8],subExternal[8],subPass[8]])
                except:
                    break


"""
    final_url="http://results.vtu.ac.in/cbcs_17/result_page.php?usn=1MV15CS088"
    re = requests.get(final_url)
    soup = BeautifulSoup(re.content,"lxml")
    for td in soup.findAll('td',{'style':'padding-left:15px'}):
    student_name = td.text[2:].upper()
    """


#[u0'', u1'', u2'', u3'Subject Code', u4'Subject Name', u5'Internal Marks', u6'External Marks', u7'Total', u8'Result', u'', u'', u'', u'', u'15MAT41', u'ENGINEERING MATHEMATICS-IV', u'16', u'49', u'65', u'P', u'', u'', u'', u'', u'15CS42', u'SOFTWARE ENGINEERING', u'13', u'28', u'41', u'P', u'', u'', u'', u'', u'15CS43', u'DESIGN AND ANALYSIS OF ALGORITHMS', u'13', u'65', u'78', u'P', u'', u'', u'', u'', u'15CS44', u'MICROPROCESSORS AND MICROCONTROLLERS', u'20', u'28', u'48', u'P', u'', u'', u'', u'', u'15CS45', u'OBJECT ORIENTED PROGRAMMING WITH JAVA', u'17', u'46', u'63', u'P', u'', u'', u'', u'', u'15CS46', u'DATA COMMUNICATIONS', u'14', u'38', u'52', u'P', u'', u'', u'', u'', u'15CSL47', u'DESIGN AND ANALYSIS OF ALGORITHM LABORATORY', u'20', u'70', u'90', u'P', u'', u'', u'', u'', u'15CSL48', u'MICROPROCESSORS LABORATORY', u'15', u'78', u'93', u'P', u'', u'', u'']

import pandas as pd
import numpy as np
import matplotlib.pyplot as pl
import datetime
from datetime import date
from datetime import timedelta

#movies
def displaymovie():
    print('Movies')
    mov=pd.read_csv('D:\\OTT Platform Management\\MOVIES.csv')
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    print(mov)
    print()
    ans=input('Do you want to go back [Yes or No] ? ')
    if ans=='Yes':
        print(moviemenu())
    else:
        displaymovie()
    
def addmovie():
    ans=input('Do you want to add records ? ')
    while ans=='yes' or ans=='y' or ans=='Yes' or ans=='Y':
        mov=pd.read_csv('D:\\OTT Platform Management\\MOVIES.csv')
        i=mov['ID'].max()+1
        title=input('Enter title of movie : ')
        date=input('Enter release date : ')
        lang=input('Enter languages available : ')
        pro=input('Enter producer of movie : ')
        cer=input('Enter certificate: ')
        cou=input('Enter country: ')
        gen=input('Enter genre of the movie : ')
        dur=input('Enter duration of the movie : ')
        run=input('Enter runtime of the movie : ')
        imbd=input('Enter IMBD ratings of the movie : ')
        gro=input('Enter gross amount : ')
        print()
        mov.loc[len(mov)]=[i,title,date,lang,pro,cer,cou,gen,dur,run,imbd,gro]
        mov.to_csv('D:\\OTT Platform Management\\MOVIES.csv',index=False)
        pd.set_option('display.max_rows', None)
        pd.set_option('display.max_columns', None)
        pd.set_option('display.width', None)
        print(mov)
        print()
        ans=input('Do you want to add more records ? ')
    else:
        print()
        print(moviemenu())
    
def updatemovie():
    ans=input('Do you want to update records ? ')
    while ans=='y' or ans=='Y' or ans=='yes' or ans=='Yes':
        mov=pd.read_csv('D:\\OTT Platform Management\\MOVIES.csv',index_col='ID')
        pd.set_option('display.max_rows', None)
        pd.set_option('display.max_columns', None)
        pd.set_option('display.width', None)
        print(mov)
        i=int(input('Enter ID of movie to be updated : '))
        print()
        if i in mov.index:
            print('Select column :')
            print(mov.columns)
            c=input('Enter column to be updated : ')
            v=input('Enter new value : ')
            mov.loc[i,c]=v
            mov.to_csv('D:\\OTT Platform Management\\MOVIES.csv')
            print()
            print('Record updated successfully!')
            print()
            print(mov.loc[i,:])
        else:
            print('ID does not exist!')
        ans=input('Do you want to update more records ? ')
    else:
        print()
        print(moviemenu())
    
def deletemovie():
    mov=pd.read_csv('D:\\OTT Platform Management\\MOVIES.csv',index_col='ID') 
    ans=input('Do you want to delete records ? ')
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    print(mov)
    print()
    while ans=='yes' or ans=='y' or ans=='Yes' or ans=='Y':
        i=int(input('Enter ID of movie to be deleted : '))
        if i in mov.index:
            mov=mov.drop(i,axis=0)
            print(mov)
            print()
            mov.to_csv('D:\\OTT Platform Management\\MOVIES.csv')
            print('Record deleted successfully!')
        else:
            print('ID does not exist!')
        ans=input('Do you want to delete more records ? ')
    else:
        print()
        print(moviemenu())

def searchmovie():
    mov=pd.read_csv('D:\\OTT Platform Management\\MOVIES.csv',index_col='TITLE') 
    ans=input('Do you want search for records ? ')
    while ans=='yes' or ans=='y' or ans=='Yes' or ans=='Y':
        t=input('Enter title of the movie : ')
        print()
        if t in mov.index:
            print(mov.loc[t])
        else:
            print('Record does not exist')
        ans=input('Do you want to continue ? ')
    else:
        print()
        print(moviemenu())
        
#series
def displayseries():
    print('SERIES AVAILABLE')
    ser=pd.read_csv('D:\\OTT Platform Management\\SERIES.csv')
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    print(ser)
    print()
    ans=input('Do you want to go back [Yes or No] ? ')
    if ans=='Yes':
        print(seriesmenu())
    else:
        displayseries()
    
def addseries():
    ans=input('Do you want to add a record ? ')
    while ans=='Y' or ans=='y' or ans=='yes' or ans=='Yes':
        df=pd.read_csv('D:\\OTT Platform Management\\SERIES.csv')
        print()
        print('Enter records for the following columns :',df.columns)
        print()
        sno=df['Sr.No'].max()+1
        tit=input('Enter title : ')
        rat=float(input('Enter ratings : '))
        l=input('Enter language : ')
        rda=input('Enter release date : ')
        gen=input('Enter genre : ')
        run=input('Enter runtime of the series : ')
        epi=input('Enter total number of episode in the series : ')
        gro=input('Enter gross amount of the series : ')
        sea=input('Enter total number of seasons of the series : ')
        print()
        df.loc[len(df)]=[sno,tit,rat,l,rda,gen,run,epi,gro,sea]
        df.to_csv('D:\\OTT Platform Management\\SERIES.csv',index=False)
        pd.set_option('display.max_rows', None)
        pd.set_option('display.max_columns', None)
        pd.set_option('display.width', None)
        print(df)
        ans=input('Do you want to continue ? ')
    else:
        print()
        print(seriesmenu())
        
def updateseries():
    ans=input('Do you want to update records ? ')
    while ans=='y' or ans=='Y' or ans=='yes' or ans=='Yes':
        ser=pd.read_csv('D:\\OTT Platform Management\\SERIES.csv',index_col='Sr.No')
        pd.set_option('display.max_rows', None)
        pd.set_option('display.max_columns', None)
        pd.set_option('display.width', None)
        print(ser)
        i=int(input('Enter ID of series to be updated : '))
        print(ser.loc[i,:])
        if i in ser.index:
            print('Select column :')
            print(ser.columns)
            c=input('Enter column to be updated : ')
            v=input('Enter new value : ')
            ser.loc[i,c]=v
            ser.to_csv('D:\\OTT Platform Management\\SERIES.csv')
            print()
            print('Record updated successfully!')
            print()
            print(ser.loc[i,:])
        else:
            print('ID does not exist!')
        ans=input('Do you want to update more records ? ')
    else:
        print()
        print(seriesmenu())
        
def deleteseries():
    ser=pd.read_csv('D:\\OTT Platform Management\\SERIES.csv',index_col='Sr.No')
    ans=input('Do you want to delete records ? ')
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    print(ser)
    while ans=='y' or ans=='Yes' or ans=='Y' or ans=='yes':
        i=int(input('Enter ID of series to be deleted : '))
        if i in ser.index:
            ser=ser.drop(i,axis=0)
            print(ser)
            print()
            ser.to_csv('D:\\OTT Platform Management\\SERIES.csv')
            print('Record deleted successfully!')
        else:
            print('ID does not exist!')
        ans=input('Do you want to delete more records ? ')
    else:
        print()
        print(seriesmenu())
    
def searchseries():
    ser=pd.read_csv('D:\\OTT Platform Management\\SERIES.csv',index_col='Title')
    ans=input('Do you want to search for records ? ')
    while ans=='y' or ans=='Y' or ans=='yes ' or ans=='Yes':
        t=input('Enter title of series to be searched for : ')
        if t in ser.index:
            print(ser.loc[t,:])
        else:
            print('Series not available!')
        ans=input('Do you want to search for more records ? ')
    else:
        print()
        print(seriesmenu())

#workforce
def displayworkforce():
    wf=pd.read_csv('D:\\OTT Platform Management\\WORKFORCE.csv')
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    print('WORKFORCE DETAILS')
    print(wf)
    print()
    ans=input('Do you want to go back [Yes or No] ? ')
    if ans=='Yes':
        print(workforcemenu())
    else:
        displayworkforce()

def addemployee():
    wf=pd.read_csv('D:\\OTT Platform Management\\WORKFORCE.csv')
    ans=input('Do you want to add records ? ')
    while ans=='y' or ans=='Y' or ans=='Yes' or ans=='yes':
        print('Enter records for the following columns :',wf.columns)
        print()
        i=wf['S-ID'].max()+1
        n=input('Enter name of employee : ')
        cn=int(input('Enter contact number : '))
        sal=float(input('Enter salary of employee : '))
        g=input('Enter gender of employee : ')
        p=input('Enter post of employee : ')
        wf.loc[len(wf)]=[i,n,cn,sal,g,p]
        wf.to_csv('D:\\OTT Platform Management\\WORKFORCE.csv',index=False)
        pd.set_option('display.max_rows', None)
        pd.set_option('display.max_columns', None)
        pd.set_option('display.width', None)
        print(wf)
        ans=input('Do you want to continue ? ')
    else:
        print()
        print(workforcemenu())

def updateemployee():
     ans=input('Do you want to update records ? ')
     while ans=='y' or ans=='Y' or ans=='yes' or ans=='Yes':
        wf=pd.read_csv('D:\\OTT Platform Management\\WORKFORCE.csv',index_col='S-ID')
        pd.set_option('display.max_rows', None)
        pd.set_option('display.max_columns', None)
        pd.set_option('display.width', None)
        print(wf)
        print()
        i=int(input('Enter ID of employee to be updated : '))
        print(wf.loc[i,:])
        print()
        if i in wf.index:
            print('Select column :')
            print(wf.columns)
            c=input('Enter column to be updated : ')
            v=input('Enter new value : ')
            wf.loc[i,c]=v
            wf.to_csv('D:\\OTT Platform Management\\WORKFORCE.csv')
            print()
            print('Record updated successfully!')
            print()
            print(wf.loc[i,:])
            print()
        else:
            print('ID does not exist!')
            print()
        ans=input('Do you want to update more records ? ')
        print()
        print(workforcemenu())
        
def deleteemployee():
    wf=pd.read_csv('D:\\OTT Platform Management\\WORKFORCE.csv',index_col='S-ID')
    ans=input('Do you want to delete records ? ')
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    print(wf)
    print()
    while ans=='y' or ans=='Yes' or ans=='Y' or ans=='yes':
        i=int(input('Enter ID of employee to be deleted : '))
        print()
        if i in wf.index:
            wf=wf.drop(i,axis=0)
            print(wf)
            print()
            wf.to_csv('D:\\OTT Platform Management\\WORKFORCE.csv')
            print('Record deleted successfully!')
            print()
        else:
            print('ID does not exist!')
            print()
        ans=input('Do you want to delete more records ? ')
    else:
        print()
        print(workforcemenu())

def searchemployee():
    wf=pd.read_csv('D:\\OTT Platform Management\\WORKFORCE.csv',index_col='NAME') 
    ans=input('Do you want search for records ? ')
    while ans=='yes' or ans=='y' or ans=='Yes' or ans=='Y':
        t=input('Enter name of employee : ')
        print()
        if t in wf.index:
            print(wf.loc[t])
            print()
        else:
            print('Record does not exist')
            print()
        ans=input('Do you want to continue ? ')
    else:
        print()
        print(workforcemenu())

#membership
def displaymember():
    mb=pd.read_csv('D:\\OTT Platform Management\\MEMBERSHIP.csv')
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    print('MEMBERSHIP DETAILS')
    print(mb)
    print()
    ans=input('Do you want to go back [Yes or No] ? ')
    if ans=='Yes':
        print(membershipmenu())
    else:
        displaymember()

def updatemember():
    ans=input('Do you want to update records ? ')
    mb=pd.read_csv('D:\\OTT Platform Management\\MEMBERSHIP.csv',index_col='M-ID')
    while ans=='y' or ans=='Y' or ans=='yes' or ans=='Yes':
        pd.set_option('display.max_rows', None)
        pd.set_option('display.max_columns', None)
        pd.set_option('display.width', None)
        print(mb)
        i=int(input('Enter ID of member to be updated : '))
        print()
        print(mb.loc[i,:])
        print()
        if i in mb.index:
            print('Select column :')
            print(mb.columns)
            print()
            c=input('Enter column to be updated : ')
            v=input('Enter new value : ')
            mb.loc[i,c]=v
            mb.to_csv('D:\\OTT Platform Management\\MEMBERSHIP.csv')
            print()
            print('Record updated successfully!')
            print()
            print(mb)
        else:
            print('ID does not exist!')
        ans=input('Do you want to update more records ? ')
    else:
        print()
        print(membershipmenu())


def searchmember():
    mb=pd.read_csv('D:\\OTT Platform Management\\MEMBERSHIP.csv',index_col='NAME') 
    ans=input('Do you want search for records ? ')
    while ans=='yes' or ans=='y' or ans=='Yes' or ans=='Y':
        t=input('Enter name of member : ')
        print()
        if t in mb.index:
            print(mb.loc[t])
            print()
        else:
            print('Record does not exist')
            print()
        ans=input('Do you want to continue ? ')
    else:
        print()
        print(membershipmenu())

    
#transactions
d={'TYPE':['A','B','C'],'PLAN':['SILVER','GOLD','PLATINUM'],'PRICE':[199,699,1669],'PLAN PERIOD':['30 DAYS','180 DAYS','356 DAYS']}
plan=pd.DataFrame(d)

def applyms():
    print('-------------------------------')
    print('1. New Member                  ')
    print('2. Existing Member             ')
    print('3. Exit                        ')
    ch=int(input('Enter your choice [1-3] : '))
    if ch==1:
        newms()
    elif ch==2:
        oldms()
    else:
        ans=input('Do you want to return to main menu [Yes or No] ? ')
        if ans=='Yes': 
            print()
            print(menu())
        else:
            applyms()
    
def newms():
    ans=input('Do you want to apply for membership ? ')
    while ans=='Yes' or ans=='yes' or ans=='Y' or ans=='y':
        mb=pd.read_csv('D:\\OTT Platform Management\\MEMBERSHIP.csv',index_col='M-ID')
        trans=pd.read_csv('D:\\OTT Platform Management\\TRANSACTIONS.csv')
        i=trans['M-ID'].max()+1
        n=input('Enter name of member : ')
        print('Choose your plan : ')
        print(plan)
        mt=input('Enter membership type : ')
        cd=date.today()
        y=cd.year
        m=cd.month
        d=cd.day
        cd=date(y,m,d)
        pm=input('Choose payment method [CARD OR NET BANKING] : ')
        if mt=='A':
            mp=plan.at[0,'PLAN']
            total=plan.at[0,'PRICE']
            nd=cd+timedelta(days=30)
        elif mt=='B':
            mp=plan.at[1,'PLAN']
            total=plan.at[1,'PRICE']
            nd=cd+timedelta(days=180)
        elif mt=='C':
            mp=plan.at[2,'PLAN']
            total=plan.at[2,'PRICE']
            nd=cd+timedelta(days=365)
        else :
            print('Enter valid plan.')
            newms()
        mb.loc[len(mb)+1]=[n,mt]
        mb.to_csv('D:\\OTT Platform Management\\MEMBERSHIP.csv')
        print()
        trans.loc[len(trans)+1]=[i,cd,n,mt,mp,cd,nd,pm,total]
        trans.to_csv('D:\\OTT Platform Management\\TRANSACTIONS.csv',index=False)
        pd.set_option('display.max_rows', None)
        pd.set_option('display.max_columns', None)
        pd.set_option('display.width', None)
        print()
        print('-------------------YOLO-------------------')
        print('                  RECEIPT                 ')
        print('Name of Member :',n)
        print('Membership Type :',mt)
        print('Membership Plan :',mp)
        print('Start of Service Period :',cd)
        print('End of Service Period :',nd)
        print('Mode of Payment :',pm)
        print('Total :',total)
        print(datetime.datetime.now())
        print('-----------------------------------------')
        print()
        ans=input('Do you want to continue ? ')
    else:
        print()
        print(applyms())

def oldms():
    ans=input('Do you want to renew your membership ? ')
    while ans=='Yes' or ans=='Y' or ans=='y' or ans=='yes':
        mb=pd.read_csv('D:\\OTT Platform Management\\MEMBERSHIP.csv',index_col='NAME')
        print(mb)
        trans=pd.read_csv('D:\\OTT Platform Management\\TRANSACTIONS.csv')
        i=trans['M-ID'].max()+1
        n=input('Enter your name : ')
        if n in mb.index:
            mt1=mb.loc[n,:]
            mt=mt1[1:]
            mt=mt.to_string(index=False)
        cd=date.today()
        y=cd.year
        m=cd.month
        d=cd.day
        cd=date(y,m,d)
        pm=input('Choose payment method [CARD OR NET BANKING] : ')
        if mt=='A':
            mp=plan.at[0,'PLAN']
            total=plan.at[0,'PRICE']
            nd=cd+timedelta(days=30)
        elif mt=='B':
            mp=plan.at[1,'PLAN']
            total=plan.at[1,'PRICE']
            nd=cd+timedelta(days=180)
        elif mt=='C':
            mp=plan.at[2,'PLAN']
            total=plan.at[2,'PRICE']
            nd=cd+timedelta(days=365)
        else :
            print('Enter valid plan.')
        print()
        print('-------------------YOLO-------------------')
        print('                  RECEIPT                 ')
        print('Name of Member :',n) 
        print('Membership Type :',mt)
        print('Membership Plan :',mp)
        print('Start of Service Period :',cd)
        print('End of Service Period :',nd)
        print('Mode of Payment :',pm)
        print('Total :',total)
        print(datetime.datetime.now())
        print('------------------------------------------')
        print()
        trans.loc[len(trans)+1]=[i,cd,n,mt,mp,cd,nd,pm,total]
        trans.to_csv('D:\\OTT Platform Management\\TRANSACTIONS.csv',index=False)
        pd.set_option('display.max_rows', None)
        pd.set_option('display.max_columns', None)
        pd.set_option('display.width', None)
        ans=input('Do you want to continue ? ')
    else:
        print()
        print(applyms())

def cancelms():
    ans=input('Do you want to cancel your membership ? ')
    while ans=='Yes' or ans=='yes' or ans=='Y' or ans=='y':
        mb=pd.read_csv('D:\\OTT Platform Management\\MEMBERSHIP.csv',index_col='NAME')
        n=input('Enter your name : ')
        if n in mb.index:
            mb=mb.drop(n,axis=0)
            pd.set_option('display.max_rows', None)
            pd.set_option('display.max_columns', None)
            pd.set_option('display.width', None)
            print(mb)
            print()
            print('Membership Cancelled!')
            mb.to_csv('D:\\OTT Platform Management\\MEMBERSHIP.csv')
        else:
            print('You are not a member yet.')
        ans=input('Enter "back" to return : ')
    else:
        print(transactionmenu())
        
    
#movieanalytics
def maxrtcon():
    mov=pd.read_csv('D:\\OTT Platform Management\\MOVIES.csv')
    a=mov.groupby('COUNTRY')['RUNTIME'].max()
    print(a)
    print()
    ans=input('Do you want to go back [Yes or No] ? ')
    if ans=='Yes':
        print(movieanalytics())
    else:
        maxrtcon()

def minrtcon():
    mov=pd.read_csv('D:\\OTT Platform Management\\MOVIES.csv')
    a=mov.groupby('COUNTRY')['RUNTIME'].min()
    print(a)
    print()
    ans=input('Do you want to go back [Yes or No] ? ')
    if ans=='Yes':
        print(movieanalytics())
    else:
        minrtcon()

def maxgrgen():
    mov=pd.read_csv('D:\\OTT Platform Management\\MOVIES.csv')
    a=mov.groupby('GENRE')['GROSS'].max()
    print(a)
    print()
    ans=input('Do you want to go back [Yes or No] ? ')
    if ans=='Yes':
        print(movieanalytics())
    else:
        maxgrgen()

def mingrgen():
    mov=pd.read_csv('D:\\OTT Platform Management\\MOVIES.csv')
    a=mov.groupby('GENRE')['GROSS'].min()
    print(a)
    print()
    ans=input('Do you want to go back [Yes or No] ? ')
    if ans=='Yes':
        print(movieanalytics())
    else:
        mingrgen()

def maxrtlang():
    mov=pd.read_csv('D:\\OTT Platform Management\\MOVIES.csv')
    a=mov.groupby('LANGUAGE')['RATING'].max()
    print(a)
    print()
    ans=input('Do you want to go back [Yes or No] ? ')
    if ans=='Yes':
        print(movieanalytics())
    else:
        maxrtlang()

def minrtlang():
    mov=pd.read_csv('D:\\OTT Platform Management\\MOVIES.csv')
    a=mov.groupby('LANGUAGE')['RATING'].min()
    print(a)
    print()
    ans=input('Do you want to go back [Yes or No] ? ')
    if ans=='Yes':
        print(movieanalytics())
    else:
        minrtlang()

def maxrtdt():
    mov=pd.read_csv('D:\\OTT Platform Management\\MOVIES.csv')
    mov['RELEASE DATE']=pd.to_datetime(mov['RELEASE DATE'],dayfirst=True)
    mov['YEAR']=mov['RELEASE DATE'].dt.year
    a=mov.groupby('YEAR')['RATING'].max()
    print(a)
    print()
    ans=input('Do you want to go back [Yes or No] ? ')
    if ans=='Yes':
        print(movieanalytics())
    else:
        maxrtdt()

def minrtdt():
    mov=pd.read_csv('D:\\OTT Platform Management\\MOVIES.csv')
    mov['RELEASE DATE']=pd.to_datetime(mov['RELEASE DATE'],dayfirst=True)
    mov['YEAR']=mov['RELEASE DATE'].dt.year
    a=mov.groupby('YEAR')['RATING'].min()
    print(a)
    print()
    ans=input('Do you want to go back [Yes or No] ? ')
    if ans=='Yes':
        print(movieanalytics())
    else:
        maxrtdt()

#seriesanalytics
def maxsrty():
    ser=pd.read_csv('D:\\OTT Platform Management\\SERIES.csv')
    ser['Release Date']=pd.to_datetime(ser['Release Date'],dayfirst=True)
    ser['Year']=ser['Release Date'].dt.year
    a=ser.groupby('Year')['Runtime'].max()
    print(a)
    print()
    ans=input('Do you want to go back [Yes or No] ? ')
    if ans=='Yes':
        print(seriesanalytics())
    else:
        maxsrty()

def minsrty():
    ser=pd.read_csv('D:\\OTT Platform Management\\SERIES.csv')
    ser['Release Date']=pd.to_datetime(ser['Release Date'],dayfirst=True)
    ser['Year']=ser['Release Date'].dt.year
    a=ser.groupby('Year')['Runtime'].min()
    print(a)
    print()
    ans=input('Do you want to go back [Yes or No] ? ')
    if ans=='Yes':
        print(seriesanalytics())
    else:
        minsrty()

    
def maxsgrgen():
    ser=pd.read_csv('D:\\OTT Platform Management\\SERIES.csv')
    a=ser.groupby('Genre')['Gross'].max()
    print(a)
    print()
    ans=input('Do you want to go back [Yes or No] ? ')
    if ans=='Yes':
        print(seriesanalytics())
    else:
        maxsgrgen()

def minsgrgen():
    ser=pd.read_csv('D:\\OTT Platform Management\\SERIES.csv')
    a=ser.groupby('Genre')['Gross'].min()
    print(a)
    print()
    ans=input('Do you want to go back [Yes or No] ? ')
    if ans=='Yes':
        print(seriesanalytics())
    else:
        minsgrgen()
  
def maxrtingy():
    ser=pd.read_csv('D:\\OTT Platform Management\\SERIES.csv')
    ser['Release Date']=pd.to_datetime(ser['Release Date'],dayfirst=True)
    ser['Year']=ser['Release Date'].dt.year
    a=ser.groupby('Year')['Ratings'].max()
    print(a)
    print()
    ans=input('Do you want to go back [Yes or No] ? ')
    if ans=='Yes':
        print(seriesanalytics())
    else:
        maxrtingy()
    

def minrtingy():
    ser=pd.read_csv('D:\\OTT Platform Management\\SERIES.csv')
    ser['Release Date']=pd.to_datetime(ser['Release Date'],dayfirst=True)
    ser['Year']=ser['Release Date'].dt.year
    a=ser.groupby('Year')['Ratings'].min()
    print(a)
    print()
    ans=input('Do you want to go back [Yes or No] ? ')
    if ans=='Yes':
        print(seriesanalytics())
    else:
        minrtingy()
   
def maxsgen():
    ser=pd.read_csv('D:\\OTT Platform Management\\SERIES.csv')
    a=ser.groupby('Genre')['Seasons'].max()
    print(a)
    print()
    ans=input('Do you want to go back [Yes or No] ? ')
    if ans=='Yes':
        print(seriesanalytics())
    else:
        maxsgen()
    
def minsgen():
    ser=pd.read_csv('D:\\OTT Platform Management\\SERIES.csv')
    a=ser.groupby('Genre')['Seasons'].min()
    print(a)
    print()
    ans=input('Do you want to go back [Yes or No] ? ')
    if ans=='Yes':
        print(seriesanalytics())
    else:
        minsgen()

#memberandplananalytics
def maxpm():
    mb=pd.read_csv('D:\\OTT Platform Management\\MEMBERSHIP.csv')
    a=mb['MEMBERSHIP PLAN'].value_counts()
    print()
    print('Most Popular Membership :',a.index[0])
    print()
    ans=input('Do you want to go back [Yes or No] ? ')
    if ans=='Yes':
        print(mpanalytics())
    else:
        maxpm()

def minpm():
    mb=pd.read_csv('D:\\OTT Platform Management\\MEMBERSHIP.csv')
    a=mb['MEMBERSHIP PLAN'].value_counts()
    print()
    print('Least Popular Membership :',a.index[len(a)-1])
    print()
    ans=input('Do you want to go back [Yes or No] ? ')
    if ans=='Yes':
        print(mpanalytics())
    else:
        minpm()

#movievisualisation
def movratyear():
    mov=pd.read_csv('D:\\OTT Platform Management\\MOVIES.csv')
    mov['RELEASE DATE']=pd.to_datetime(mov['RELEASE DATE'],dayfirst=True) #conversion of series to date format
    b=mov['RELEASE DATE'].dt.year
    a=mov.groupby(b)['RATING'].mean()
    year=list(a.index)
    avg=list(a.values)
    pl.plot(year,avg)
    pl.title('Average Yearly Ratings Graph')
    pl.xlabel('Year')
    pl.ylabel('Average Ratings')
    pl.show()
    ans=input('Do you want to go back [Yes or No] ? ')
    if ans=='Yes':
        print(movievisual())
    else:
        movratyear()
    
def movgrosgenr():
    mov=pd.read_csv('D:\\OTT Platform Management\\MOVIES.csv')
    s=mov['GENRE']
    v=mov['GROSS']
    pl.bar(s,v,width=0.25,color='m')
    pl.title('GROSS V/S GENRE')
    pl.xlabel('Genre')
    pl.ylabel('Gross')
    pl.ylim(min(v),max(v)+100000)
    pl.show()
    ans=input('Do you want to go back [Yes or No] ? ')
    if ans=='Yes':
        print(movievisual())
    else:
        movgrosgenr()
       
def movratlang():
    mov=pd.read_csv('D:\\OTT Platform Management\\MOVIES.csv')
    s=mov['LANGUAGE']
    v=mov['RATING']
    pl.bar(s,v,width=0.25,color='g')
    pl.title('RATINGS V/S LANGUAGE')
    pl.xlabel('Language')
    pl.ylabel('Ratings')
    pl.show()
    ans=input('Do you want to go back [Yes or No] ? ')
    if ans=='Yes':
        print(movievisual())
    else:
        movratlang()
    
def movgroscer():
    mov=pd.read_csv('D:\\OTT Platform Management\\MOVIES.csv')
    s=mov['CERTIFICATE']
    v=mov['GROSS']
    pl.bar(s,v,width=0.25,color='y')
    pl.title('GROSS V/S CERTIFICATE')
    pl.xlabel('Certificate')
    pl.ylabel('Gross')
    pl.ylim(min(v),max(v)+100000)
    pl.show()
    ans=input('Do you want to go back [Yes or No] ? ')
    if ans=='Yes':
        print(movievisual())
    else:
        movgroscer()

def movcourun():
    mov=pd.read_csv('D:\\OTT Platform Management\\MOVIES.csv')
    s=mov['COUNTRY']
    v=mov['RUNTIME']
    pl.bar(s,v,width=0.25,color='r')
    pl.title('RUNTIME V/S COUNTRY')
    pl.xlabel('Country')
    pl.ylabel('Runtime')
    pl.show()
    ans=input('Do you want to go back [Yes or No] ? ')
    if ans=='Yes':
        print(movievisual())
    else:
        movcourun()
    
def movduration():
    mov=pd.read_csv('D:\\OTT Platform Management\\MOVIES.csv')
    s=mov['DURATION']
    pl.hist(s,bins=10,color='c')
    pl.xlabel('Duration of movie')
    pl.title('DURATION')
    pl.show()
    ans=input('Do you want to go back [Yes or No] ? ')
    if ans=='Yes':
        print(movievisual())
    else:
        movduration()

#seriesvisualisation
def sergengro():
    ser=pd.read_csv('D:\\OTT Platform Management\\SERIES.csv')
    s=ser['Genre']
    v=ser['Gross']
    pl.bar(s,v,color='olive',width=0.25)
    pl.xlabel('Genre')
    pl.ylabel('Gross')
    pl.title('GROSS V/S GENRE')
    pl.ylim(min(v),max(v)+1000000)
    pl.show()
    ans=input('Do you want to go back [Yes or No] ? ')
    if ans=='Yes':
        print(seriesvisual())
    else:
        sergengro()
    
def serlangro():
    ser=pd.read_csv('D:\\OTT Platform Management\\SERIES.csv')
    s=ser['Language']
    v=ser['Gross']
    pl.bar(s,v,color='purple',width=0.25)
    pl.xlabel('Language')
    pl.ylabel('Gross')
    pl.title('LANGUAGE V/S GENRE')
    pl.ylim(min(v),max(v)+1000000)
    pl.show()
    ans=input('Do you want to go back [Yes or No] ? ')
    if ans=='Yes':
        print(seriesvisual())
    else:
        serlangro()

def serlanrun():
    ser=pd.read_csv('D:\\OTT Platform Management\\SERIES.csv')
    s=ser['Language']
    v=ser['Runtime']
    pl.bar(s,v,color='pink',width=0.25)
    pl.xlabel('Language')
    pl.ylabel('Runtime')
    pl.title('LANGUAGE V/S RUNTIME')
    pl.ylim(150,350)
    pl.show()
    ans=input('Do you want to go back [Yes or No] ? ')
    if ans=='Yes':
        print(seriesvisual())
    else:
        serlanrun()

def serratgen():
    ser=pd.read_csv('D:\\OTT Platform Management\\SERIES.csv')
    s=ser['Ratings']
    v=ser['Genre']
    pl.bar(v,s,color='pink',width=0.25)
    pl.xlabel('Ratings')
    pl.ylabel('Genre')
    pl.title('RATINGS V/S GENRE')
    pl.show()
    ans=input('Do you want to go back [Yes or No] ? ')
    if ans=='Yes':
        print(seriesvisual())
    else:
        serratgen()

#memberandplanvisualisation
def pmgraph():
    mb=pd.read_csv('D:\\OTT Platform Management\\MEMBERSHIP.csv')
    sil=[]
    gol=[]
    pla=[]
    for i in mb['MEMBERSHIP PLAN']:
        if i=='A':
            sil.append(i)
        if i=='B':
            gol.append(i)
        if i=='C':
            pla.append(i)
    df=pd.DataFrame({'GOLD':len(gol),'SILVER':len(sil),'PLATINUM':len(pla)},index=['   '])
    df.plot(kind='bar',color=['pink','magenta','purple'],width=0.25)
    pl.xlabel('Membership Plan')
    pl.ylabel('Frequency')
    pl.title('Representation of Most Bought Membership Plan')
    pl.show()
    ans=input('Do you want to go back [Yes or No] ? ')
    if ans=='Yes':
        print(mpvisual())
    else:
        pmgraph()

def mppay():
    trans=pd.read_csv('D:\\OTT Platform Management\\TRANSACTIONS.csv')
    card=[]
    net=[]
    for i in trans['METHOD OF PAYMENT']:
        if i=='CARD':
            card.append(i)
        if i=='NET BANKING':
            net.append(i)
    df=pd.DataFrame({'CARD':len(card),'NET BANKING':len(net)},index=[' '])
    df.plot(kind='bar',color=['olive','g'])
    pl.xlabel('Payment Method')
    pl.ylabel('Frequency')
    pl.title('Representation of Most Popular Payment Method')
    pl.show()
    ans=input('Do you want to go back [Yes or No] ? ')
    if ans=='Yes':
        print(mpvisual())
    else:
        pmgraph()

def salegraph():
    mb=pd.read_csv('D:\\OTT Platform Management\\MEMBERSHIP.csv')
    a=mb['MEMBERSHIP PLAN'].value_counts()
    a=a.sort_index(ascending=True)
    x=list(a.index)
    y=list(a.values)
    l=[]
    k=y[0]*199
    r=y[1]*699
    m=y[2]*1299
    l.extend([k,r,m])
    pl.bar(x,l,width=0.25,color='#C3B1E1')
    pl.xlabel('Membership Plan')
    pl.ylabel('Revenue')
    pl.title('Revenue Generated from Each Plan')
    pl.show()
    ans=input('Do you want to go back [Yes or No] ? ')
    if ans=='Yes':
        print(mpvisual())
    else:
        salegraph()
    

#menu   
def menu():
    print('------------------Welcome to YOLO------------------')
    print('1. Movies                          ')
    print('2. Series                          ')
    print('3. WorkForce                       ')
    print('4. Membership                      ')
    print('5. Transactions                    ') 
    print('6. Analytics Menu                  ')
    print('7. Visualisation Menu              ') 
    print('8. Exit                            ')
    ch=int(input('Enter your choice [1-8] : '))
    print()
    if ch==1:
        moviemenu()
    elif ch==2:
        seriesmenu()
    elif ch==3:
        workforcemenu()
    elif ch==4:
        membershipmenu()
    elif ch==5:
        transactionmenu()
    elif ch==6:
        analyticsmenu()
    elif ch==7:
        visualisationmenu()
    else:
        exit()

def moviemenu():
    print('--------------Movies Menu--------------')
    print('1. Display Movie Record                ')
    print('2. Add New Movie                       ')
    print('3. Update Movie Record                 ')
    print('4. Delete Movie Record                 ')
    print('5. Show Movie Details                  ')
    print('6. Exit                                ')
    ch=int(input('Enter your choice [1-6] : '))
    print()
    if ch==1:
        displaymovie()
    elif ch==2:
        addmovie()
    elif ch==3:
        updatemovie()
    elif ch==4:
        deletemovie()
    elif ch==5:
        searchmovie()
    else:
        ans=input('Do you want to return to main menu [Yes or No] ? ')
        if ans=='Yes':
            print()
            print(menu())
        else:
            moviemenu()
       
        
def seriesmenu():
    print('--------------Series Menu--------------')
    print('1. Display Series Record               ')
    print('2. Add New Series                      ')
    print('3. Update Series Record                ')
    print('4. Delete Series Record                ')
    print('5. Show Series Details                 ')
    print('6. Exit                                ')
    ch=int(input('Enter your choice [1-6] : '))
    print()
    if ch==1:
        displayseries()
    elif ch==2:
        addseries()
    elif ch==3:
        updateseries()
    elif ch==4:
        deleteseries()
    elif ch==5:
        searchseries()
    else:
        ans=input('Do you want to return to main menu [Yes or No] ? ')
        if ans=='Yes': 
            print()
            print(menu())
        else:
            seriesmenu()
       

def workforcemenu():
    print('--------------WorkForce Menu--------------')
    print('1. Display Workforce Record               ')
    print('2. Add New Employee                       ')
    print('3. Update Employee                        ')
    print('4. Delete Employee Record                 ')
    print('5. Show Employee Details                  ')
    print('6. Exit                                   ')
    ch=int(input('Enter your choice [1-6] : '))
    print()
    if ch==1:
        displayworkforce()
    elif ch==2:
        addemployee()
    elif ch==3:
        updateemployee()
    elif ch==4:
        deleteemployee()
    elif ch==5:
        searchemployee()
    else:
        ans=input('Do you want to return to main menu [Yes or No] ? ')
        if ans=='Yes': 
            print()
            print(menu())
        else:
            workforcemenu()

def membershipmenu():
    print('-------------Membership Menu--------------')
    print('1. Display Membership Records             ')
    print('2. Update Member Record                   ')
    print('3. Show Member Details                    ')
    print('4. Exit                                   ')
    ch=int(input('Enter your choice [1-4] : '))
    print()
    if ch==1:
        displaymember()
    elif ch==2:
        updatemember()
    elif ch==3:
        searchmember()
    else:
        ans=input('Do you want to return to main menu [Yes or No] ? ')
        if ans=='Yes': 
            print()
            print(menu())
        else:
            membershipmenu()
    
def transactionmenu():
    print('-----------Transaction Menu---------------')
    print('1. Apply for Membership                   ')
    print('2. Cancel Membership                      ')
    print('3. Exit                                   ')
    ch=int(input('Enter your choice [1-3] : '))
    if ch==1:
        applyms()
    elif ch==2:
        cancelms()
    else:
        ans=input('Do you want to return to main menu [Yes or No] ? ')
        if ans=='Yes': 
            print()
            print(menu())
        else:
            transactionmenu()

def analyticsmenu():
    print('-----------Analytics Menu-----------')
    print('1. Movie Analytics                  ')
    print('2. Series Analytics                 ')
    print('3. Member,Sales and Plan Analytics  ')
    print('4. Exit                             ')
    ch=int(input('Enter your choice [1-4] : '))
    print()
    if ch==1:
        movieanalytics()
    elif ch==2:
        seriesanalytics()
    elif ch==3:
        mpanalytics()
    else:
        ans=input('Do you want to return to main menu [Yes or No] ? ')
        if ans=='Yes': 
            print()
            print(menu())
        else:
            transactionmenu()


def visualisationmenu():
    print('---------Visualisation Menu---------')
    print('1. Movie Visualisation              ')
    print('2. Series Visualisation             ')
    print('3. Member and Plan Visualisation    ')
    print('4. Exit                             ')
    ch=int(input('Enter your choice [1-4] : '))
    print()
    if ch==1:
        movievisual()
    elif ch==2:
        seriesvisual()
    elif ch==3:
        mpvisual()
    else:
        ans=input('Do you want to return to main menu [Yes or No] ? ')
        if ans=='Yes': 
            print()
            print(menu())
        else:
            visualisationmenu()

def applyms():
    print('-------------------------------')
    print('1. New Member                  ')
    print('2. Existing Member             ')
    print('3. Exit                        ')
    ch=int(input('Enter your choice [1-3] : '))
    if ch==1:
        newms()
    elif ch==2:
        oldms()
    else:
        ans=input('Do you want to return to menu [Yes or No] ? ')
        if ans=='Yes': 
            print()
            print(transactionmenu())
        else:
            applyms()
    
def movieanalytics():
    print('-------------------------------')
    print('1. Maximum Runtime by Country  ')
    print('2. Minimum Runtime by Country  ')
    print('3. Maximum Gross by Genre      ')
    print('4. Minimum Gross by Genre      ')
    print('5. Maximum Ratings by Langauge ')
    print('6. Minimum Ratings by Language ')
    print('7. Maximum Ratings by Year     ')
    print('8. Minimum Ratings by Year     ')
    print('9. Exit                        ')     
    ch2=int(input('Enter your choice [1-9] : '))
    print()
    if ch2==1:
        maxrtcon()
    elif ch2==2:
        minrtcon()
    elif ch2==3:
        maxgrgen()
    elif ch2==4:
        mingrgen()
    elif ch2==5:
        maxrtlang()
    elif ch2==6:
        minrtlang()
    elif ch2==7:
        maxrtdt()
    elif ch2==8:
        minrtdt()
    else:
        ans=input('Do you want to return to menu [Yes or No] ? ')
        if ans=='Yes': 
            print()
            print(analyticsmenu())
        else:
            movieanalytics()

def seriesanalytics():
    print('-------------------------------')
    print('1. Maximum Runtime by Year     ')
    print('2. Minimum Runtime by Year     ')
    print('3. Maximum Gross by Genre      ')
    print('4. Minimum Gross by Genre      ')
    print('5. Maximum Ratings by Year     ')
    print('6. Minimum Ratings by Year     ')
    print('7. Maximum Seasons by Genre    ')
    print('8. Minimum Seasons by Genre    ')
    print('9. Exit                        ')     
    ch2=int(input('Enter your choice [1-9] : '))
    print()
    if ch2==1:
        maxsrty()
    elif ch2==2:
        minsrty()
    elif ch2==3:
        maxsgrgen()
    elif ch2==4:
        minsgrgen()
    elif ch2==5:
        maxrtingy()
    elif ch2==6:
        minrtingy()
    elif ch2==7:
        maxsgen()
    elif ch2==8:
        minsgen()
    else:
        ans=input('Do you want to return to menu [Yes or No] ? ')
        if ans=='Yes': 
            print()
            print(analyticsmenu())
        else:
            seriesanalytics()

def mpanalytics():
    print('--------------------------------------------')
    print('1. Most Popular Membership                  ')
    print('2. Least Popular Membership                 ')
    print('3. Exit                                     ')
    ch=int(input('Enter your choice [1-3] : '))
    if ch==1:
        maxpm()
    elif ch==2:
        minpm()
    else:
        ans=input('Do you want to return to menu [Yes or No] ? ')
        if ans=='Yes': 
            print()
            print(analyticsmenu())
        else:
            mpanalytics()


def movievisual():
    print('--------------------------------------------')
    print('1. Representation of Ratings by Year        ')
    print('2. Representation of Gross by Genre         ')
    print('3. Representation of Rating by Language     ')
    print('4. Representation of Gross by Certification ')
    print('5. Representation of Country by Runtime     ')
    print('6. Representation of Duration of Time       ')
    print('7. Exit                                     ')
    ch=int(input('Enter your choice : '))
    if ch==1:
        movratyear()
    elif ch==2:
        movgrosgenr()
    elif ch==3:
        movratlang()
    elif ch==4:
        movgroscer()
    elif ch==5:
        movcourun()
    elif ch==6:
        movduration()
    else:
        ans=input('Do you want to return to menu [Yes or No] ? ')
        if ans=='Yes': 
            print()
            print(visualisationmenu())
        else:
            movievisual()

def seriesvisual():
    print('----------------------------------------')
    print('1. Representation of Genre by Gross        ')
    print('2. Representation of Language by Gross     ')
    print('3. Representation of Language by Runtime   ')
    print('4. Representation of Ratings by Genre      ')
    print('5. Exit                                    ')  
    ch=int(input('Enter your choice : '))
    if ch==1:
        sergengro()
    elif ch==2:
        serlangro()
    elif ch==3:
        serlanrun()
    elif ch==4:
        serratgen()
    else:
        ans=input('Do you want to return to menu [Yes or No] ? ')
        if ans=='Yes': 
            print()
            print(visualisationmenu())
        else:
            seriesvisual()

def mpvisual():
    print('----------------------------------------------------')
    print('1. Representation of Membership Type Frequency      ')
    print('2. Represenatation of Revenue of Each Plan          ')
    print('3. Representation of Payment Method Frequency       ')
    print('4. Exit                                     ')
    ch=int(input('Enter your choice [1-4] : '))
    if ch==1:
        pmgraph()
    elif ch==2:
        salegraph()
    elif ch==3:
        mppay()
    else:
        ans=input('Do you want to return to menu [Yes or No] ? ')
        if ans=='Yes': 
            print()
            print(visualisationmenu())
        else:
            mpvisual()

print(menu())

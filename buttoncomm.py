
#%% THE BUTTON GENERATOR

import mysql.connector as sql
pd=sql.connect(host = 'localhost', user ='root', password = 'lelouchiszero')
if pd.is_connected:
    print("__CONNECTED__")
c1=pd.cursor()
c1.execute("use periodic;")
def sblock():  
    '''generates buttons for the sblock'''
    c1.execute("select Atomic_no, Element from modern_pt where block = 's-block';")
    l=[]
    for i in c1:
        l+=i
    
    ename=''
    bname=None
    c=1
    v=0
    row=1
    column=0
    bsyntax=[]
    while c<12:
        bname=l[v]
        ename=l[v+1]
        bsyntax.append("""%s=tk.Button(base, height = "5" , width = "10" , text = %s , command = lambda:info(%s),fg="white",bg="black").grid(row=%d, column=%d)"""%(bname,ename,bname,row,column))
        c+=1
        v+=2
        column+=1
        if column%2==0:
            row+=1
            column=0
    return bsyntax    
            
def dblock(): 
    ''' generates buttons for the dblock'''
    c1.execute("select Atomic_no, Element from modern_pt where Block = 'd-block';")
    l=[]
    for i in c1:
        l+=i
    
    ename=''
    bname=None
    c=1
    v=0
    row=3
    column=2
    bsyntax=[]
    while c<22:
        bname=l[v]
        ename=l[v+1]
        bsyntax.append('%s=tk.Button(base, height = "5" , width = "10" , text = %s , command = lambda:info(%s),fg="white",bg="black").grid(row=%d , column=%d)'%(bname,ename,bname,row,column))
        c+=1
        v+=2
        column+=1
        if ename in ["Zinc","Cadium","Mercury","Copernicium"]:
            row+=1
            column=2

    return bsyntax
    
def pblock():       
    ''' generates buttons for the pblock'''
    c1.execute("select Atomic_no, Element from modern_pt where Block = 'p-block';")
    l=[]
    for i in c1:
        l+=i
    
    ename=''
    bname=None
    c=1
    v=0
    row=1
    column=12
    bsyntax=[]
    while c<25:
        bname=l[v]
        ename=l[v+1]
        bsyntax.append('%s=tk.Button(base, height = "5" , width = "10" , text = %s , command = lambda:info(%s),fg="white",bg="black").grid(row=%d , column=%d)'%(bname,ename,bname,row,column))
        c+=1
        v+=2     
        column+=1
        if column==17:
            row+=1
            column=12
    return bsyntax
            
def fblock():
    '''generates buttons for the fblock'''
    c1.execute("select Atomic_no, Element from modern_pt where Block = 'f-block';")
    l=[]
    for i in c1:
        l+=i
    
    ename=''
    bname=None
    c=1
    v=0
    row=8
    column=2
    bsyntax=[]
    while c<3:
        bname=l[v]
        ename=l[v+1]
        bsyntax.append('%s=tk.Button(base, height = "5" , width = "10" , text = %s , command = lambda:info(%s),fg="white",bg="black").grid(row=%d, column=%d)'%(bname,ename,bname,row,column))
        c+=1
        v+=2 
        column+=1
        if column==16:
            row=2
            column=2
    return bsyntax




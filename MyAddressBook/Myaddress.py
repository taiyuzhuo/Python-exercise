import pickle as p
import sys
import os

filename = 'AddressBook.data'

class Myaddress:
    '''The number of addresses'''
    def __init__(self,name,email,phone):
        self.name = name
        self.email = email
        self.phone = phone

def addinfo():
    s = input('Input the information like tyz;tyz@126.com;17600101820-->')
    s1 = s.split(';')
    pp = Myaddress(s1[0],s1[1],s1[2])
    f=open(filename,'rb')
    tmp = p.load(f)
    tmp[pp.name] = pp.email+';'+pp.phone
    f.close()
    f = open(filename,'wb')
    p.dump(tmp,f)
    f.close()
    del tmp
def delete():
    f = open(filename,'rb')
    tmp = p.load(f)
    count = 0
    for name,info in tmp.items():
        count +=1
        s1 = info.split(';')
        print('The name[{}] are {}. Email: {}; Phone: {}'.format(count,name,s1[0],s1[1]))
    s = input('Input the information you want to delete-->')
    del tmp[s]
    f.close()
    f = open(filename,'wb')
    p.dump(tmp,f)
    f.close()
    del tmp
def Myfind():
    f = open(filename,'rb')
    tmp = p.load(f)
    count = 0
    for name,info in tmp.items():
        count +=1
        print('The name[{}] are {}'.format(count,name))
    s = input('Input the information of who you want to know-->')
    if s in tmp:
        s1 = tmp[s]
        s2 = s1.split(';')
        print('The email address of {} is {}'.format(s,s2[0]))
        print('The phone number of {} is {}'.format(s,s2[1]))
    else:
        print('The name you just input is not in my address book.')
    del tmp
def main():
    while True:
        u = input('This is my address book.\n1.search;\n2.Add;\n3.delete;\n4.quit\n-->')
        if u=='1':
            Myfind()
        elif u=='2':
            addinfo()
        elif u=='3':
            delete()
        elif u=='4':
            sys.exit()
        else:
            print('retry')


if os.path.exists(filename):
    main()
else:
    f=open(filename,'wb')
    tmp={'jack':'jack@ict.ac.cn,13645654345'}
    p.dump(tmp,f)
    f.close()
    del tmp
    main()

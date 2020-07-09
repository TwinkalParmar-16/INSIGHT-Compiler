f=open("input.text",'r')
read_data=f.readlines()
for i in range(len(read_data)):
    read_data[i]=read_data[i].strip()
   
    
if '' in read_data:
    while '' in read_data:
        read_data.remove('')
read_data_copy=read_data
print(read_data_copy)
list1=["~$",'$~','AND',"OR","NOT",'~','<','>','<=','>=','==','IF','CURL','S@','E@',"G@",':','(',')','[',']','REST_ALL','=',"+","-",'*','/','^','NOT=']
'''
i=0
k=0
t1=t2=t3=t4=t5=t6=t7=t8=t9=t10=t11=t12=t13=t14=t15=t16=t17=t18=t19=t20=t21=t22=t23=t24=t25=t26=t27=0
for i in range(len(read_data)):
    str1=read_data[i]
    for k in range(len(str1)):
        if '~$' in str1:
            print('~$      :      opening symbol of programme ')
            read_data[i].replace("~$",'')
            print(read_data[i])
        if '$~' in str1:
            print('$~      :       closing symbol of programme ')
        if '~' in str1:
            if(t1==0):
               print('~    :      closing statement ')
               t1=t1+1
        if '(' in str1:
            if(t2==0):
               print('(    :      opening bracket ')
               t2=t2+1
        if ')' in str1:
            if(t3==0):
               print(')    :      closing bracket ')
               t3=t3+1
        if ':' in str1:
            if(t4==0):
               print(':    :      colon ')
               t4=t4+1
        if '[' in str1:
            if(t5==0):
               print('[    :      opening bracket ')
               t5=t5+1
        if ']' in str1:
            if(t6==0):
               print(']    :      closing statement ')
               t6=t6+1
        if 'NOT' in str1:
            if(t7==0):
               print('NOT  :      logic operator ')
               t7=t7+1
        if 'AND' in str1:
            if(t8==0):
               print('AND    :      logic operator ')
               t8=t8+1
        if 'OR' in str1:
            if(t9==0):
               print('OR    :      logic operator ')
               t9=t9+1
        if '==' in str1:
            if(t10==0):
               print('==    :      logic operator ')
               t10=t10+1
        if '<' in str1:
            if(t11==0):
               print('>    :      logic operator ')
               t11=t11+1
        if '>' in str1:
            if(t12==0):
               print('>    :      logic operator ')
               t12=t12+1
        if 'NOT=' in str1:
            if(t13==0):
               print('NOT=    :      logic operator ')
               t13=t13+1
        if '>=' in str1:
            if(t14==0):
               print('>=    :      logic operator ')
               t14=t14+1
        if '<=' in str1:
            if(t15==0):
               print('<=    :      logic operator ')
               t15=t15+1
        if '+' in str1:
            if(t16==0):
               print('+    :      arithmetic operator ')
               t16=t16+1
        if '-' in str1:
            if(t17==0):
               print('-    :      arithmetic operator ')
               t17=t17+1
        if '*' in str1:
            if(t18==0):
               print('*    :      arithmetic operator ')
               t18=t18+1
        if '/' in str1:
            if(t19==0):
               print('/    :      arithmetic operator ')
               t19=t19+1
        if '^' in str1:
            if(t20==0):
               print('^    :      arithmetic operator ')
               t20=t20+1
        if 'CURL' in str1:
            if(t21==0):
               print('CURL    :      loop keyword ')
               t21=t21+1
        if 'IF' in str1:
            if(t22==0):
               print('IF    :      IF keyword ')
               t22=t22+1
        if 'REST_ALL' in str1:
            if(t23==0):
               print('REST_ALL    :      ELSE keyword ')
               t23=t23+1
        if 'S@' in str1:
            if(t24==0):
               print('S@    :       keyword ')
               t24=t24+1
        if 'E@' in str1:
            if(t25==0):
               print('E@    :       keyword ')
               t25=t25+1
        if 'G@' in str1:
            if(t26==0):
               print('G@    :       keyword ')
               t26=t26+1
        if '='  in str1:
            if(t27==0):
                print('=    :    assignment operator')
                t27=t27+1
print(read_data1)
   '''
my_list=['~','$','[',']','(',')',':','=','>','<','+','-','/','*','^']
i=0
k=0
for i in range(len(read_data)):
    str=read_data[i]
    for k in range(len(str)):
        if str[k] in my_list:
            str=str.replace(str[k],' ')
    read_data[i]=str

i=0
k=0
for i in range(len(read_data)):
    str=read_data[i]
    if "G@" in str:
        str=str.replace("G@",' ')
    if "E@" in str:
        str=str.replace("E@",' ')
    if "S@" in str:
        str=str.replace("S@",' ')
    if "REST_ALL" in str:
        str=str.replace("REST_ALL",' ')
    if "IF" in str:
        str=str.replace("IF",' ')
    if "CURL" in str:
        str=str.replace("CURL",' ')
    if "AND" in str:
        str=str.replace("AND",' ')
    if "OR" in str:
        str=str.replace("OR",' ')
    if "NOT" in str:
        str=str.replace("NOT",' ')
    read_data[i]=str

print("final",read_data)

i=0
k=0
IsDigit=0
for i in range(len(read_data)):
    str=read_data[i]
    temp_list=str.split()
    #print(temp_list)
    for k in range(len(temp_list)):
        if temp_list[k].isdigit():
            IsDigit=1
            print(temp_list[k],":CONSTANT")
        if temp_list[k].isalnum() and IsDigit!=1:
            print(temp_list[k],':VARIABLE')
    



        

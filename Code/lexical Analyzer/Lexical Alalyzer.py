f=open("input.text",'r')
read_data=f.readlines()

print(read_data)
for i in range(len(read_data)):
    read_data[i]=read_data[i].strip()
   
    
if '' in read_data:
    while '' in read_data:
        read_data.remove('')
read_data_copy=read_data
print(read_data_copy)
x=[]
k=0
z=[]
a=0
temp_list=[]

index=read_data.index('~$')
#print(index);
new_func=read_data[:6]

#print(new_func)
t=0

str=new_func[1]
INDEX=str.index('(')
#print(INDEX)
fun=str[:INDEX]
#print(fun)
print(fun,"  :  FUNCTION NAME")
x.append(fun)


for i in range(len(read_data)):
  str=read_data[i]
  for k in range (len(str)):
    if '~$' in str:
        if '~$' not in x:
          print('~$      : Opening symbol of programme')
          x.append('~$')
    if '$~' in str:
        if '$~' not in x:
            print('$~      : Closing symbol of programme')
            x.append('$~')
    if '~' in str:
        if '~' not in x:
            print('~      : Closing statement')
            x.append('~')        
    if (ord(str[k])==43 or ord(str[k])==45 or ord(str[k])==42 or ord(str[k])==47 or ord(str[k])==94):
        if str[k] not in x:
            print(str[k],'       : Airthmatic Operator')
            x.append(str[k])
    if(ord(str[k])==91 or ord(str[k])==40):
        if str[k] not in x:
            print(str[k],'       :Opening brackets')
            x.append(str[k])
    if(ord(str[k])==41 or ord(str[k])==93):
        if str[k] not in x:
            print(str[k],'       : Closing brackets')
            x.append(str[k])
    if(ord(str[k])==60 or ord(str[k])==62):
        if str[k] not in x:
            print(str[k],'       : Logical Operator')
            x.append(str[k])
    if(ord(str[k])==61 ):
        if str[k] not in x:
            print(str[k],'      : Assignment Operator')
            x.append(str[k])
    if 'NOT' in str :
        if 'NOT' not in x :
            print('NOT     : Logical Operator')
            x.append('NOT')
    if 'AND' in str :
        if 'AND' not in x :
            print('AND     : Logical Operator')
            x.append('AND')
    if 'OR' in str :
        if 'OR' not in x :
            print('OR      : Logical Operator')
            x.append('OR')
    if 'IF' in str :
        if 'IF' not in x :
            print('IF      : IF keyword')
            x.append('IF')        
    if 'CURL' in str :
        if 'CURL' not in x :
            print('CURL    : LOOP keyword')
            x.append('CURL')
    if 'CURL_C' in str :
        if 'CURL_C' not in x :
            print('CURL_C    : Condition LOOP keyword')
            x.append('CURL_C')
    if 'REST_ALL' in str :
        if 'REST_ALL' not in x :
            print('REST-ALL: ELSE  keyword')
            x.append('REST_ALL')
    if 'EXIT_fun_c' in str :
        if 'EXIT_fun_c' not in x :
            print('EXIT_fun_c    : Exit for function(keyword)')
            x.append('EXIT_fun_c')
    if 'R_N' in str :
        if 'R_N' not in x :
            print('R_N    : Return keyword for function')
            x.append('R_N')
    if '==' in str :
        if '==' not in x :
            print('==      : Comparision Operator')
            x.append('==')        
    if '<=' in str :
        if '<=' not in x :
            print('<=      : Comparision Operator')
            x.append('<=')          
    if '>=' in str :
        if '>=' not in x :
            print('>=      : Comparision Operator')
            x.append('>=')
    if 'NOT=' in str :
        if 'NOT=' not in x :
            print('NOT=    : Comparision Operator')
            x.append('NOT=')
    if 'S@' in str :
        if 'S@' not in x :
            print('S@      : Keyword')
            x.append('S@')
    if 'E@' in str :
        if 'E@' not in x :
            print('E@      : Keyword')
            x.append('E@')
    if 'G@' in str :
        if 'G@' not in x :
            print('G@      : Keyword')
            x.append('G@')         
    if ':' in str:
        if ':' not in x:
            print(':       : Colon')
            x.append(':')
    if fun in str:
        
        '''
    if (ord (str[k])>=97 and ord (str[k])<123):
            if str[k] not in x:
                print(str[k],'   : variable')
                x.append(str[k])
for j in range (len(read_data)):
    a=read_data[i]
    print(a)
    if a[j] not in x: 
        z.append(a[j])'''
        
         
#print('hhhhhh',z)
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
    if fun in str:
       str=str.replace(fun,' ')
       qw=str.index(',')
       #print(qw)
       lstr=str[:qw]
       rstr=str[qw+1:]
       #print(lstr,"hh",rstr)
       temp_list.append(lstr)
       temp_list.append(rstr)
    read_data[i]=str
#print(temp_list)
k=0
me=0
#print(len(temp_list))
for i in range(len(temp_list)):
    temp_list[i]=temp_list[i].strip()
if '' in read_data:
    while '' in temp_list:
        read_data.remove('')
#print(temp_list)
for me in range(len(temp_list)):
  if temp_list[me].isdigit():
      if temp_list[me] not in x:
        print(temp_list[me],": CONSTANT")
        x.append(temp_list[me])
  elif temp_list[me].isalnum():
        if temp_list[me] not in x:
            print(temp_list[me],": VARIABLE")
            x.append(temp_list[me])
            
temp_list=[]
i=0
k=0
IsDigit=0


for i in range(len(read_data)):
    str=read_data[i]
    temp_list=str.split()
    #print(temp_list)
    for k in range(len(temp_list)):
        if temp_list[k].isdigit():
            if temp_list[k] not in x:
                print(temp_list[k],"     : CONSTANT")
                x.append(temp_list[k])
            
        elif temp_list[k].isalnum():
            if temp_list[k] not in x:
              print(temp_list[k],'        : VARIABLE')
              x.append(temp_list[k])
        
    



        

        

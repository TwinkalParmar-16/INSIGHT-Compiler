f=open("input.text",'r')
read_data=f.readlines()

for i in range(len(read_data)):
    read_data[i]=read_data[i].strip()
   
x=0
p=0
q=0
abc=0
r=[]
correct=0
if '' in read_data:
    while '' in read_data:
        read_data.remove('')
read_data_copy=read_data
index=read_data.index("~$")
func_list=read_data[:index]
print(func_list)
str=func_list[1]
in1=str.index('(')
fun=str[:in1]
print(fun)


#print(read_data[0])
temp_list=[]
if read_data[0]!="~$" or read_data[-1]!='$~':
    print("Error: opening or closing statement")
    correct+=1
'''read_data.remove(read_data[0])
read_data.remove(read_data[-1])'''
    #to extract if stamnets from file
'''for i in range (len(read_data)):
    if "[" in read_data[i]:
        print(read_data[i],"--")'''
y=read_data.count('[')
x=read_data.count(']')+read_data.count(']~')
#print(x,y)
if(y != x):
    print('Error:expected declaration input at the end of output')
    correct+=1
for i in range (len(read_data)):
    str=read_data[i]
    if '~$' in str:
        i2=i
for i in range (len(read_data)):
    
    str=read_data[i]
    if(str[-1]!='~'):
        if 'IF' not  in read_data[i] and 'CURL' not in read_data[i] and 'REST_ALL' not in read_data[i] and '[' not in read_data[i] and 'CURL_C' not in read_data[i] and '~$' not in read_data[i] and '$~' not in read_data[i] and fun not in read_data[i]:
            print('Error:~ missing at the end of line-->',read_data[i])
            correct+=1
    if(str[-1]=='~'):
        if 'IF' in read_data[i] or 'CURL' in read_data[i] or 'REST_ALL' in read_data[i] or '[' in read_data[i] or 'CURL_C' in read_data[i] or fun in read_data[i]:
            print('Error:~ at the end of line-->',read_data[i])
            correct+=1
    #fun_checking
    if fun in str:
                i1=i
                if(i1>i2):
                    if str[-1]!='~':
                      print('~ missing in line -->',str)
                      correct+=1
                if(i1>i2):
                    if str[-2]!=')':
                        print('error in line -->',str)
                if(i1<i2):
                    if str[-1]!=')':
                       print('error in line -->',str) 
    if("]" in str):
        k=i
        while(read_data[k]!='[' and k>=0):
              temp_list.append(read_data[k])
              k-=1
        temp_list.append(read_data[k])     
        read_data[k]=read_data[k]+' '# to fetch the correct bracktets
        temp_list.reverse()
        #print(temp_list)
        t=0
        for t in range(len(temp_list)):
            str=temp_list[t]
            #if checking
            if "IF" in str:
                if str[2]!="(" or str[-1]!=')':
                    print("Error:in line",str)
                    correct+=1
            #loop checking
            if "CURL(" in str:
              if "S@" in str and ":E@" in str and "E@" in str and ":G@" in str and "G@" in str:#to remove the problem of 'substring not found'
                  if str not in r:
                        s_c=str.count('S@')
                        e_c=str.count(':E@')
                        g_c=str.count(':G@')
                        if(s_c!=1 or e_c!=1 or g_c!=1):
                          p=1
                          r.append(str)
                        S=str.index("S@")
                        G=str.index("G@")
                        E=str.index("E@")
                        if(S>E or E>G ):
                            print('Error:Invalid notation-->',str)
                            correct+=1
                            r.append(str)
                            p=0
                        if(p==1):
                            print('Error:in line',str)
                            correct+=1
              else:
                 print("Error:in line",str)
                 correct+=1
                 r.append(str)
                  
            #loop wirh condition checking
            if "CURL_C(" in str:
             if "S@" in str and ":E@" in str and "E@" in str:
               if str not in r:
                    S_C=str.count("S@")
                    E_C=str.count(":E@")
                    if(S_C!=1 or E_C!=1):
                     q=1
                     r.append(str)
                    s=str.index("S@")
                    e=str.index("E@")
                    if(s>e):
                            print("Error:Invalid notion-->",str)
                            correct+=1
                            q=0
                            r.append(str)
                    if 'G@' in str or 'g@' in str: 
                        print("Error:Invalid notion-->",str)
                        correct+=1
                        q=0
                        r.append(str)
                    if(q==1):
                        print('Error:in line',str)
                        correct+=1                
             else:
                if str not in r: 
                 print("Error:in line",str)
                 correct+=1
                 r.append(str)
                 
            
            # to check after this"["
            if temp_list[t]=='[':
                str_check=temp_list[t+1]
                if "IF(" not in str_check and "CURL(" not in str_check and "CURL_C(" not in str_check and fun not in str_check:
                    print("Error:Invalid statement after",str)
                    correct+=1
                    #correctly working
            
            if temp_list[t]=="REST_ALL":
                check=0
                if abc!=1:
                    for v in range(0,t):
                      str=temp_list[v]
                      if "IF" in str:
                          check=1
                    if check==0:
                      print("Error:REST_ALL can not be used without IF")
                      correct+=1
                    abc=1
        temp_list=[]
if(correct==0):
    print('Code is correct')
        
            
    
       

        
        
       
        
    
            
    
    

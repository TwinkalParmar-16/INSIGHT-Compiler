f=open("input.text",'r')
read_data=f.readlines()
#print(read_data)
for i in range(len(read_data)):
    read_data[i]=read_data[i].strip()
if '' in read_data:
    while '' in read_data:
        read_data.remove('')
#print(read_data)

length=len(read_data)
#print(length)

def is_float(string):
  try:
    return float(string) and '.' in string
  except ValueError:
    return False
for i in range(length):
  str1=read_data[i]
  list_l=[]
  list_r=[]
  if '=' in str1:
    #print(i,"= available")
    length2=len(str1)
    #print(length,"length str1")
    index=str1.index('=')
    #print(i,"index =")
    for k in range(index-1,-1,-1):
      #print("index",k,"--word",str1[k])
      list_l.append(str1[k])
    #print(list_l,"list_l")

    for j in range(index+1,length2):
      #print("index",j,"--word",str1[j])
      if str1[j]=="~":
           break
      list_r.append(str1[j])
    #"""print(list_r,"list_r")"""

    new_list_l=list_l[::-1]
    #print(new_list_l)
    #print(str1[index])
    #print(list_r)

    l_value=''.join(new_list_l)
    r_value=''.join(list_r)
    #print(l_value)
    #print(r_value)

    if r_value.isdigit():
      print(l_value,str1[index],r_value,'------','INT')
    elif is_float(r_value):
      print(l_value,str1[index],r_value,'------','FLOAT')
    elif r_value[0]=='"' and r_value[-1]=='"':
       print(l_value,str1[index],r_value,'------','STRING')
    elif r_value[0]=="'" and r_value[-1]=="'":
       print(l_value,str1[index],r_value,'------','STRING')
    else:
      print("UNRECOGNIZED CONSTANT FOR INSIGHT")
       

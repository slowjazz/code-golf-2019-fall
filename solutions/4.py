s=input().replace(' ','')
r,z="",""
for i in s:
    if i.isupper():
        r+='1'
    else: r+='0'
for i in range(0,len(r),5):
    z+=chr(int(r[i:i+5],2)+65)
print(z)
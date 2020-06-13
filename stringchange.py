str1=list(input())
str2=list(input())
str3=list(input())
for i in range(len(str1)):
    if(str1[i]=='i' or str1[i]=='o' or str1[i]=='a' or str1[i]=='u' or str1[i]=='e' or str1[i]=='I' or str1[i]=='O' or str1[i]=='A' or str1[i]=='U' or str1[i]=='E'):
        str1[i]='$'
for i in range(len(str2)):
    if(str2[i]!='i' and str2[i]!='o' and str2[i]!='a' and str2[i]!='u' and str2[i]!='e' and str2[i]!='I' and str2[i]!='O' and str2[i]!='A' and str2[i]!='U' and str2[i]!='E'):
        str2[i]='#'
for i in range(len(str3)):
    str3[i]=str3[i].upper()
print(''.join(str1))
print(''.join(str2))
print(''.join(str3))
    
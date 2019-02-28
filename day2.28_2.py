i=1
str=[]
while i<=43:
    a = input("请投票：")
    if a=="exit":
        break
    str.append(a)
print(str)
dict={}
for i in str:
    key=dict.get(i)
    if key==None:
        dict[i]=1
    else:
        dict[i]+=1
print(dict)
print("最大值的是：",max(dict,key=dict.get))
print("最大值的票数：",dict[max(dict,key=dict.get)])
dict=sorted(dict.items(),key=lambda item:item[1],reverse=True)
print(dict)








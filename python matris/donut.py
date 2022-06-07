import funcyy
resultlisty=[]
matris=input("").strip().split()
newlist= matris[:matris.index("=")]
secondlist=matris[matris.index("=")+1:]

leftside_sum_of_y=0
leftside_sum_of_x=0
rigtsize_sum_of_x=0
rigtsize_sum_of_y=0



const_left=0
const_right=0

for i in range(len(newlist)):
    
    if matris[i][-1]=="y":
        leftside_sum_of_y=leftside_sum_of_y+int(matris[i][:-1])
    elif matris[i][-1]=="x":
        leftside_sum_of_x=leftside_sum_of_x+int(matris[i][:-1])
    else:
        const_left=const_left+ int(matris[i])
    
    


for i in range(len(secondlist)):
    if secondlist[i][-1]=="x":
        rigtsize_sum_of_x=rigtsize_sum_of_x+int(secondlist[i][:-1])
    elif secondlist[i][-1]=="y":
        rigtsize_sum_of_y=rigtsize_sum_of_y+int(secondlist[i][:-1])
    else:
        const_right=const_right+ int(secondlist[i]) 



    

 
lsize=leftside_sum_of_y-rigtsize_sum_of_y
rgtsize=rigtsize_sum_of_x-leftside_sum_of_x
print(f"y = {lsize/rgtsize}x {const_right-const_left}")

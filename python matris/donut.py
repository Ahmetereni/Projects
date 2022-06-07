import funcyy as ff
resultlisty=[]
matris=input("").strip().split()
firstlist= matris[:matris.index("=")]
secondlist=matris[matris.index("=")+1:]

lside_y,lside_x,lside_const=ff.funky(firstlist)
rside_y,rside_x,rside_const=ff.funky(secondlist)

print(lside_y,lside_x,lside_const)
import time
start=time.time()
maze=[
    ["#","#","#","#","#","O","#","#","#","#",],
    ["#","O","#","#","#","#","#","#","#",],
    ["#","#","#","#","#","#","#","#","O",],
    ["#","#","#","#","#","#","#","#","O",],
    ["#","#","#","#","#","#","#","#","O",],
    ["#","#","#","#","#","#","#","#","O",],
    ["#","#","#","#","#","#","#","#","O",],
    ["#","#","#","#","#","#","#","#","O",],

] 
finishstr=""
for listindex in maze:
    if len(finishstr)>= len(listindex):
        finishstr=finishstr+"\n"

    for char in listindex:

        for i in range(len(char)):
            
            
                
            if char =="#":
                finishstr+="c"
            if char =="O":
                finishstr+="Z"
            

                
end=time.time()
print(finishstr)


        
        
            
    

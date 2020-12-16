import arm_memory as setting
import arm_instruction as machine
setting.init()


''''
pT_rows = {0:0, 4:1,8:0,12:-1}

def main():
    r[1] = 1
    r[3] = 16    
    while True:
        if r1 == 7:
            break
        #mypasTRI(r1,r3)
        r1 = r1 +1

def mypasTRI(r1, r3):
     
	res = 1
	if (k > n - k) : 
		k = n - k 
	for i in range(0 , k) : 
		res = res * (n - i) 
		res = res // (i + 1) 
	
	return res 

# Driver program 
n = 7
printPascal(n) 


# This code is contributed by Nikita Tiwari. 
'''



machine.create('pT_rows',[0,1,0,-1])
machine.create()
setting.r['r0'] = setting.symbol['Name']
machine.LDR('r1',['r0',0])
setting.r['r1'] += 3
machine.STR('r1',['r0',8])
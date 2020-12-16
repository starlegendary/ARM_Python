import arm_memory as setting

def show():
    import pandas as pd
    print("Register: ")
    print(pd.DataFrame.from_dict(setting.r, 
                        orient='index',).T)
    print()
    print("Memory: ")
    print(pd.DataFrame.from_dict(setting.memory, 
                        orient='index',
                       columns=['Value']))
    print()
    print("Symbol: ")       
    print(pd.DataFrame.from_dict(setting.symbol, 
                        orient='index',
                       columns=['Address']))
    print()
    print('+'*20)
    print()
def create(name,value):
  if type(value) == list:
      while True:
          addr = rdaddress()
          for i in range(len(value)):
              if addr+i*4 in setting.memory:
                  break
              setting.memory[addr+i*4] = value[i]
              if i == len(value) - 1: 
                  setting.symbol[name] = addr
                  print("Create ",name,"=",value,"at",addr) 
                  print()
                  show()
                  return        
  addr = rdaddress()
  setting.memory[addr] = value
  setting.symbol[name] = addr
  print("Create ",name,"=",value,"at",addr) 
  print()
  show()

def LDR(a,b):
    if type(b) == list:
        if type(b[1]) == int:
            setting.r[a] = setting.memory[setting.r[b[0]]+b[1]]
        else:
            setting.r[a] = setting.memory[setting.r[b[0]]+setting.r[b[1]]]
        print("Load Value of",a,"to address",b[0],"+",b[1])
    else:
        setting.r[a] = setting.symbol[b]
    show()

def STR(a,b):
    if type(a) == str:
        sth = setting.r[a]
    else:
        sth = a
    if type(b[1]) == int:
        setting.memory[setting.r[b[0]]+b[1]] = sth
    else:
        setting.memory[setting.r[b[0]]+setting.r[b[1]]] = sth
    print("Store Value of",a,"to address",b[0],"+",b[1])
    show()



def address(val):
    for key, value in setting.memory.items():
         if val == value:
             return key
def rdaddress():
    import random 
    return random.choice([x*4 for x in range(0,setting.n_address) if x*4 not in setting.memory])
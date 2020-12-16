def init():
    global r,memory,symbol
    n_address = 1000
    n_bit = 16

    r = {'r'+str(i):0 for i in range(n_bit)}
    r['r13'] = n_address*4

    memory = {}
    symbol = {}
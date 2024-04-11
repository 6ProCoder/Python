import time
x = []
y = 0
print 'ama thes gramata graje (gramata) an thes noumera tote (noumera) kai ama thes na stamatisi tote (stop)'
while y!='stop':


    y = raw_input(x)
    if y == 'gramata':
        while y!='noumera':
            y = raw_input(x)
            if y!='noumera':
                x.append (y)
    else:
        if y!='stop':
            x.append (int (y))
print '>>>',x,'<<<'
time.sleep(10)

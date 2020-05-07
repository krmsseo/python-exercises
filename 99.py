for z in range(0,3):
    for y in range(1,10):
        for x in range(1,4):
            print( 3*z+x,'*', y, '=',str((3*z+x)*y).rjust(3), end='    ')
        print()
    print()
        

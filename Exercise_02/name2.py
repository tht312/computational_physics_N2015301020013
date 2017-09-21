import time
n=0
while n < 20:
    if n < 19: 
        print('\n' * n)
        print(" " * n, end=' '),print("##### #####  #   #    ####    #   #     #      ###   #####  #    #     #   #")
        print(" " * n, end=' '),print("  #   #      ##  #  #         #   #    # #    #   #    #    #   # #    ##  #")
        print(" " * n, end=' '),print("  #   #####  # # #  #  ####   #####   #####   #   #    #    #  #####   # # #")
        print(" " * n, end=' '),print("  #   #      #  ##  #    ##   #   #  #     #  #   #    #    # #     #  #  ##")
        print(" " * n, end=' '),print("  #   #####  #   #   #### #   #   #  #     #   ###     #    # #     #  #   #")
        n=n+1
        time.sleep(1) 
        print("\x1b[2J")
    else:
        n = 0

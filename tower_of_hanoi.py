def tower_of_hanoi(n, source, target, auxillary): # lets say, n is number of desk, soucre is the place of desk, target is place where u will put the desk, auxillary is middle rod
    if n > 0:                                      # actually there are three rod, first one is source, middle is auxillary, last is target
                                              # n is greater than zero means that the function needs to moves or is operate recursive function. the function will keeping on operating untill the n become zero 
        tower_of_hanoi(n-1, source, auxillary,target)

        print("move disk", n-1, "from rod", source, "to rod", target )

        tower_of_hanoi(n-1, auxillary, target, source)

x = 3
tower_of_hanoi(x,1, 2, 3)


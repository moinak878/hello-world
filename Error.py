while True:
        try:
                value=int(input("Enter a number between 1 and 10 : "))
        except :# ValueError:
                print ' You must enter a value between 1 and 10'
                print'===========RESTART==============='
        else:
                if(value>0) and (value<=10) :
                        print 'You entered %d'%value
                        exit()
                else:
                        print 'Wrong Input'
                        print'===========RESTART==============='


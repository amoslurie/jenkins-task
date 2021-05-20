import sys
#n = len(sys.argv)
#print("Total arguments passed:", n)
# Check number o arguments
if len(sys.argv) != 3:
     raise ValueError('Usage: python3 script <arg> ')
else:
    if int(sys.argv[2])%3 ==0:
    #    print(f'Script Name is {sys.argv[0]}')
        print ('run number modulo is', int(sys.argv[2])%3)
        print(f'The name of the Jenkins job  is  {sys.argv[1]}')

    else:
        raise ValueError('Failed due to sequence number ')

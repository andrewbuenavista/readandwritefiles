def main():

    infile = open("clients.txt",'r')

    count = 1
    
    for line in infile:

        print(count, '. ', line.rstrip('\n'), sep = '')

        count += 1

    infile.close()
    
main()



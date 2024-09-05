#This program writes three line of data to the file
def main():

    #open a file named philosophers.txt
    outfile = open("philosophers.txt", "a")

#write the name of three philosophers
#to the file
    outfile.write("John Locke\n")
    outfile.write("David Hume\n")
    outfile.write("Edmud Burke\n")
    outfile.write("Wuttimetee Kanharee\n")

# close the file
    outfile.close()

#call the main function
main()
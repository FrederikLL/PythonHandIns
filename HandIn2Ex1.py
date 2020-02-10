import sys
import getopt
import argparse
#1
filecli = str(sys.argv[1])
#A

def print_file_content(file):
    #file_path = 'C:\\Users\\Bruger\\Documents\\4semester\\Python\\csvtest.csv' 
    with open(file) as file_object:
        for line in file_object:
            print(line)

print_file_content(filecli)
#B
randlst = [(1,2),(3,4),(5,6),("string1","String2")]
def write_list_to_file(output_file, lst):
    with open(output_file, 'w') as file_object1:
        #for item in lst:
        file_object1.write("\n".join(str(item) for item in lst))
        
#Virker, men udkommenteret
#write_list_to_file('C:\\Users\\Bruger\\Documents\\4semester\\Python\\pytfilecopyto.txt',randlst)
#print('File got new data!')

#Ba
#Not sure i understand the assignment
def write_list_to_file_with_str(output_file1, *str1):
    with open(output_file1, 'w') as file_object1:
        file_object1.write("\n".join(str1))

#virker men udkommenteret
#write_list_to_file_with_str('C:\\Users\\Bruger\\Documents\\4semester\\Python\\pytfilecopyto.txt',"Hej", "test", "niels")

#C
def read_csv(input_file):
    with open(input_file) as file_object:
        lines = file_object.readlines()

    for line in lines:
        print(line.rstrip())

print_file_content('C:\\Users\\Bruger\\Documents\\4semester\\Python\\csvtest.csv')

#2 og 3
#A og B
#C:\\Users\\Bruger\\Documents\\4semester\\Python\\csvtest.csv
#I assign the argv just below imports
# def clifunc(argv):
#     inputfile = ''
#     try:
#         opts,args= getopt.getopt(argv, "hi:f:", ["ifile=","file="])
#         print('hi1')
#     except getopt.GetoptError:
#         print('HandIn2Ex1.py <filetoreadfrom> --file <filetoreadto>')
#         sys.exit(2)
#     for option, arg in opts:
#         print('hi')
#         if option == '-h':
#             print('HandIn2Ex1.py <filetoreadfrom> --file <filetoreadto>')
#             sys.exit()
#         elif option in ("-i", "--ifile"):
#             inputfile = arg
#         elif option in ("-f", "--file"):
#             with open(inputfile) as file_object:
#                 for line in file_object:
#                     with open(arg, 'w') as file_object2:
#                         file_object2.write("\n" + line)
#                         print('yo')
#     print('did we get here')
# if __name__ == "__main__" :
#     clifunc(sys.argv[1:])

parser = argparse.ArgumentParser()
parser.add_argument("readfrom", help="File to read from")
parser.add_argument('-f', '--file', help='File to write to')
#parser.add_argument('-h', '--help', help="this is the help",)

args = parser.parse_args()

filefrom = args.readfrom
fileto = args.file
#helpz = 'HandIn2Ex1.py <filetoreadfrom> --file <filetoreadto>'
#print(helpz)

with open(filefrom) as file_object:
    for line in file_object:
        print(line)
        with open(fileto, 'a') as file_object2:
            file_object2.write('\n' + line)
            print(line)

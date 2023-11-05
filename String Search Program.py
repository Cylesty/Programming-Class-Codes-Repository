# Collaborators: Alano Davin Mandagi Awuy - 2306172363 & Flori Andrea Ng - 2306171713 & Bryant Warrick Cai - 2306256255

import time
import os
import sys

# Function for finding tag of a file
def find_tag(file_name, tag):
    with open(file_name, 'r') as f:
        first_line = f.readline().strip('\n')           # Reads the first line from the file and remove the newline character (\'n') / empty space
        line_lst = first_line.split()                   # Splits the first line into a list of words
        found_tag = [x for x in line_lst if tag in x]   # Filters the first line and creates a list containing the specified tag
        found_tag = found_tag[0]                        # Gets the first element from the list as a string to manipulate it ( can use .replace on it )
        found_tag = found_tag.replace(tag, '').replace("=", '').replace('"', '')  # Remove the specified tag, equal sign, and double quotes, leaving only the tag 
        return found_tag  # Returns the bare tag (word only such as jateng)


# Function for making list of output
def output_list(file_name, file, province, class_, subclass_, judicial_inst):
    file.append(file_name)                                         # Appends name of the target file to file list
    province.append(find_tag(file_name, 'provinsi'))               # Apennds provinsi tag to province list
    class_.append(find_tag(file_name, 'klasifikasi'))              # Apennds klasifikasi tag to class_ list
    subclass_.append(find_tag(file_name, 'sub_klasifikasi'))       # Apennds sub_klasifikasi tag to _subclass list
    judicial_inst.append(find_tag(file_name, 'lembaga_peradilan')) # Apennds lembaga_peradilan to judicial_inst(itution) list

# Function for searching keywords in files
def search_files(search_tag, keyword_1, operator, keyword_2):
    main_list = [[], [], [], [], []]    # Placeholder for list
    if search_tag == "all":
        start_tag = "<putusan"
        end_tag   = "</putusan>"

    else: # For the other 10 tag types
        start_tag = f"<{search_tag}>"
        end_tag   = f"</{search_tag}>"


    for file_name in dataset: # Iterates through every file in dataset
        with open(file_name, 'r') as doc: # Opens file and reads data in file without needing to close it manually
            read_file = doc.read()
            start_num = read_file.find(start_tag) # Variable for finding starting tag
            end_num = read_file.find(end_tag)     # Variable for finding ending tag
            tag_content = read_file[start_num + len(start_tag):end_num].strip()     # Takes content between tags
            if operator == "OR" and (keyword_1 in tag_content or keyword_2 in tag_content):
                output_list(file_name, *main_list) # Calls output_list function with mentioned operator
            elif operator == "AND" and (keyword_1 in tag_content and keyword_2 in tag_content):
                output_list(file_name, *main_list)
            elif operator == "ANDNOT" and (keyword_1 in tag_content and keyword_2 not in tag_content):
                output_list(file_name, *main_list)
            elif operator == "NONE" and (keyword_1 in tag_content):
                output_list(file_name, *main_list)
    return main_list

# Function for output
def print_document_list(file, province, class_, subclass_, judicial_inst):
    for i in range(len(file)):  # Iterates through range of file elements
        col0 = file[i]          # Takes string of 'file' element at index 'i'
        col1 = province[i]      # Same as above line
        col2 = class_[i]
        col3 = subclass_[i]
        col4 = judicial_inst[i]
        print(f"{col0} {col1.rjust(15)} {col2.rjust(15)} {col3.rjust(30)} {col4.rjust(20)}") # Justifies text to the right, number is character limit
    print()
    print(f"Total number of documents = {len(file)}") # len(file) takes the number of elements in the range

result = [[], [], [], [], []]   # Placeholder list for results

if __name__ == "__main__":      # Run code only when it's not being imported

    start = time.time()         # Starts measuring time when the program is executed

    path = "C:\\Users\\matri\\Desktop\\Codes\\Programming Tasks\\TP02\\dataset"  # Sets path variable
    os.chdir(path)              # Change the current working directory to this path
    dataset = os.listdir(path)  # Lists all files in the directory

    if len(sys.argv) == 3:      # If user input has search_tag and keyword_1 then proceed
        operator = 'NONE'       # Default operator if not provided
        result = search_files(sys.argv[1], sys.argv[2], operator, '')  # Calls 'search_files' based on specified criteria

    elif len(sys.argv) == 5:    # If user input has search_tag, keyword_1, operator, and keyword_2 then proceed ( 5 elements )
        operator = sys.argv[3]  # assigns operator as 3rd element in sys.argv

        if operator not in ['AND', 'OR', 'ANDNOT']:            # Validation for operator
            print("The operator must be AND, OR, or ANDNOT.")  # Display an error message for invalid operator
            sys.exit(1)  # Exits program
        result = search_files(sys.argv[1], sys.argv[2], operator, sys.argv[4]) # Calls 'search_files' based on specified criteria.

    else: # Validation for arguments and keywords
        print("The program argument is incorrect.") # Displays an error message for incorrect arguments
        print()
        sys.exit(1)  # Exits the program

    file, province, class_, subclass_, judicial_inst = result              # Unpacks the 'result' list into separate variables for easier access to its contents.
    print_document_list(file, province, class_, subclass_, judicial_inst)  # Prints the output list

    end = time.time()       # Stops measuring time when the program is done being executed
    run_time = end - start  # Finds the time taken for the program to execute
    print()
    print(f"Total search time         = {run_time:.3f} seconds" + '\n')


# sample input: python -u "C:\Users\matri\Desktop\Codes\Programming Tasks\TP02\KKI_SEA_2306256223_AmeeraKhairaTawfiqa_TP02.py" fakta "kebakaran hutan" ORXX "narkotika gol onga"

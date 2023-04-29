import re

print("Supported file formats:\n")
print("XML - Removes spaces between XML tags.")
print("EDI - Compares two EDI files and checks if they have the same structure.\n")
file_format = input("Enter the file format you want to edit: ")

if file_format.upper() == 'XML' or 'EDI':

    file_name = input("Enter the name of the file you want to edit: ")

    try:
        test_file = open(file_name, "r")
    except FileNotFoundError:
        print("File does not exist in the current directory.")
        exit()
    else:
        name_of_file, file_extension = file_name.split(".")

        if file_extension.upper() == 'XML':
            line = test_file.read()
            pattern = r'>\s+<'
            if re.search(pattern, line):
                edit_file = re.sub(pattern, '><', line)
                creating_new_file = name_of_file + "_edited." + file_extension
                new_file = open(creating_new_file, "w")
                new_file.write(edit_file)
                test_file.close()
                new_file.close()
                print(f"\n{file_name} has been successfully processed with no white spaces between the tags.")
            else:
                print(f'No spaces between XML tags were found.')

        elif file_extension.upper() == 'EDI':
            file_name2 = input("Enter the name of the second file to be compared: ")
            try:
                with open(file_name2, "r") as test_file2:
                    file1_content = test_file.read()
                    file2_content = test_file2.read()
                pattern = r'\b[a-zA-Z]{3}\b'
                file1_segments = re.findall(pattern, file1_content)
                file2_segments = re.findall(pattern, file2_content)
                if file1_segments == file2_segments:
                    print("The structure of the two files are identical.")
                else:
                    different_segments_file1 = []
                    different_segments_file2 = []
                    for i, segment in enumerate(file1_segments):
                        if segment != file2_segments[i]:
                            different_segments_file1.append(segment)
                            different_segments_file2.append(file2_segments[i])
                    print(f"\nThe two files have different segments. \nIn file '{file_name}' "
                          f"different segments are {different_segments_file1}, and in file '{file_name2}' are {different_segments_file2}")
                    test_file.close()
                    test_file2.close()
            except FileNotFoundError:
                print("One or both files do not exist in the current directory.")
                exit()
        else:
            print("File format not supported.")
            exit()

else:
    print('The file format you have selected is not supported.')

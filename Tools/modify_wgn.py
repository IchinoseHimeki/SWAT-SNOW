'''
File: modify_wgn.py
File Created: 2023-10-10 11:20:18
Author: IchinoseHimeki (darwinlee19980811@hotmail.com)
-----
Last Modified: 2023-10-10 11:23:25
Modified By: IchinoseHimeki (darwinlee19980811@hotmail.com>)
-----
Copyright 2023
Requisite: python 3.x
Description: Modifiy all .wgn files accordingly to meet new swat model data input requirements.
'''
import os

# Function to modify the .wgn files
def modify_wgn_file(file_path, output_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    # Check if the file has at least 3 lines to modify
    if len(lines) < 3:
        print(f"{file_path} does not have enough lines to modify. Skipping.")
        return
    
    # Extracting the LONGITUDE info from the second line
    line_2_parts = lines[1].split('LONGITUDE =')
    if len(line_2_parts) < 2:
        print(f"Could not find LONGITUDE info in {file_path}. Skipping.")
        return
    
    # Creating the new second and third lines
    new_line_2 = line_2_parts[0].strip() + '\n'
    new_line_3 = ' LONGITUDE =' + line_2_parts[1].strip() + '\n'
    
    # Modifying the file content
    new_lines = [lines[0], new_line_2, new_line_3] + lines[2:]
    
    # Writing the modified content to a new file
    with open(output_path, 'w') as file:
        file.writelines(new_lines)
    
    print(f"File {file_path} modified successfully. Output saved to {output_path}.")

wgnlists = [os.path.join(os.getcwd(), file) for file in os.listdir(os.getcwd()) if file.endswith('.wgn')]
for i in wgnlists:
    modify_wgn_file(i,i)
import os



def get_folder_size(folder_path):
    total_size = 0
    file_names = []  # List to store file names
    for dirpath, dirnames, filenames in os.walk(folder_path):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            
            if not os.path.islink(file_path):  # Ignore symbolic links
                total_size += os.path.getsize(file_path)
                file_names.append(filename)  # Add file name to the list
                new_path = os.path.join('/Users/walidsphone./Desktop/scratchproject/Games/GameFiles', filename)
                os.rename(file_path, new_path)
                
    return total_size, file_names


folder_path = "/Users/walidsphone./Desktop/pss"  # Replace with your folder path
folder_size, file_names = get_folder_size(folder_path)
print(f"Total size of the folder '{folder_path}' is: {folder_size} bytes")
print("File names within the folder:")
x=''
for name in file_names:
    x=name
    print(name)


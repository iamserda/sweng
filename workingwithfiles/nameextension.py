import os

def manual_get_filename_and_fileextension(folder_path):
    for item in os.listdir(folder_path):
        if os.path.isfile(folder_path + item):
            # the file extension
            index = len(item) - 1
            while item[index] != ".":
                index -= 1

            # moving the index ahead of the '.' from the previous loop
            end_index = index
            
            #extracting the file name
            while item[index] != "/":
                index -= 1
                if index >= 0:
                    start_index = index
                else:
                    break
            print(f"filename: {item[start_index:end_index]}, ext: {item[end_index:]}")

manual_get_filename_and_fileextension("../")

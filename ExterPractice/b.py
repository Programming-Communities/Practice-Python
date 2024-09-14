import os

base_path = r'C:\Users\Aamir\Desktop\New folder'

num_folders = 100

for i in range(1, num_folders + 1):
    folder_name = f'folder_{i}'
    folder_path = os.path.join(base_path, folder_name)
    os.makedirs(folder_path, exist_ok=True)

    
    print(f'Created folder: {folder_name}')

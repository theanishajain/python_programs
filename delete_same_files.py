import os
import hashlib
import stat


def get_file_checksum(file_path):
    """Calculate and return the checksum of a file."""
    hasher = hashlib.md5()
    with open(file_path, 'rb') as f:
        buf = f.read()
        hasher.update(buf)
    return hasher.hexdigest()

def find_and_delete_duplicates(folder_path):
    """Find and delete duplicate files in the given folder."""
    file_hashes = {}
    duplicates = []
    os.chmod(duplicates, stat.S_IWRITE)  # Change file to writable
    os.remove(duplicates)
    
    # Iterate through all files in the folder
    for root, _, files in os.walk("C:\\Users\\Anisha\\Desktop\\PYTHON_ALL"):
        for file in files:
            file_path = os.path.join(root, file)
            checksum = get_file_checksum(file_path)
            
            if checksum in file_hashes:
                duplicates.append(file_path)
            else:
                file_hashes[checksum] = file_path

    # Delete duplicates
    for duplicate in duplicates:
        print(f"Deleting duplicate file: {duplicate}")
        os.remove(duplicate)

    if not duplicates:
        print("No duplicate files found.")
    else:
        print("Duplicate files deleted successfully.")

# Set the folder path
find_and_delete_duplicates("C:\\Users\\Anisha\\Desktop\\PYTHON_ALL")

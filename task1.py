import hashlib

def calculate_hash(file_path):
    sha256 = hashlib.sha256()

    with open(file_path, "rb") as file:
        while chunk := file.read(4096):
            sha256.update(chunk)

    return sha256.hexdigest()

# Original file
file_path = input("Enter file path: ")

original_hash = calculate_hash(file_path)
print("\nOriginal Hash:")
print(original_hash)

input("\nPress Enter after making changes to the file...")

new_hash = calculate_hash(file_path)

print("\nNew Hash:")
print(new_hash)

if original_hash == new_hash:
    print("\n[+] File Integrity Maintained")
else:
    print("\n[-] File Has Been Modified")
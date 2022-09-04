def main():
#prompt user for file name and extension
    file = input("File name: ")
    file = file.lower()
    extension(file)

def extension(f):

#create list of available file extensions
    file_extensions = ["GIF/.gif", "IMAGE/.jpeg", "PNG/.png", "PDF/.pdf", "TXT/.txt", "ZIP/.zip"]
    error = "application/octet-stream" 

#recognize file by ".extension", else output application/octet-stream
    if ".gif" in f:
        print(file_extensions[0])
    elif ".jpeg" in f:
        print(file_extensions[1])
    elif ".jpg" in f:
        print(file_extensions[1])
    elif ".png" in f:
        print(file_extensions[2])
    elif ".pdf" in f:
        print(file_extensions[3])
    elif ".txt" in f:
        print(file_extensions[4])
    elif ".zip" in f:
        print(file_extensions[5])    
    else:
        print(error)

main()
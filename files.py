def main():
#prompt user for file name and extension
    file = input("File name: ")
    file = file.lower()
    extension(file)

def extension(f):

#create list of available file extensions
    file_extentions = ["GIF/.gif", "IMAGE/.jpeg", "PNG/.png", "PDF/.pdf", "TXT/.txt", "ZIP/.zip"]
    error = "application/octet-stream" 

#recognize file by ".extension"

#else output application/octet-stream


main()
def main():
# prompt user for file name and extention
    file = input("Name of file: ")
    file = file.lower()
    extention(file)
    
# implement function that checks the file extention
def extention():
# create list of available files
    file_extentions = ["GIF/.gif", "IMAGE/.jpeg", "PNG/.png", "PDF/.pdf", "TXT/.txt", "ZIP/.zip"]
    error = ["application/octet-stream"]

# recognize file by ".file_extention"

# else output application/octet-stream

main() 
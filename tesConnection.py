from ftplib import FTP

# Connect to the FTP server
ftp = FTP()
ftp.connect('dossier.plnnusantarapower.co.id', port=21)
ftp.login(user='dossier', passwd='dossier')

# Check if login was successful
welcome_message = ftp.getwelcome()
print(welcome_message)

# list all folders in the current directory
# print("File List:")
# files = ftp.dir()
# print(files)

# Change the current directory into /LOADER
# ftp.cwd('LOADER')
# print("File List:")
# files = ftp.dir()
# print(files)

# Change the current directory into /LOADER
ftp.cwd('LOADER')

# Get the list of filenames in the current directory
filenames = ftp.nlst()

# Specify the full path to the output file
output_file = '/Users/guntar/OneDrive/0B Projects/78 Olah Folder Sertifikat PJCA/fileList.txt'

# Open the output text file and write the filenames to it
with open(output_file, 'w') as f:
    for filename in filenames:
        f.write(filename + '\n')

print(f"Filenames have been written to {output_file}")

# Use the LIST command
# ftp.retrlines('LIST')

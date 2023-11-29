from ftplib import FTP
import os
import shutil

# FTP server details
ftp_server = "dossier.plnnusantarapower.co.id"
ftp_username = "dossier"
ftp_password = "dossier"

# Connect to the FTP server
ftp = FTP()
ftp.connect(ftp_server, port=21)
ftp.login(user=ftp_username, passwd=ftp_password)

# Local directory containing PDF files
local_directory = "/Users/guntar/Documents/Working Files/Data/DataUploadVPN"
done_upload_directory = "/Users/guntar/Documents/Working Files/Data/FileDoneUpload"
remote_path = 'LOADER'

# Change to the remote directory
ftp.cwd(remote_path)

# List all files in the local directory
files = os.listdir(local_directory)
total_files = len(files)

# Counter for uploaded files
uploaded_files = 0

# Upload each file to the FTP server
for file in files:
    local_file_path = os.path.join(local_directory, file)
    with open(local_file_path, 'rb') as local_file:
        ftp.storbinary('STOR ' + file, local_file)
        uploaded_files += 1
        print(f"File {file} uploaded successfully")
        # Move the file to the done upload directory
        shutil.move(local_file_path, os.path.join(done_upload_directory, file))
        # Print the upload progress
        print(f"💬 Upload progress: {uploaded_files/total_files*100:.2f}% ({uploaded_files} of {total_files} files)")

# Close the FTP connection
ftp.quit()
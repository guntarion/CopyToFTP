from ftplib import FTP
import os

# FTP server details
from ftplib import FTP

# FTP server details
ftp_server = "dossier.plnnusantarapower.co.id"
ftp_username = "dossier"
ftp_password = "dossier"

# Connect to the FTP server
ftp = FTP()
ftp.connect(ftp_server, port=21)
ftp.login(user=ftp_username, passwd=ftp_password)

# Local directory containing PDF files
local_directory = "/Users/guntar/Documents/Working Files/Data/FileToBeCopied"
remote_path = 'LOADER'

# Function to upload a file with progress information
def upload_file(ftp, local_file_path, remote_file_path):
    with open(local_file_path, "rb") as local_file:
        ftp.storbinary(f"STOR {remote_file_path}",
                       local_file, 8192, callback=print_progress)

# Function to print upload progress
def print_progress(data):
    uploaded_bytes = len(data)
    print(f"Uploaded {uploaded_bytes} bytes", end="\r")

# Connect to the FTP server
with FTP(ftp_server) as ftp:
    ftp.login(user=ftp_username, passwd=ftp_password)

    # Check if login was successful
    welcome_message = ftp.getwelcome()
    print(welcome_message)

    # Change to the remote directory
    ftp.cwd(remote_path)
    print("File List:")
    files = ftp.dir()
    print(files)

    # List PDF files in the local directory
    pdf_files = [file for file in os.listdir(
        local_directory) if file.endswith(".pdf")]
    ## list all those .pdf files in the local directory
    print(pdf_files)
    
    # Upload each PDF file
    for pdf_file in pdf_files:
        local_path = os.path.join(local_directory, pdf_file)
        remote_path = remote_path + '/' + pdf_file

        # Upload the file with progress info
        upload_file(ftp, local_path, remote_path)

        # Ensure the upload is complete
        # NOOP command does nothing but checks the connection status
        ftp.voidcmd("NOOP")

    # Print a message when all files are uploaded
    print("\nAll files uploaded successfully.")


# Connect to the FTP server
with FTP(ftp_server) as ftp:
    ftp.login(user=ftp_username, passwd=ftp_password)

    # Check if login was successful
    welcome_message = ftp.getwelcome()
    print(welcome_message)

    # Change to the remote directory
    ftp.cwd(remote_path)
    print("File List:")
    files = ftp.dir()
    print(files)

    # List PDF files in the local directory
    pdf_files = [file for file in os.listdir(
        local_directory) if file.endswith(".pdf")]
    ## list all those .pdf files in the local directory
    print(pdf_files)
    
    # Upload each PDF file
    for pdf_file in pdf_files:
        local_path = os.path.join(local_directory, pdf_file)
        remote_path = remote_path + '/' + pdf_file

        # Upload the file with progress info
        upload_file(ftp, local_path, remote_path)

        # Ensure the upload is complete
        # NOOP command does nothing but checks the connection status
        ftp.voidcmd("NOOP")

    # Print a message when all files are uploaded
    print("\nAll files uploaded successfully.")

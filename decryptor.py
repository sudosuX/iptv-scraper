import pyzipper
import os

def decrypt_zip(zip_file_path, output_dir, password):
    try:
        with pyzipper.AESZipFile(zip_file_path) as zf:
            # Check if the provided password is correct
            try:
                zf.setpassword(password.encode('utf-8'))
                zf.extractall(output_dir)
                print("Decryption successful.")
            except RuntimeError:
                print("Incorrect password provided. Decryption failed.")
    except Exception as e:
        print(f"An error occurred during decryption: {e}")

if __name__ == "__main__":
    # Retrieve the password from GitHub repository secrets
    password = os.environ.get("PASSWORD", "")
    
    # Specify the path to the encrypted ZIP file
    zip_file_path = 'encrypted.zip'
    
    # Specify the output directory for the extracted files
    output_dir = 'output'
    
    # Decrypt the ZIP file
    decrypt_zip(zip_file_path, output_dir, password)

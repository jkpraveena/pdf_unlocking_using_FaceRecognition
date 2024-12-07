#TO LOCK THE FILE 

import PyPDF2

def lock_pdf(input_pdf_path, output_pdf_path, password):
    # Open the original PDF
    with open(input_pdf_path, 'rb') as input_file:
        pdf_reader = PyPDF2.PdfReader(input_file)
        pdf_writer = PyPDF2.PdfWriter()

        # Add all pages to the PDF writer
        for page_num in range(len(pdf_reader.pages)):
            pdf_writer.add_page(pdf_reader.pages[page_num])

        # Add password protection
        pdf_writer.encrypt(password)

        # Write the locked PDF to a new file
        with open(output_pdf_path, 'wb') as output_file:
            pdf_writer.write(output_file)

    print(f"PDF locked with password and saved to {output_pdf_path}")

# Example Usage:
input_pdf = 'pdf_path'
output_pdf = 'pdf_path'
password = 'your_password'
lock_pdf(input_pdf, output_pdf, password)

# UNLOCKING PDFS AND DOCUMENTS USING FACE RECOGNITION

import cv2
import numpy as np
import face_recognition
from PyPDF2 import PdfReader, PdfWriter
import subprocess
import io
import sys
import tempfile
import os

# Function to register a face
def register_face():
    print("Position your face in front of the camera to register.")
    video_capture = cv2.VideoCapture(0)
    face_encodings = []

    while True:
        ret, frame = video_capture.read()
        if not ret:
            break

        # Find faces in the current frame
        face_locations = face_recognition.face_locations(frame)
        if face_locations:
            face_encoding = face_recognition.face_encodings(frame, face_locations)[0]
            face_encodings.append(face_encoding)
            cv2.imshow("Registering Face", frame)
            print("Face registered successfully!")
            break

    video_capture.release()
    cv2.destroyAllWindows()

    if face_encodings:
        # Save the encoding as a NumPy array instead of bytes
        np.save("registered_face.npy", face_encodings[0])
        print("Registered face saved as a NumPy array.")

# Function to login using the face recognition
def login_face():
    print("Position your face in front of the camera to login.")
    video_capture = cv2.VideoCapture(0)

    # Load the saved NumPy array encoding
    registered_face_encoding = np.load("registered_face.npy")

    while True:
        ret, frame = video_capture.read()
        if not ret:
            break

        # Find faces in the current frame
        face_locations = face_recognition.face_locations(frame)
        if face_locations:
            face_encoding = face_recognition.face_encodings(frame, face_locations)[0]
            matches = face_recognition.compare_faces([registered_face_encoding], face_encoding)

            if True in matches:
                print("Login successful! Unlocking document...")
                video_capture.release()
                cv2.destroyAllWindows()
                return True

    video_capture.release()
    cv2.destroyAllWindows()
    return False

# Function to unlock the document
def unlock_pdf(pdf_path, password):
    try:
        # Attempt to decrypt the PDF
        reader = PdfReader(pdf_path)
        if reader.is_encrypted:
            # Try decrypting the file
            if reader.decrypt(password):
                print("File decrypted successfully.")
                
                # Create a byte stream to store the decrypted PDF
                writer = PdfWriter()
                for page in reader.pages:
                    writer.add_page(page)

                # Write to a byte stream instead of a file
                byte_stream = io.BytesIO()
                writer.write(byte_stream)

                # Rewind the byte stream and save it to a temporary file
                byte_stream.seek(0)

                # Create a temporary file to save the decrypted PDF
                with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_pdf:
                    temp_pdf_path = temp_pdf.name
                    with open(temp_pdf_path, 'wb') as temp_file:
                        temp_file.write(byte_stream.read())

                print(f"Temporary decrypted file saved as {temp_pdf_path}")

                # Open the temporary file in the system's default PDF viewer
                if sys.platform == 'darwin':  # macOS
                    subprocess.Popen(['open', temp_pdf_path])
                elif sys.platform == 'linux':  # Linux
                    subprocess.Popen(['xdg-open', temp_pdf_path])
                else:
                    print("Unsupported OS for direct PDF opening.")
                print("PDF opened successfully.")
            else:
                print("Failed to decrypt the document. Incorrect password or encryption issue.")
        else:
            print("The document is not encrypted.")
    except Exception as e:
        print(f"Failed to unlock the document: {e}")

# Main function to control the flow
def main():
    action = input("Do you want to register or login? (r/l): ").lower()

    if action == "r":
        register_face()
    elif action == "l":
        if login_face():
            pdf_path = 'pdf_path'  # Specify your PDF path here
            password = 'your_password'  # Specify the password for your encrypted PDF here
            unlock_pdf(pdf_path, password)
        else:
            print("Face login failed.")
    else:
        print("Invalid option. Please choose 'r' to register or 'l' to login.")

if __name__ == "__main__":
    main()

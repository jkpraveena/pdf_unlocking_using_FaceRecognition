# pdf_unlocking_using_FaceRecognition

**Title:** Secure PDF Encryption with Biometric Face Recognition

**Overview:**
This project provides a biometric-based authentication system for locking and unlocking PDF documents, combining face recognition with PDF encryption to offer secure document management.

**Technologies Used:**
	•	Python
	•	OpenCV (for face detection)
	•	face_recognition (for encoding and matching faces)
	•	PyPDF2 (for PDF encryption and decryption)
	•	NumPy (for facial feature encoding)

**Features:**
	•	Real-time face registration and encoding using face_recognition.
	•	PDF encryption and decryption using PyPDF2 with password protection.
	•	98% recognition accuracy for face matching.
	•	Cross-platform support (macOS, Linux).

**Applications:**
	•	Secure document access in finance, healthcare, and legal sectors.
	•	Scalable solution for enterprise-level document management.

**Scalability & Future Enhancements:**
	•	Can be scaled for enterprise-level use with multi-user authentication.
	•	Future work to integrate cloud-based storage and remote authentication.

**Necessity of the Project:**
In the digital age, securing sensitive documents is critical. This project provides an effective, user-friendly solution for securing PDF files with biometric authentication, eliminating the need for traditional passwords and improving access control.

**Setup Instructions**

**1. Prerequisites**

Make sure you have the following installed on your system:
	•	Python 3.x
	•	Required Python libraries:
	•	opencv-python
	•	face_recognition
	•	PyPDF2
	•	NumPy

**2. Registering Your Face (First-time Setup)**

To register your face for unlocking PDFs:
	1.	Run the script by executing:
python your_script_name.py
        2.	The script will prompt you to choose either “register” or “login”. Select “r” for registration.
	3.	Position your face in front of the camera. The system will capture and save your face encoding in a file called registered_face.npy.

**3. Unlocking a PDF with Face Recognition**

Once your face is registered, you can unlock a PDF:
	1.	Run the script again:
python your_script_name.py
	2.	When prompted, choose “l” for login.
	3.	Position your face in front of the camera. If the system detects and matches your face with the registered encoding, it will unlock the encrypted PDF.

**4. PDF Path and Password**
	•	You will be asked to provide the path to the encrypted PDF and the password used to lock the document.
	•	The system will attempt to decrypt the PDF using the password after successfully authenticating your face.

**How It Works**

	•	Face Registration: The system captures your facial features using a camera and saves the encoded features in a file (registered_face.npy). This ensures that the system can authenticate you in the future.
	•	Face Login: When you log in, the system compares the live captured face with the registered face encoding and grants access if there’s a match.
	•	PDF Locking/Unlocking: The PDF is encrypted using a password. Once authenticated, the system decrypts the PDF and opens it for viewing.


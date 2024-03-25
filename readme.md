## Welcome to Python Password Manager (Version 1.0)
---
**Securely Manage Your Passwords**

Welcome to Python Password Manager, your trusted solution for securely managing your passwords. With Python Password Manager, you can store your sensitive credentials with confidence, knowing that they are protected using state-of-the-art encryption techniques.

**Master Password Encryption**

To begin using Python Password Manager, you will be prompted to create a master password. This master password will be securely encrypted using a 256-bit hash, ensuring that only you have access to your password vault.

**AES-256 Encryption for Secrets**

Your passwords and other secrets stored within Python Password Manager are encrypted using AES-256, a robust encryption algorithm. This ensures that your sensitive information remains confidential and protected from unauthorized access.

## How to Use
---
**Installation Guide for Python Virtual Environment**

To ensure a clean and isolated environment for running Python Password Manager, it is recommended to set up a Python virtual environment. Follow these steps to install Python virtual environment and get started with Python Password Manager:

1. **Clone the Repository:** Begin by cloning the Python Password Manager repository to your local machine using the following command:
   git clone <repository-url>
   
2. **Navigate to the Project Directory:** Move into the directory of the cloned repository:
   cd python-password-manager
   
3. **Install Python Virtual Environment (virtualenv):** If you haven't already installed `virtualenv`, you can install it via pip:
   pip install virtualenv
   
4. **Create a Virtual Environment:** Create a virtual environment for Python Password Manager using the following command:
   virtualenv venv
   
5. **Activate the Virtual Environment:** Activate the virtual environment by running the activation script according to your operating system:
   - On Windows:
     venv\Scripts\activate
   - On macOS and Linux:
     source venv/bin/activate
   
6. **Install Required Dependencies:** With the virtual environment activated, install the required dependencies listed in the `requirements.txt` file:
   pip install -r requirements.txt
   
7. **Run Python Password Manager:** Once the dependencies are installed, you can now run Python Password Manager using Python:
   python main.py

With these steps completed, you have successfully set up Python virtual environment and installed Python Password Manager. You can now start using the password manager to securely store and manage your passwords offline.

## Some Commands

List secrets
```
[pw-manager]: /ls
+----+--------+---------------------+---------------------+
| Id |  Key   |    Created Date     |    Updated Date     |
+====+========+=====================+=====================+
| 1  | teste  | 2024-03-17 17:37:13 | 2024-03-17 17:37:13 |
+----+--------+---------------------+---------------------+
| 2  | teste2 | 2024-03-17 17:59:08 | 2024-03-17 17:59:08 |
+----+--------+---------------------+---------------------+
| 3  | amazon | 2024-03-24 23:11:47 | 2024-03-24 23:12:05 |
```

List secret history:
```
[pw-manager]: /lsh amazon
+----+--------+---------------------+-------+
| Id |  Key   |    Created Date     | Value |
+====+========+=====================+=======+
| 1  | amazon | 2024-03-24 23:11:47 | 1234  |
+----+--------+---------------------+-------+
| 2  | amazon | 2024-03-24 23:11:55 | 4321  |
+----+--------+---------------------+-------+
| 3  | amazon | 2024-03-24 23:12:05 | 5432  |
+----+--------+---------------------+-------+
```

**Coming Soon in Future Updates:**

In the next update, The Password Manager will be upgraded to be executable and capable of running in Linux as a Debian package. Stay tuned for enhanced usability and compatibility.
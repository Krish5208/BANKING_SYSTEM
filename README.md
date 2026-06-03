# Banking Management System with Biometric Authentication

A Python-based Banking Management System that combines traditional banking operations with modern biometric authentication methods. The system allows users to securely access their bank account using real-time face detection, Windows Hello verification, or account number and PIN authentication.

---

## Features

### Authentication System

* Real-time Face Detection using OpenCV
* Windows Hello Authentication Support
* Account Number and PIN Login
* Multi-level security verification
* Automatic fallback to PIN login if biometric authentication fails

### Banking Operations

* Deposit Money
* Withdraw Money
* Balance Inquiry
* Fixed Deposit (FD) Creation
* View Active Fixed Deposits
* Close Fixed Deposits with Penalty Calculation
* Secure Logout System

### Fixed Deposit Module

* Create Fixed Deposits from available balance
* Calculate maturity amount automatically
* Display FD details including amount, tenure, and interest rate
* Early FD closure with penalty deduction

---

## Technologies Used

* Python
* OpenCV
* Haar Cascade Classifier
* Windows Hello
* Object-Oriented Programming (OOP)

---

## Project Structure

```text
Banking-System/
│
├── main.py
├── biometric_auth.py
└── README.md
```

---

## System Workflow

1. User launches the application.
2. User chooses authentication method:

   * Biometric Login
   * PIN Login
3. Face Detection verifies user presence.
4. Windows Hello verification is performed.
5. After successful authentication, banking services become available.
6. User can perform transactions and manage Fixed Deposits.
7. User logs out securely.

---

## How to Run ?

### 1. Clone Repository

```bash
git clone https://github.com/yourusername/banking-system.git
```

### 2. Navigate to Project Folder

```bash
cd banking-system
```

### 3. Install Required Libraries

```bash
pip install opencv-python
```

### 4. Run Application

```bash
python main.py
```

---

## 📸 Authentication Methods

### Face Detection Authentication

The system uses OpenCV's Haar Cascade Classifier to detect faces in real time through the webcam.

### Windows Hello Authentication

Users can verify their identity using Windows Hello facial recognition or fingerprint authentication.

### PIN Authentication

As a backup option, users can log in using their Account Number and PIN.

---

## Learning Outcomes

This project demonstrates:

* Object-Oriented Programming in Python
* Computer Vision using OpenCV
* Biometric Authentication Concepts
* Banking Transaction Management
* Security-Oriented Application Development

---

## Future Enhancements

* Database Integration (MySQL / SQLite)
* Transaction History
* Account Registration System
* OTP Verification
* GUI using Tkinter or PyQt
* Multiple User Accounts
* Fingerprint API Integration
* Secure Password Hashing

---

## Author

Krish Zalavadiya

Python Developer | Computer Vision Enthusiast | Information Technology Student

---



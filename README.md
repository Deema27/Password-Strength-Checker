# Pygame Password Strength Checker

A graphical password strength checker built with **Python**, **Pygame**, and **pygwidgets**.  
This application allows users to enter a password, validates it against standard security rules, and provides immediate feedback on its strength.

---

## Features

- **Password Validation Rules**
  - Minimum 15 characters
  - At least one lowercase letter
  - At least one uppercase letter
  - At least one number
  - At least one special character
  - No whitespace characters

- **Password Strength Assessment**
  - Very strong: meets all criteria
  - Moderate: meets most criteria
  - Weak: fails multiple criteria

- **Graphical User Interface**
  - Pygame window with input box
  - Enter button to submit password
  - Dynamic feedback messages displayed below input box
  - Backspace and normal typing supported

- **Object-Oriented Design**
  - `PasswordChecker` class encapsulates password data using private variables
  - Methods to analyze, validate, and assess strength
  - Easy to extend and maintain

---

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Deema27/Password-Strength-Checker.git
   cd Password-Strength-Checker

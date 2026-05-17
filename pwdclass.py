import string  # For checking letters, digits, and special characters

class PasswordChecker:
    
    """
    A class to analyze password strength and validate password rules.
    Uses private variables to encapsulate internal data.
    """

    def __init__(self, password):
        # ----------------------------
        # Private variables
        # ----------------------------
        self.__password = password           # The password itself
        self.__lower_count = 0               # Number of lowercase letters
        self.__upper_count = 0               # Number of uppercase letters
        self.__num_count = 0                 # Number of digits
        self.__specialchar_count = 0         # Number of special characters
        self.__whitespace_count = 0          # Number of whitespace characters
        self.__length = len(password)        # Length of the password

    def analyze(self):
        
        """
        Analyze the password and count different types of characters.
        Resets all counters before calculation.
        """
        
        # Reset all counts
        self.__lower_count = self.__upper_count = self.__num_count = 0
        self.__specialchar_count = self.__whitespace_count = 0
        self.__length = len(self.__password)

        # Loop through each character in the password
        for char in self.__password:
            
            if char in string.ascii_lowercase:
                self.__lower_count += 1
                
            elif char in string.ascii_uppercase:
                self.__upper_count += 1
                
            elif char in string.digits:
                self.__num_count += 1
                
            elif char == ' ':
                self.__whitespace_count += 1
                
            else:
                self.__specialchar_count += 1

    def validate(self):
        
        """
        Validate the password according to rules:
        - Minimum 10 characters
        - At least one lowercase letter
        - At least one uppercase letter
        - At least one number
        - At least one special character
        - No whitespace
        Returns a list of feedback messages.
        """
        
        messages = []

        if self.__length < 10:
            messages.append("Password requires at least 10 characters.")
            
        if self.__lower_count < 1:
            messages.append("Password requires at least one lowercase letter.")
            
        if self.__upper_count < 1:
            messages.append("Password requires at least one uppercase letter.")
            
        if self.__num_count < 1:
            messages.append("Password requires at least one number.")
            
        if self.__specialchar_count < 1:
            messages.append("Password requires at least one special character.")
            
        if self.__whitespace_count > 0:
            messages.append("Password cannot have any whitespaces.")

        return messages

    def strength(self):
        
        """
        Calculate a simple strength score for the password.
        Returns a string describing the strength.
        """
        
        # Each rule adds 1 to the score if satisfied
        score = sum([
            self.__length >= 10,
            self.__lower_count >= 1,
            self.__upper_count >= 1,
            self.__num_count >= 1,
            self.__specialchar_count >= 1
        ])

        # Determine password strength
        if score == 5:
            return "Password is very strong!"
        elif score >= 3:
            return "Password is moderate."
        else:
            return "Password is too weak!"


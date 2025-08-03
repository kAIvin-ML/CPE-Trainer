import os


# [0] ------------------------- Screen -------------------------
def clear_screen():
    """
    Clears the terminal screen based on the operating system.
    """
    # Windows
    if os.name == 'nt':  
        os.system('cls')
    # Unix-like (Linux, macOS)
    else:
        os.system('clear')

# [1] ------------------------- Separators -------------------------
        
def separator_equalsign_50():
    separator = "=" * 50
    print(separator)

def separator_hyphen_75():
    separator = "-" * 75
    print(separator)
    
    
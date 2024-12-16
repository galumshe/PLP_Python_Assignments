"""
This module contains the main functions for file operations.
It handles reading from and writing to files.
"""

def read_file(filename):
    """
    Reads the content of a file and returns it as a string.
    
    Args:
        filename (str): The name of the file to read
        
    Returns:
        str: The content of the file
        
    Raises:
        FileNotFoundError: If the file doesn't exist
        PermissionError: If the program doesn't have permission to read the file
    """
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"The file '{filename}' was not found.")
    except PermissionError:
        raise PermissionError(f"Permission denied when trying to read '{filename}'.")
    except Exception as e:
        raise Exception(f"An unexpected error occurred while reading the file: {str(e)}")

def write_file(filename, content):
    """
    Writes content to a new file.
    
    Args:
        filename (str): The name of the file to write to
        content (str): The content to write to the file
        
    Raises:
        PermissionError: If the program doesn't have permission to write to the file
    """
    try:
        with open(filename, 'w') as file:
            file.write(content)
    except PermissionError:
        raise PermissionError(f"Permission denied when trying to write to '{filename}'.")
    except Exception as e:
        raise Exception(f"An unexpected error occurred while writing the file: {str(e)}")

def modify_content(content):
    """
    Modifies the content of the file. In this example, it:
    1. Converts the text to uppercase
    2. Adds line numbers to each line
    
    Args:
        content (str): The original content
        
    Returns:
        str: The modified content
    """
    # Split the content into lines
    lines = content.split('\n')
    
    # Process each line: add line number and convert to uppercase
    modified_lines = [f"{i+1}. {line.upper()}" for i, line in enumerate(lines)]
    
    # Join the lines back together
    return '\n'.join(modified_lines)
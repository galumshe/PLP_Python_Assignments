"""
Main program file that handles user interaction and orchestrates the file operations.
"""

from file_operations import read_file, write_file, modify_content

def main():
    """
    Main function that runs the program and handles user interaction.
    """
    # Keep trying until successful or user quits
    while True:
        try:
            # Get input filename from user
            input_filename = input("Enter the name of the file to read (or 'q' to quit): ")
            
            # Check if user wants to quit
            if input_filename.lower() == 'q':
                print("Goodbye!")
                break
            
            # Read the content from the input file
            content = read_file(input_filename)
            
            # Modify the content
            modified_content = modify_content(content)
            
            # Generate output filename by adding '_modified' before the extension
            name_parts = input_filename.rsplit('.', 1)
            output_filename = f"{name_parts[0]}_modified.{name_parts[1]}" if len(name_parts) > 1 else f"{input_filename}_modified"
            
            # Write the modified content to the new file
            write_file(output_filename, modified_content)
            
            print(f"\nSuccess! Modified content has been written to '{output_filename}'")
            print("\nHere's a preview of the modifications:")
            print("-" * 50)
            print(modified_content[:200] + "..." if len(modified_content) > 200 else modified_content)
            print("-" * 50)
            
        except FileNotFoundError as e:
            print(f"\nError: {e}")
            print("Please make sure the file exists and try again.")
            
        except PermissionError as e:
            print(f"\nError: {e}")
            print("Please check file permissions and try again.")
            
        except Exception as e:
            print(f"\nAn unexpected error occurred: {e}")
            print("Please try again or use a different file.")
        
        print()  # Empty line for better readability

if __name__ == "__main__":
    # Print welcome message and instructions
    print("Welcome to the File Modifier Program!")
    print("This program will read a file, modify its contents, and save it to a new file.")
    print("The modifications include:")
    print("1. Converting text to uppercase")
    print("2. Adding line numbers to each line\n")
    
    # Start the main program
    main()
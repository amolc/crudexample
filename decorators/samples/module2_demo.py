import os

def demo_file_operations():
    filename = "sample_data.txt"
    
    # 1. Writing to a file
    print(f"--- Writing to {filename} ---")
    with open(filename, "w") as f:
        f.write("Line 1: Hello Python!\n")
        f.write("Line 2: This is a file handling demo.\n")
        f.write("Line 3: Safely closing using 'with' context manager.\n")

    # 2. Reading the entire file
    print(f"\n--- Reading {filename} ---")
    with open(filename, "r") as f:
        content = f.read()
        print(content)

    # 3. Reading line by line
    print(f"--- Reading {filename} line by line ---")
    with open(filename, "r") as f:
        for i, line in enumerate(f, 1):
            print(f"Line {i}: {line.strip()}")

    # 4. Appending to a file
    print(f"\n--- Appending to {filename} ---")
    with open(filename, "a") as f:
        f.write("Line 4: This line was appended.\n")

    # 5. Exception Handling
    print("\n--- Exception Handling Demo ---")
    try:
        with open("non_existent_file.txt", "r") as f:
            print(f.read())
    except FileNotFoundError:
        print("Caught Error: The file 'non_existent_file.txt' does not exist.")

    # Clean up
    if os.path.exists(filename):
        os.remove(filename)
        print(f"\nCleaned up: {filename} removed.")

if __name__ == "__main__":
    demo_file_operations()

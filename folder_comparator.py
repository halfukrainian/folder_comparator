import os  

def compare_directories(dir1, dir2, output_file):
    if not os.path.exists(dir1):
        print(f"Error: The directory '{dir1}' does not exist.")
        return
    
    if not os.path.exists(dir2):
        print(f"Error: The directory '{dir2}' does not exist.")
        return

    files_dir1 = {os.path.relpath(os.path.join(root, f), dir1) for root, _, files in os.walk(dir1) for f in files}
    files_dir2 = {os.path.relpath(os.path.join(root, f), dir2) for root, _, files in os.walk(dir2) for f in files}

    only_in_dir1 = files_dir1 - files_dir2
    only_in_dir2 = files_dir2 - files_dir1

    with open(output_file, 'w', encoding='utf-8') as f:
        if not only_in_dir1 and not only_in_dir2:
            f.write("The directories are the same. No differences found.\n")
            print("The directories are the same. No differences found.")
        else:
            if only_in_dir1:
                f.write(f"Files only in {dir1}:\n")
                f.write("\n".join(f"  - {file}" for file in only_in_dir1) + "\n")
            
            if only_in_dir2:
                f.write(f"\nFiles only in {dir2}:\n")
                f.write("\n".join(f"  - {file}" for file in only_in_dir2))

    print(f"Comparison completed. Results saved in: {output_file}")

def main():
    dir1 = input("Enter the first directory path: ").strip().strip('"')
    dir2 = input("Enter the second directory path: ").strip().strip('"')

    current_directory = os.getcwd()
    output_file = os.path.join(current_directory, "comparison_results.txt")
    
    print(f"Results will be saved to {output_file}")

    compare_directories(dir1, dir2, output_file)

    input("Press Enter to exit...")

if __name__ == "__main__":
    main()

"""The program shall convert the numbers to binary and hexadecimal base."""

import sys
import os
import time

def convert_numbers(filename):
    """Loads a file from a given filename.

    Args:
        filename: The name to the file to be loaded.
    """

    if not os.path.exists(filename):
        print(f"Error: File '{filename}' not found.")
        return

    try:
        start_time = time.time()  # Getting start time
        # Req 6
        with open(filename, 'r', encoding="utf-8") as file:
            i = 0

            # Print ConvertionResults.txt
            with open("ConvertionResults.txt", "w", encoding="utf-8") as outfile:
                print(f"FILENAME: {filename}")
                outfile.write(f"FILENAME: {filename}\n")

                print("ITEM NUMBER BIN HEX")
                outfile.write("ITEM NUMBER BIN HEX\n")
                for line in file:
                    # Req 3
                    try:
                        i = i + 1
                        num = int(line.strip())
                        # Req 2
                        binary_num = format(num, "08b")
                        hex_num = format(num, "X")
                        print(f"{i} {line} {binary_num} {hex_num}")

                        print(f"{i} {num} {binary_num} {hex_num}")
                        outfile.write(f"{i} {num} {binary_num} {hex_num}\n")
                    except ValueError as e:
                        print(f"Invalid number was found, processing: {line.strip()} - {e}")

                    end_time = time.time()  # Getting end time
                    elapsed_time = end_time - start_time

                print(f"ELAPSED TIME: {elapsed_time:.4f} seconds") # Req 7
                outfile.write(f"ELAPSED TIME: {elapsed_time:.4f} seconds\n") # Req 7

    except Exception as e:
        print(f"Something went wrong while reading the file: {e}")

# Req 1
if __name__ == "__main__":
    # Req 5
    if len(sys.argv) != 2:
        # Req 4
        print("Usage: python convertNumbers.py <filename>")
    else:
        file_arg = sys.argv[1]
        convert_numbers(file_arg)

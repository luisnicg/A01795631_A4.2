"""The program shall convert the numbers to binary and hexadecimal base."""

import sys
import os
import time

def world_count(filename):
    """Loads a file from a given filename.

    Args:
        filename: The name to the file to be loaded.
    """

    if not os.path.exists(filename):
        print(f"Error: File '{filename}' not found.")
        return

    word_counts = {}
    start_time = time.time()  # Getting start time
    # Req 3
    try:
        # Req 6
        with open(filename, 'r', encoding="utf-8") as file:
            # Req 2
            for line in file:
                words = line.lower().split()
                for word in words:
                    word = ''.join(c for c in word if c.isalnum())
                    if word:
                        word_counts[word] = word_counts.get(word, 0) + 1

        sorted_counts = sorted(word_counts.items(), key=lambda item: item[1], reverse=True)

        # Print results to console
        print(f"Row Labels	Count of {filename}:")
        for word, count in sorted_counts:
            print(f"{word}: {count}")

        end_time = time.time()  # Getting end time
        elapsed_time = end_time - start_time
        print(f"ELAPSED TIME: {elapsed_time:.4f} seconds") # Req 7

        # Save results to file
        with open("WordCountResults.txt", "w", encoding="utf-8") as outfile:
            outfile.write(f"Row Labels	Count of {filename}:\n")
            for word, count in sorted_counts:
                outfile.write(f"{word}: {count}\n")
            outfile.write(f"ELAPSED TIME: {elapsed_time:.4f} seconds\n") # Req 7

    except Exception as e:
        print(f"Something went wrong: {e}")

# Req 1
if __name__ == "__main__":
    # Req 5
    if len(sys.argv) != 2:
        # Req 4
        print("Usage: python WordCountResults.py <filename>")
    else:
        file_arg = sys.argv[1]
        world_count(file_arg)

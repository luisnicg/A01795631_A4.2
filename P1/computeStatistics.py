"""The program shall compute all descriptive statistics from a file containing numbers."""

import sys
import os
import time
from collections import Counter

def compute_descriptive_statistics(filename):
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
            numbers = []
            # Req 3
            # Looking for invalid values and fixing them. 
            for line in file:
                try:
                    num = float(line.strip())
                    numbers.append(num)
                except ValueError as e:
                    print(f"Invalid number was found, processing: {line.strip()} - {e}")
                    number_string = ''.join([i for i in line if i.isdigit()])
                    num = float(number_string.strip())
                    numbers.append(num)

            if not numbers:
                print("No valid numbers found in the file")
                return

            # Req 2
            n = len(numbers)
            mean = sum(numbers) / n

            # Calculate the squared differences from the mean
            squared_diffs = [(x - mean)**2 for x in numbers]

            # Calculate the variance using the sum of the squared differences
            variance = sum(squared_diffs)/ n

            # Standard Deviation
            sd = variance ** 0.5

            # Median
            numbers.sort()
            if n % 2 == 0:
                median = (numbers[n // 2 - 1] + numbers[n // 2]) / 2
            else:
                median = numbers[n // 2]

            # Mode
            data = Counter(numbers)
            mode = data.most_common(1)[0][0]

            end_time = time.time()  # Getting end time
            elapsed_time = end_time - start_time

            # Output the Results
            print(f"FILENAME: {filename}")
            print(f"COUNT: {n}")
            print(f"MEAN: {mean}")
            print(f"MEDIAN: {median}")
            print(f"MODE: {mode}")
            print(f"SD: {sd}")
            print(f"VARIANCE: {variance}")
            print(f"ELAPSED TIME: {elapsed_time:.4f} seconds") # Req 7

        # Print StatisticsResults.txt
        with open("StatisticsResults.txt", "w", encoding="utf-8") as outfile:
            outfile.write(f"FILENAME: {filename}\n")
            outfile.write(f"COUNT: {n}\n")
            outfile.write(f"MEAN: {mean}\n")
            outfile.write(f"MEDIAN: {median}\n")
            outfile.write(f"MODE: {mode}\n")
            outfile.write(f"VARIANCE: {variance}\n")
            outfile.write(f"SD: {sd}\n")
            outfile.write(f"ELAPSED TIME: {elapsed_time:.4f} seconds\n") # Req 7

    except ValueError as e:
        print(f"Something went wrong while reading the file: {e}")

# Req1
if __name__ == "__main__":
    # Req 5
    if len(sys.argv) != 2:
        # Req 4
        print("Usage: python computeStatistics.py <filename>")
    else:
        file_arg = sys.argv[1]
        compute_descriptive_statistics(file_arg)

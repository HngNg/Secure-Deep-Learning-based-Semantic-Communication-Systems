import os
import re

# Define the input directory
input_dir = "C:/Users/IBM/Desktop/Bob_snr"

# Initialize an empty list to store PSNR values
PSNR_values = []
PSNR_snr = []
# for snr in range (-5, 21, 5):
for snr in range (20, 21, 5):
    snr_dir = input_dir + str(snr) + "/Bob/test_output"
    # Iterate over all files in the input directory
    for file in os.listdir(snr_dir):
        # Check if the file name contains the term "PSNR"
        if "PSNR" in file:
            # Extract the PSNR value from the file name
            match = re.search(r"PSNR_(.*?)_", file)
            if match:
                PSNR_value = float(match.group(1))
                # Append the PSNR value to the list
                PSNR_values.append(PSNR_value)

    # Calculate the average of the PSNR values
    avg_PSNR = sum(PSNR_values) / len(PSNR_values)
    # print("avg_PSNR: " + avg_PSNR)
    PSNR_snr.append(avg_PSNR)


# Print the average PSNR value
# print("Average PSNR:", str(avg_PSNR))
print("Average PSNR:")
print(PSNR_snr)

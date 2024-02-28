import os
import re

# Define the input directory
input_dir = "C:/Users/IBM/Desktop/Bob_snr"

# Initialize an empty list to store SSIM values
SSIM_values = []
SSIM_snr = []
for snr in range (-5, 21, 5):
# for snr in range (20, 21, 5):
    snr_dir = input_dir + str(snr) + "/Bob/test_output"
    # Iterate over all files in the input directory
    for file in os.listdir(snr_dir):
        # Check if the file name contains the term "SSIM"
        if "SSIM" in file:
            # Extract the SSIM value from the file name
            match = re.search(r"SSIM_tensor\((.*?)\)", file)
            if match:
                SSIM_value = float(match.group(1))
                # Append the SSIM value to the list
                SSIM_values.append(SSIM_value)

    # Calculate the average of the SSIM values
    avg_SSIM = sum(SSIM_values) / len(SSIM_values)
    # print("avg_SSIM: " + avg_SSIM)
    SSIM_snr.append(avg_SSIM)


# Print the average SSIM value
# print("Average SSIM:", str(avg_SSIM))
print("Average SSIM:")
print(SSIM_snr)

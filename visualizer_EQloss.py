import re
import os
import matplotlib.pyplot as plt

# Define the list of folders
root_dir = "C:/Users/IBM/Desktop/"
# folders = ["Bob_snr-5", "Bob_snr0", "Bob_snr5", "Bob_snr10", "Bob_snr15", "Bob_snr20",
#            "Eve_snr-5", "Eve_snr0", "Eve_snr5", "Eve_snr10", "Eve_snr15", "Eve_snr20"]

# folders = ["Bob_snr-5", "Bob_snr0", "Bob_snr5", "Bob_snr10", "Bob_snr15", "Bob_snr20"]
# user = "Bob"
folders = ["Eve_snr-5", "Eve_snr0", "Eve_snr5", "Eve_snr10", "Eve_snr15", "Eve_snr20"]
# user = "Eve"

# Create a dictionary to store the EQ loss values for each folder
eq_loss_values = {}

# Iterate over the folders
for folder in folders:
    # Get the path to the "loss_log.txt" file
    loss_log_path = os.path.join(root_dir+ folder, "loss_log.txt")

    # Read the "loss_log.txt" file
    with open(loss_log_path, "r") as f:
        # Skip the first line
        next(f)

        # Iterate over the remaining lines
        line_cnt = 0
        for line in f:
            if line_cnt == 100: break   
            line_cnt += 1
            # Extract the EQ loss value
            match = re.search(r"EQ: (.*?)\s", line)
            if match:
                eq_loss_value = float(match.group(1))

                # Store the EQ loss value in the dictionary
                if folder not in eq_loss_values:
                    eq_loss_values[folder] = []
                eq_loss_values[folder].append(eq_loss_value)

# Create a plot for each folder
for folder, eq_loss_values in eq_loss_values.items():
    if (folder[7] == '-'):
        plt.plot(eq_loss_values, label="SNR = -5 dB")
        print("SNR = -5 dB")
        print(eq_loss_values)
    elif (len(folder) == 9):
        plt.plot(eq_loss_values, label="SNR = "+folder[7]+folder[8]+" dB")
        print("SNR = "+folder[7]+folder[8]+" dB")
        print(eq_loss_values)
    else:
        plt.plot(eq_loss_values, label="SNR = "+folder[7]+" dB")
        print("SNR = "+folder[7]+" dB")
        print(eq_loss_values)
    


# Add a legend to the plot
plt.legend()

plt.xlabel('Epoch')
plt.ylabel('EQ Loss')
# Set the title of the plot
# plt.title("EQ Loss vs. Epoch (CIFAR10)")
# plt.title("Bob's EQ Loss vs. Epoch (CIFAR10)")
plt.title("Eve's EQ Loss vs. Epoch (CIFAR10)")
# plt.yscale('log')
# plt.yticks([0.1, 1, 10, 100, 1000], ['0.1', '1', '10', '100', '1000'])

# Show the plot
plt.grid(True)
plt.show()
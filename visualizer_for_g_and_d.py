import re
import matplotlib.pyplot as plt

# Function to extract the required values from the logs
def extract_values(log_file):
    with open(log_file, 'r') as file:
        lines = file.readlines()
    
    g_l2_losses = []
    d_real_losses = []
    d_fake_losses = []

    # Regular expression pattern to extract G_L2, D_real, and D_fake values
    pattern = re.compile(r"G_L2:\s([0-9.]+)\s.*D_real:\s([0-9.]+)\sD_fake:\s([0-9.]+)")

    for line in lines:
        match = pattern.search(line)
        if match:
            g_l2_losses.append(float(match.group(1)))
            d_real_losses.append(float(match.group(2)))
            d_fake_losses.append(float(match.group(3)))

    return g_l2_losses, d_real_losses, d_fake_losses

# Function to plot the values
def plot_values(g_l2_losses, d_real_losses, d_fake_losses):
    # Calculate epochs based on the number of lines
    epochs = [i / 6 for i in range(len(g_l2_losses))]

    plt.figure(figsize=(14, 7))

    plt.plot(epochs, g_l2_losses, label='G_L2 Loss', linestyle='--', linewidth = 3)
    plt.plot(epochs, d_real_losses, label='D_real Loss', linestyle='-', linewidth = 3)
    plt.plot(epochs, d_fake_losses, label='D_fake Loss', linestyle='-.', linewidth = 3)
    plt.tick_params(axis='both', which='major', labelsize=20)

    plt.xlabel('Epochs', fontsize=28)
    plt.ylabel('Loss Values', fontsize=28)
    plt.title('Training Losses Over Epochs (G_L2, D_real, D_fake)', fontsize=28)
    plt.legend(fontsize=24)
    plt.show()

# Main function
def main():
    log_file = 'g_d_loss_logs.txt'  # Replace with the path to your log file
    g_l2_losses, d_real_losses, d_fake_losses = extract_values(log_file)
    plot_values(g_l2_losses, d_real_losses, d_fake_losses)

# Execute the main function
if __name__ == "__main__":
    main()

import matplotlib.pyplot as plt
import csv

# Path to your CSV file
cifar_csv = ['Bob/', 'Eve/'] 

plt.figure(figsize=(10, 6))
color_cnt = 0
snr_vals = [-5, 10]

for file_name in cifar_csv:
    # for snr in snr_vals:
    for snr in range (-5, 21, 5):
        epochs = []
        train_acc_densenet = []
        file_name_snr = file_name + str(snr) + "checkpoints/JSCC_OFDM/checkpointloss_log.txt"
        print("Processing file:", file_name_snr)
        with open(file_name_snr, 'r') as file:
            csv_reader = csv.reader(file)
            cnt = 0
            for row in csv_reader:
                epoch_num = cnt
                cnt += 1
                epochs.append(epoch_num)
                train_accuracy__ = float(row[0])/100.0
                train_acc_densenet.append(train_accuracy__)

        label_prefix = 'Eve' if 'Eve' in file_name else 'Bob'
        print (len(train_acc_densenet))
        plt.plot(epochs, train_acc_densenet, label=f'{label_prefix} - Accuracy, SNR {snr}', marker='.')
    eve+=1
# Add labels and a legend
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.title('Model Accuracy Over Epochs - CIFAR10')
plt.legend()

# Display the plot
plt.grid(True)
plt.show()

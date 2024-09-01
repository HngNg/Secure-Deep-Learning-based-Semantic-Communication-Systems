import matplotlib.pyplot as plt
import csv

# Path to your CSV file
users = ['Bob', 'Eve'] 

plt.figure(figsize=(10, 6))
color_cnt = 0
# snr_val_bpg = [5, 10, 15, 20]
snr_val = [-5, 0, 5, 10, 15, 20]
ssim_bob = [0.49695316, 0.68870187, 0.82166916, 0.9023301, 0.9463163, 0.96479434]
ssim_eve = [0.13119702, 0.13120452, 0.13119625, 0.13121043, 0.13118857, 0.13121313]
ssim_bob_wo_gan = [0.44262294, 0.59016393, 0.71093, 0.80444964, 0.8864168618266978, 0.92505854]
# ssim_bpg_cr1 = [0.5878220140515222, 0.7505854800936766, 0.8302107728337235, 0.8735362997658078]
ssim_jpeg_ldpc_16qam = [0.0180, 0.0183, 0.0184, 0.4616, 0.4621, 0.4624]
ssim_jpeg_ldpc_64qam = [0.0189, 0.0191, 0.0190, 0.0196, 0.1232, 0.4498]

p = 80093676

plt.plot(snr_val, ssim_bob, label=f'Secure Deep JSCC Bob with CycleGAN', marker='o', linewidth=3, markersize=10)
plt.plot(snr_val, ssim_bob_wo_gan, label=f'Secure Deep JSCC Bob without CycleGAN', marker='h', linewidth=3, markersize=10)
# plt.plot(snr_val, ssim_bob, label=f'Secure Deep JSCC Bob without GAN', marker='o', linewidth=3)
plt.plot(snr_val, ssim_eve, label=f'Secure Deep JSCC Eve', marker='s', linewidth=3, markersize=10)
# plt.plot(snr_val_bpg, ssim_bpg_nc, label=f'BPG+LDPC+QAM (no clipping)', marker='.')
plt.plot(snr_val, ssim_jpeg_ldpc_16qam, label=f'JPEG+LDPC+16QAM', marker='^', linewidth=3, markersize=10)
plt.plot(snr_val, ssim_jpeg_ldpc_64qam, label=f'JPEG+LDPC+64QAM', marker='D', linewidth=3, markersize=10)
plt.tick_params(axis='both', which='major', labelsize=18)

# Add labels and a legend
plt.xlabel('SNR/dB')
plt.ylabel('SSIM')
plt.title('SSIM', weight = 'bold')
plt.legend()

# Set font sizes
plt.xlabel('SNR/dB', fontsize=22)
plt.ylabel('SSIM', fontsize=22)
plt.title('SSIM', fontsize=22)

# Add legend with larger font size
plt.legend(fontsize=16)

# Display the plot
plt.grid(True)
plt.show()
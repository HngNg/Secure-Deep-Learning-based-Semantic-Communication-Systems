import matplotlib.pyplot as plt
import csv

# Path to your CSV file
users = ['Bob', 'Eve'] 

plt.figure(figsize=(10, 6))
color_cnt = 0
snr_val = [-5, 0, 5, 10, 15, 20]
# snr_val_bpg = [5, 10, 15, 20]
psnr_bob = [18.917090100318266, 21.592948316986543, 24.34097173501443, 27.15626081062057, 29.98877216371984, 32.04016945632867]
psnr_bpg_wo_gan = [15.5407166, 17.69771986, 21.114332247557, 24.75276872964169, 27.3094462, 29.74267100]
psnr_eve = [12.657664503083858, 12.657593148160842, 12.65757806712423, 12.657854863576278, 12.657470164761788, 12.657537826888827]
# psnr_bpg_nc = [20.814332247557, 24.690553745928334, 27.85016286644951, 30.358306188925077]
psnr_jpeg_ldpc_16qam = [9.85, 9.85, 9.87, 18.63, 18.67, 18.71]
psnr_jpeg_ldpc_64qam = [9.87, 9.91, 9.79, 9.82, 11.58, 18.64]

plt.plot(snr_val, psnr_bob, label=f'Secure Deep JSCC with CycleGAN', marker='o', linewidth=3, markersize=10)
plt.plot(snr_val, psnr_bpg_wo_gan, label=f'Secure Deep JSCC without CycleGAN', marker='h', linewidth=3, markersize=10)
plt.plot(snr_val, psnr_eve, label=f'Secure Deep JSCC Eve', marker='s', linewidth=3, markersize=10)
plt.plot(snr_val, psnr_jpeg_ldpc_16qam, label=f'JPEG+LDPC+16QAM', marker='^', linewidth=3, markersize=10)
plt.plot(snr_val, psnr_jpeg_ldpc_64qam, label=f'JPEG+LDPC+64QAM', marker='D', linewidth=3, markersize=10)
plt.tick_params(axis='both', which='major', labelsize=18)

# Add labels and a legend
plt.xlabel('SNR/dB', fontsize=22)
plt.ylabel('PSNR(dB)', fontsize=22)
plt.title('PSNR', fontsize=22)

# Add legend with larger font size
plt.legend(fontsize=18)

# Display the plot
plt.grid(True)
plt.show()

import matplotlib.pyplot as plt
temp = [1, 3, 55, 2, 7, 12, 66, 35]

fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(temp, c='red')

plt.title('Title', fontsize=24)
plt.xlabel('', fontsize=16)
plt.ylabel('Tempr', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
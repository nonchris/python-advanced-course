import matplotlib.pyplot as plt
import numpy as np

# Sample data
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
temperature = [10, 15, 23, 25, 20]
rainfall = [50, 30, 80, 20, 10]
humidity = [40, 25, 60, 15, 5]

# Create a figure and axes
ax1: plt.Axes
fig, ax1 = plt.subplots()
ax1.set_xlabel("Months")

# Plot rainfall using a bar plot on the left y-axis
x_steps = np.arange(len(months))
ax1.bar(x_steps, rainfall, color='blue', width=0.3, alpha=0.7, label='Rainfall')
ax1.text(2.5, 45,
         "btw.: we can place text\n"
            "at random locations!", rotation="vertical", color="red")

# set the locations with x-steps but the labels with second array of same len
ax1.set_xticks(x_steps, months)
ax1.set_ylabel('Rainfall (mm)', color='blue')
ax1.tick_params(axis='y', labelcolor='blue')

# Create a twin Axes sharing the xaxis
ax2 = ax1.twinx()

# Plot temperature on the right y-axis
ax2.plot(months, temperature, color='orange', label='Temperature')
ax2.set_xlabel('Month')
ax2.set_ylabel('Temperature (°C)', color='orange')
ax2.tick_params(axis='y', labelcolor='orange')


# Combine legends from both axes
lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax2.legend(lines + lines2, labels + labels2, loc='upper left')

# Title and show the plot
plt.title('Temperature and Rainfall Plot\n'
          '...with totally realistic data')
plt.show()

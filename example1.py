import matplotlib.pyplot as plt

# Sample data
x = [0, 1, 2, 3, 4, 5]
y = [0, 1, 4, 9, 16, 25]

# Create a figure and axis
fig, ax = plt.subplots()

# Plot data
ax.plot(x, y)

# Move the y-axis labels to the right side
ax.yaxis.tick_right()
ax.yaxis.set_label_position("right")
ax.patch.set_facecolor('black')

# Customize the color of the axes
ax.spines['bottom'].set_color('blue')
ax.spines['top'].set_color('red')
ax.spines['left'].set_color('green')
ax.spines['right'].set_color('purple')

# Customize the ticks color
ax.tick_params(axis='x', colors='blue')
ax.tick_params(axis='y', colors='purple')

# Customize the label color
ax.xaxis.label.set_color('blue')
ax.yaxis.label.set_color('purple')

# Add labels and title
ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')
ax.set_title('Customized Matplotlib Graph')

# Show the plot
plt.show()

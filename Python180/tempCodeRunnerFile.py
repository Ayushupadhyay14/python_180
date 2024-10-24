import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Ellipse, Polygon

# Create a figure and axis
fig, ax = plt.subplots()

# Define face circle
face = Circle((0.5, 0.5), 0.4, color='yellow', ec='black')
ax.add_patch(face)

# Define eyes
eye_left = Ellipse((0.35, 0.65), 0.1, 0.2, angle=30, color='white', ec='black')
eye_right = Ellipse((0.65, 0.65), 0.1, 0.2, angle=150, color='white', ec='black')
ax.add_patch(eye_left)
ax.add_patch(eye_right)

# Define eyebrows
eyebrow_left = Polygon([[0.3, 0.8], [0.4, 0.75], [0.5, 0.85]], closed=True, color='black')
eyebrow_right = Polygon([[0.6, 0.85], [0.7, 0.75], [0.8, 0.8]], closed=True, color='black')
ax.add_patch(eyebrow_left)
ax.add_patch(eyebrow_right)

# Define mouth
mouth = Ellipse((0.5, 0.3), 0.4, 0.2, angle=0, color='red', ec='black')
ax.add_patch(mouth)

# Set aspect of the plot to equal
ax.set_aspect('equal')

# Turn off axes
ax.axis('off')

# Title
plt.title('Sahi Hai', fontsize=14, fontweight='bold')
#plt.title("Subhah subhah Thik Hai")

# Print
plt.show()

print("Dimag kharab mat karna!")  # "Don't stress your brain!"

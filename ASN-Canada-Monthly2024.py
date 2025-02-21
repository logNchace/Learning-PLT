import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from PIL import Image

# Data
months = ['January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December']
accidents = [20, 28, 19, 20, 30, 34, 36, 35, 26, 19, 21, 15]

# Create a gradient colormap (light blue to dark blue)
cmap = LinearSegmentedColormap.from_list('gradient', ['#00008B', '#00008B'])

# Create the bubble plot
fig, ax = plt.subplots(figsize=(12, 6))  # Adjusted figure size for better layout

# Create a scatter plot with bubbles on a single line
x = range(len(months))  # X positions for the bubbles (0 to 11)
y = [0.0] * (len(months))  # Y positions (move bubbles up by 0.2 units)
sizes = [a * 100 for a in accidents]  # Bubble sizes proportional to accidents
colors = np.linspace(0, 1, len(months))  # Gradient colors for bubbles

scatter = ax.scatter(x, y, s=sizes, c=colors, cmap=cmap, edgecolor='black', alpha=0.8, )

# Add month labels below the bubbles (adjust y value to move labels)
for i, month in enumerate(months):
    ax.text(i, -0.1, month, ha='center', va='top', fontsize=10, fontweight='bold', color='black')

# Add numbers inside the bubbles (adjust y value to move numbers)
for i, accident in enumerate(accidents):
    ax.text(i, 0, f'{accident}', ha='center', va='center', fontsize=12, fontweight='bold', color='white')

# Add title and subtitle
ax.set_title('An Exclusive Service of Flight Safety Foundation', fontsize=12, pad=15)
ax.text(0.5, 1.1, 'Aviation Safety Network',
        ha='center', va='center', transform=ax.transAxes, fontsize=20, fontweight='bold', color='gray')

# Add text annotations (adjust y values to move annotations)
annotation_text_1 = "- Monthly Aircraft Accident Statistics in CANADA (2024) - "
ax.text(0.5, 0.91, annotation_text_1, ha='center', va='center', transform=ax.transAxes,
        fontsize=14, color='black', fontweight='bold', bbox=dict(facecolor='white', alpha=0.8, edgecolor='none'))

annotation_text_2 = "source: https://asn.flightsafety.org/asndb/year/2024/1/C"
ax.text(0.5, 0.85, annotation_text_2, ha='center', va='center', transform=ax.transAxes,
        fontsize=10, color='blue', bbox=dict(facecolor='white', alpha=0.8, edgecolor='none'))

annotation_text_3 = " 303 occurrences including 40 fatalities  "
ax.text(0.5, 0.75, annotation_text_3, ha='center', va='center', transform=ax.transAxes,
        fontsize=12, color='black', fontweight='bold', bbox=dict(facecolor='white', alpha=0.8, edgecolor='none'))

# Add watermark image (adjust x, y, zoom, and alpha to tweak position and transparency)
watermark_img = Image.open('plane.jpg')  # Make sure 'plane.png' is in the same directory
watermark_img = watermark_img.resize((3000, 3000))  # Resize the image
imagebox = OffsetImage(watermark_img, zoom=0.5, alpha=0.05)  # Adjust zoom and alpha for size and transparency
ab = AnnotationBbox(imagebox, (0.5, 0.5), frameon=False, boxcoords="axes fraction")
ax.add_artist(ab)

# Customize the chart
ax.set_xlim(-0.5, len(months) - 0.5)  # Adjust x-axis limits to fit bubbles
ax.set_ylim(-0.5, 0.5)  # Keep y-axis tight around the bubbles
ax.axis('off')  # Hide the axes for a clean look

# Show the chart
plt.tight_layout()
plt.show()

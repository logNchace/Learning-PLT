import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

# Data
cities = [
    "Toronto, ON", "Montreal, QC", "Calgary, AB", "Edmonton, AB", "Ottawa, ON",
    "Winnipeg, MB", "Mississauga, ON", "Vancouver, BC", "Brampton, ON",
    "Quebec City, QC", "Hamilton, ON", "Halifax, NS", "Laval, QC", "Surrey, BC",
    "Etobicoke, ON", "London, ON", "Markham, ON", "Vaughan, ON",
    "Oakville, ON", "Victoria, BC", "Windsor, ON", "Kitchener, ON", "Gatineau, QC",
    "Longueuil, QC", "Burnaby, BC"
]

populations = [
    2600000, 1762949, 1019942, 1010899, 812129, 749607, 668549, 600000,
    593638, 531902, 519949, 439819, 422993, 394976, 365000, 346765, 328696,
    306233, 297601, 289625, 278013, 256885, 242124, 229330, 202799
]

# Plotting
plt.figure(figsize=(15, 10))  # Adjust the figure size as needed
x = range(len(cities))

# Add line connecting all markers
plt.plot(x, populations, color='#252525', linestyle='--', linewidth=0.5, alpha=0.6, zorder=1,)

# Plot the markers
plt.scatter(x, populations, color='blue', s=50, zorder=2, marker='D', edgecolor='black', linewidths=0.5)

# Adding vertical lines (behind the markers)
for i, pop in enumerate(populations):
    plt.vlines(x[i], 0, pop,color='#252525', zorder=0,  linestyle='--', linewidth=0.8, alpha=0.5)


plt.title("Largest Cities in Canada", pad=30,weight='bold',fontsize=18)
plt.ylabel("Population", labelpad=30, weight='bold', fontsize=12)

# Add value labels with space between marker and label
for i, j in enumerate(populations):
    plt.text(x[i], j + 50000, f'{j:,d}', ha='left', va='bottom', rotation=35, fontsize=8, )

plt.xticks(x, cities, rotation=45, ha='right', fontweight='bold', fontsize=8)
plt.yticks(rotation=45, fontsize=10)

# Adding gridlines for Y-axis
plt.grid(axis='y', linestyle='--', alpha=0.3, color='#d3d3d3')
plt.grid(axis='x', linestyle='--', alpha=0.3, color='#d3d3d3')

# Adjust spines
ax = plt.gca()


plt.text(0.63, 0.91,
         'Population Density',
         alpha=0.8,
         fontsize=10,
         weight='bold',   # Make text bold
         rotation=0,
         ha='left',       # Align text to the left
         va='top',        # Align text to the top
         transform=plt.gca().transAxes  # Use Axes coordinates
         )

plt.text(0.63, 0.87,
         'The 2024 population density in Canada is 4 people per Km2 (11 people per mi2),\ncalculated on a total land area of 9,093,510 Km2 (3,511,022 sq. miles).',
         alpha=0.8,
         fontsize=8,
         rotation=0,
         ha='left',   # Align text to the left
         va='top',    # Align text to the top
         transform=plt.gca().transAxes  # Use Axes coordinates
         )



ax.get_yaxis().set_major_formatter(mticker.StrMethodFormatter('{x:,.0f}'))

ax.spines['top'].set_visible(False)   # Hide the top spine
ax.spines['right'].set_visible(False)  # Hide the right spine
ax.spines['bottom'].set_alpha(0.3) # Bottom spine
ax.spines['left'].set_alpha(0.3)   # Left spine

plt.axhline(y=0, color='#505050', linewidth=2)


# Adjust axis limits to remove gap on x-axis
plt.ylim(0, max(populations) + 100000)
plt.xlim(-0.5, len(cities) - 0.5)

plt.show()

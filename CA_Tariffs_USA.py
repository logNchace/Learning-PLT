import matplotlib.pyplot as plt
import numpy as np
import matplotlib.image as mpimg

# Data
categories = {
    'Dairy Products': {
        'Butter': 298,
        'Milk': 270,
        'Cheese': 245
    },
    'Ind. Goods': {
        'Copper': 48,
        'Aluminum': 45,
        'Steel': 25
    },
    'Cons. Goods': {
        'Eggs': 163,
        'Wheat': 94,
        'Cars': 45,
        'TVs': 45,
        'Bovine/Meat': 26.5
    },
    'Other Agri. Prod.': {
        'Chicken': 238,
        'Sausages': 69.9,
        'Barley seed': 57.8
    }
}

# Flatten and group data by category
labels = []
values = []
category_labels = []  # To store category labels and their positions
current_position = 0

for category, items in categories.items():
    # Sort items within each category by value (descending order)
    sorted_items = sorted(items.items(), key=lambda x: x[1], reverse=False)
    for item, value in sorted_items:
        labels.append(item)  # Only include the item name
        values.append(value)
    # Record the position for the category label
    category_labels.append((category, current_position + len(sorted_items) / 2 - 0.5))
    current_position += len(sorted_items)

# Define gradient colors for each category
colors = {
    'Dairy Products': list(plt.cm.Blues(np.linspace(0.4, 1, len(categories['Dairy Products'])))),
    'Ind. Goods': list(plt.cm.Greens(np.linspace(0.4, 1, len(categories['Ind. Goods'])))),
    'Cons. Goods': list(plt.cm.Oranges(np.linspace(0.4, 1, len(categories['Cons. Goods'])))),
    'Other Agri. Prod.': list(plt.cm.Purples(np.linspace(0.4, 1, len(categories['Other Agri. Prod.']))))
}

# Assign colors to each bar
bar_colors = []
current_category_index = 0
for i, label in enumerate(labels):
    category = list(categories.keys())[current_category_index]
    bar_colors.append(colors[category].pop(0))
    if i + 1 == sum(len(items) for _, items in list(categories.items())[:current_category_index + 1]):
        current_category_index += 1

# Plotting
plt.figure(figsize=(10, 8))
bars = plt.barh(range(len(labels)), values, color=bar_colors)
plt.xlabel('Percentage (%)', fontsize=12, fontweight="bold", labelpad=20)
plt.title('Canada\'s Tariffs on the USA', fontweight="bold", pad=25)

# Set X/Y-axis ticks and labels
plt.yticks(range(len(labels)), labels,
            fontsize=9,
            #fontname='Arial',
            #fontweight="bold"
            )
plt.xticks(
            fontsize=9,
            #fontname='Arial',
            #fontweight="bold"
            )

# Add vertical category labels
for category, pos in category_labels:
    plt.text(-25, pos, category, rotation=90, va='center', ha='right', fontsize=11, fontweight="bold",  color='black')

# Add actual numbers at the end of each bar
for i, (value, bar) in enumerate(zip(values, bars)):
    plt.text(bar.get_width() + 2, bar.get_y() + bar.get_height() / 2, f'{value}%', va='center', ha='left', fontsize=9, fontweight="bold",)


plt.text(
    0.95, 0.55,  # Position (95% from the left, 2% from the bottom)
    "These figures have been circulating widely,\nit’s highly recommended to visit the official Tariff Finder website at\n\nhttps://www.tariffinder.ca/en/getStarted. ",
    fontsize=9, color='black', alpha=0.8, ha='right', transform=plt.gca().transAxes
)

plt.grid(axis="x", linestyle="--", alpha=0.2)

for spine in plt.gca().spines.values():
    spine.set_color('black')
    spine.set_linewidth(1)
    spine.set_linestyle(':')

plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['bottom'].set_visible(True)
plt.gca().spines['left'].set_visible(True)


#plt.gca().set_facecolor('lightyellow')
#plt.gcf().set_facecolor('lightyellow')

plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

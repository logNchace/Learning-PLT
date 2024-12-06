import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
from matplotlib.ticker import FuncFormatter

annee = list(range(1995, 2025))  # Years from 1995 to 2023
deces = [52722, 52278, 54281, 54306, 54959, 53287, 54372, 55748, 54972, 55614, 55988, 54434,
         56748, 57149, 58043, 58841, 59539, 61007, 61315, 63244, 64185, 63589, 66092, 68811,
         67617, 74849, 70151, 78400, 77550, 65500]

# Plotting
plt.figure(figsize=(12, 6))  # Set figure size for better readability
plt.plot(annee, deces,
         label='Nombre de Décès',
         color='black',
         alpha=0.3,
         linewidth=0.8,
         linestyle='--',
         #marker='8',
         #markerfacecolor='red',
         #markersize=8,
         #markeredgewidth=0.5,  # Border width
         #markeredgecolor='black',  # Border color
         )  # x-axis: annee, y-axis: deces

plt.scatter(annee, deces,
            color='red',
            marker='h',
            s=66,  # Marker size
            edgecolor='black',  # Marker border color
            linewidths=0.5,
            zorder=2
            )  # On top of the line


# Annotate data points with their Y-values (number of deaths)
for x, y in zip(annee, deces):
    plt.annotate(f'{y}', (x, y),
            textcoords="offset points",  # Position relative to the point
            xytext=(0, 8),  # Offset by 5 points upwards
            ha='center',  # Center-align text
            fontsize=8,  # Adjust font size
            color='black',
            weight = 'bold'
                 )

# Customize x-axis to display all years
plt.xticks(annee, rotation=45, fontsize=10)  # Use `annee` for xticks to ensure all years are displayed
plt.yticks( rotation=45,fontsize=10)

# Title and Labels


plt.title('Décès annuels (1995–2024) - Québec',
          #y=0.99,  # Adjust this to move the suptitle closer to the top
          ha='center',
          va='center',
          fontsize=14,
          color='black',
          weight='bold',
          pad=30
          )

#plt.title("Comptabilisation des décès en 2024, de janvier à octobre",
#          fontsize=10,
#          ha='center',  # Center-align horizontally
#          va='center',  # Align vertically to the center of the plot
#         color='black',
#          weight='bold',
#          pad=35  # Adjust this to move the title closer to the suptitle
#          )


plt.xlabel("Années",
           labelpad=15,
           fontdict={'fontname': 'Arial'},
           fontsize=14,
           color='black',
           weight='bold'
           )

plt.ylabel("Décès",
           labelpad=15,
           fontdict={'fontname': 'Arial'},
           fontsize=14,
           color='black',
           weight='bold'
           )

# Add minor ticks and gridlines on Y-axis
ax = plt.gca()
ax.yaxis.set_minor_locator(MultipleLocator(1000))  # Set minor tick interval
plt.grid(True, which='both', axis='y', linestyle='--', alpha=0.3)  # Add gridlines for both major and minor ticks
ax.yaxis.set_major_formatter(FuncFormatter(lambda x, _: f'{x:,.0f}'))


# Add a footer text

plt.text(1, 0.15, 'Comptabilisation des décès en 2024, de janvier à octobre',
         alpha=1,
         fontsize=8,
         weight='bold',
         rotation=0,
         ha='right',
         va='bottom',
         transform=plt.gca().transAxes
         )

plt.text(1, 0.05, 'Mise à jour: 5 Décembre 2024\n Prochaine mise à jour: 16 janvier 2025 '
                  '\n\nhttps://statistique.quebec.ca/fr/produit/tableau/698#tri_phe=3528',
         alpha=0.8,
         fontsize=8,
         #weight='bold',
         rotation=0,
         ha='right',
         va='bottom',
         transform=plt.gca().transAxes
         )

# Add a legend and grid
plt.grid(True, linestyle='--', alpha=0.3)

ax = plt.gca()
# graph border - spines
ax.spines['top'].set_visible(False)   # Hide the top spine
ax.spines['right'].set_visible(False)  # Hide the right spine
ax.spines['bottom'].set_alpha(0.3) # Bottom spine
ax.spines['left'].set_alpha(0.3)   # Left spine



# Display the plot
plt.show()

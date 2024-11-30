import matplotlib.pyplot as plt
import numpy as np
from matplotlib.font_manager import weight_dict
from matplotlib.ticker import MultipleLocator, AutoMinorLocator

"https://color-hex.org/"
"https://statistique.quebec.ca/fr/produit/tableau/esperance-de-vie-a-la-naissance-selon-le-sexe-par-region-administrative-quebec#tri_sexe=44591"

# X data = Moyenne d'age
x = [77.8, 78.1, 78.2, 78.6, 78.9, 79.2, 79.4, 79.6, 79.9, 80.2, 80.5, 80.7, 80.9, 81.2, 81.5, 81.6, 81.8, 81.9, 82.1,
     82.3, 82.4, 82.5, 82.6, 82.5, 82.6, 82.4, 82.5]

xf = [81.0, 81.1, 81.2, 81.5, 81.7, 81.9, 82.0, 82.1, 82.4, 82.6, 82.8, 83.0, 83.1, 83.3, 83.5, 83.7, 83.8, 83.8, 83.9,
     84.1, 84.2, 84.3, 84.4, 84.3, 84.5, 84.3, 84.4]

xh = [74.6, 74.9, 75.0, 75.4, 75.8, 76.2, 76.6, 76.9, 77.3, 77.7, 78.0, 78.3, 78.6, 78.9, 79.2, 79.4, 79.7, 79.9, 80.1,
      80.3, 80.5, 80.6, 80.7, 80.6, 80.7, 80.5, 80.6]

# Y  Annees
y = list(range(1997, 2024))
year_range = range(1997, 2024)  # From 1997 to 2023 (inclusive)
plt.yticks(year_range)

# Sexes réunis
plt.plot(x, y,
        label='Sexes réunis',
        color='black',
        linewidth='0.2',
        marker='8',
        markerfacecolor='#000000',
        markersize= '6',
        markeredgewidth = 0.5,  # border width
        markeredgecolor = 'white',  # border color
         )
# Femmes - color : https://color-hex.org/color/bf1077
plt.plot(xf, y,
        label='Femmes',
        color='#bf1077',
        linewidth='0.2',
        marker='8',
        markerfacecolor='#bf1077',
        markersize= '6',
        markeredgewidth = 0.5,  # border width
        markeredgecolor = 'black',  # border color
         )

# Hommes - color : https://color-hex.org/color/0052ff
plt.plot(xh, y,
        label='Hommes',
        color='#0052ff',
        linewidth='0.2',
        marker='8',
        markerfacecolor='#0052ff',
        markersize= '6',
        markeredgewidth = 0.5,  # border width
        markeredgecolor = 'black',  # border color
         )


# Markers Enhancement

offset = 0.5  # Vertical offset for annotations

# Sexes réunis
for i in range(len(x)):
    # Add annotation
    plt.text(x[i], y[i] + offset,
             f'({x[i]}, {y[i]})',
             fontsize=6, ha='center', va='bottom',
             color='black')

    # Add vertical line
    plt.vlines(x[i], ymin=y[i], ymax=y[i] + offset,
             colors='black',
             linestyles='solid',
             linewidth=1)
# Femmes
for i in range(len(xf)):
    # Add annotation
    plt.text(xf[i], y[i] + offset,
             f'({xf[i]}, {y[i]})',
             fontsize=6, ha='center', va='bottom',
             color='black')

    # Add vertical line
    plt.vlines(xf[i], ymin=y[i], ymax=y[i] + offset,
             colors='#bf1077',
             linestyles='solid',
             linewidth=1)

# Hommes
for i in range(len(xh)):
    # Add annotation
    plt.text(xh[i], y[i] + offset,
             f'({xh[i]}, {y[i]})',
             fontsize=6, ha='center', va='bottom',
             color='black')

    # Add vertical line
    plt.vlines(xh[i], ymin=y[i], ymax=y[i] + offset,
             colors='#0052ff',
             linestyles='solid',
             linewidth=1)


### Graph enhancement
plt.suptitle ('Espérance de vie à la naissance - (1997 à 2023) \n Régions administratives du Québec', y=0.99, fontsize= 14, color= 'black', weight='bold',)
plt.title('\n Abitibi-Témiscamingue, Bas-Saint-Laurent, Capitale-Nationale, Centre-du-Québec, Chaudière-Appalaches, Côte-Nord, Estrie, \n Gaspésie–Îles-de-la-Madeleine, Lanaudière, Laurentides, Laval, Mauricie, Montérégie, Montréal, Nord-du-Québec, Outaouais, Saguenay–Lac-Saint-Jean',
            fontsize=8,
            ha='center',
            color='#00243d',
            pad=20
          )
plt.xlabel(
    'Âges (Moyenne)',
            labelpad=15,
            fontdict={'fontname': 'Arial'},
            fontsize= 14,
            color='black',
            weight='bold'
            )

plt.ylabel(
    'Années',
            labelpad=18,
            fontdict={'fontname': 'Arial'},
            fontsize= 14,
            color='black',
            weight='bold'
            )

#watermark
plt.text(1, 0.05, ' Mise à jour : 22 mai 2024 \n https://statistique.quebec.ca/fr/produit/tableau/799',
            alpha=0.8,
            fontsize=9,
            weight='bold',
            rotation=00,
            ha='right',
            va='bottom',
            transform=plt.gca().transAxes
            )

# Add a legend with custom frame colors and transparency
legend = plt.legend(
            loc='upper left',
            shadow=True,
            edgecolor='#f3f3f3',
            frameon=True,
            framealpha=1,
            fancybox=True,
            labelspacing=0.9,
            )

# Customize the face color of the legend (background)
legend.get_frame().set_facecolor('white')

# Enable major and minor grids for x-axis only
plt.grid(axis='x', which='major', color='#00243d', linewidth=0.1, alpha=0.3, linestyle='--')
plt.grid(axis='x', which='minor', color='#007acc', linewidth=0.1, alpha=0.3, linestyle='--')

ax = plt.gca()

# Set major ticks every 0.3 units
ax.xaxis.set_major_locator(MultipleLocator(0.3))
# Set minor ticks every 0.1 units
ax.xaxis.set_minor_locator(MultipleLocator(0.1))
# Format x-axis to show 1 decimal place
ax.xaxis.set_major_formatter(plt.FormatStrFormatter('%.1f'))

ax.xaxis.grid(True)
ax.yaxis.grid(False)

# graph border - spines
ax.spines['top'].set_visible(False)   # Hide the top spine
ax.spines['right'].set_visible(False)  # Hide the left spine




plt.show()






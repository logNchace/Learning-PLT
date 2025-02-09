import matplotlib.pyplot as plt
import pandas as pd
import io
import seaborn as sns

# Your data (as a string)
data = """Region                             Subventions
Abitibi-Témiscamingue                            $1,798,410.00
Bas-Saint-Laurent                                 $3,708,660.00
Capitale-Nationale                              $278,119,234.92
Centre-du-Québec                                 $1,128,800.00
Chaudière-Appalaches                             $3,344,727.00
Côte-Nord                                          $798,060.00
Estrie                                            $1,329,190.00
Gaspésie - Îles-de-la-Madeleine                 $2,188,900.00
Lanaudière                                       $1,502,554.00
Laurentides                                       $3,153,463.00
Laval                                               $380,250.00
Mauricie                                          $2,143,940.00
Montérégie                                      $4,358,580.00
Montréal                                       $346,414,081.65
Nord-du-Québec                                   $2,004,390.00
Outaouais                                        $12,978,620.00
Saguenay - Lac-Saint-Jean                         $1,051,800.00"""

# Read the data
df = pd.read_csv(io.StringIO(data), sep=r'\s\s+', engine='python', skipinitialspace=True)

# Data Cleaning
df['Subventions'] = df['Subventions'].replace({r'\$': '', ',': ''}, regex=True).astype(float)

# Sort by Subventions (descending)
df_sorted = df.sort_values('Subventions', ascending=False)

# Define color gradient
colors = sns.color_palette("Blues_r", len(df_sorted))

# Create the horizontal bar chart
plt.figure(figsize=(12, 8))
bars = plt.barh(df_sorted['Region'], df_sorted['Subventions'], color=colors)

# Add data labels with connecting lines
for i, v in enumerate(df_sorted['Subventions']):
    plt.hlines(y=i, xmin=v, xmax=v + (v * 0.05), color='gray', linewidth=1.5)  # Small line
    plt.text(v + (v * 0.06), i, f"${v:,.2f}", va='center', fontsize=10)

# Customize the chart
plt.title("Subventions versées par le ministère de la Culture et des Communications \n Avril 2024 à Septembre 2024", fontweight="bold")
plt.xlabel("Montant annoncé ($)", fontsize=11, fontweight="bold", labelpad=20)
plt.ylabel("Region administrative", fontsize=11,fontweight="bold", labelpad=20)
plt.gca().invert_yaxis()  # Invert y-axis to have highest at top
plt.xscale("log")  # Log scale for better visualization
plt.xticks([1e5, 1e6, 1e7, 1e8], ["100K", "1M", "10M", "100M"])  # Custom labels

plt.text(
    0.95, 0.10,  # Position (95% from the left, 2% from the bottom)
    "Total des subventions versées pour 2024: $666,403,660.57",
    fontsize=12, color='black', alpha=0.8, ha='right', transform=plt.gca().transAxes
)

plt.grid(axis="x", linestyle="--", alpha=0.3)

plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['bottom'].set_visible(True)
plt.gca().spines['left'].set_visible(True)

plt.xticks(rotation=45)
plt.yticks(rotation=45)

plt.tight_layout()
plt.show()

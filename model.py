import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from bokeh.plotting import figure, show, output_notebook
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure, output_notebook, show
from bokeh.models import ColumnDataSource
import seaborn as sn
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource, HoverTool
from bokeh.palettes import Spectral3
import pandas as pd
DATA = pd.read_csv("/home/petitjean/MITIenvHP/DATA_neuronal_dataset-essaisoutlier01 (2).csv")
# visualisation du dataset avec bokeh
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource, HoverTool
from bokeh.palettes import Viridis3
from bokeh.io import output_notebook
import pandas as pd
import numpy as np

# Afficher les graphiques Bokeh dans le notebook Jupyter
output_notebook()

# --- ÉTAPE 1 : Traitement des données brutes depuis le dataframe DATA ---
# Création de la liste des noms de colonnes des neurones
neurone_cols = [f"neurone{str(i).zfill(2)}" for i in range(1, 101)]
time_vector = DATA["temps-ms"].values
total_time = time_vector[-1]

# Définition des fenêtres temporelles pour le calcul de densité de décharge
bin_size_ms = 100
time_bins = np.arange(0, total_time + bin_size_ms, bin_size_ms)
num_bins = len(time_bins) - 1

# Matrice pour stocker les vecteurs de densité de décharge
X_raw_density = np.zeros((100, num_bins))

# Listes pour les segments du raster plot
xs, y0s, y1s = [], [], []
h = 0.8  # hauteur des barres de spikes
spike_counts_per_neuron = []

print("Traitement des spikes bruts et attribution des couleurs selon l’index du neurone...")

for i, col in enumerate(neurone_cols):
    # Récupérer les temps de spike pour le neurone courant
    spike_times = DATA.loc[DATA[col] == 1, "temps-ms"].values
    num_spikes = len(spike_times)
    spike_counts_per_neuron.append(num_spikes)

    # Calcul de l’histogramme de densité de décharge
    density_vector, _ = np.histogram(spike_times, bins=time_bins)
    X_raw_density[i, :] = density_vector

    # Ajouter les segments du raster plot
    xs.extend(spike_times.tolist())
    y0s.extend([i + 1] * num_spikes)
    y1s.extend([i + 1 + h] * num_spikes)

print("Attribution des couleurs selon les plages d’index...")

# --- ÉTAPE 2 : Attribution manuelle des couleurs selon l’index du neurone ---
colors_palette = Viridis3  # 3 couleurs

colors_raster = []

for i in range(100):

    # --- EXCEPTION : neurone index 30 (neurone31) en ROUGE ---
    if i == 30:
        neuron_color = "red"

    # --- Couleurs par plage d’index pour les autres neurones ---
    elif 1 <= i+1 <= 30:
        neuron_color = colors_palette[0]
    elif 31 <= i+1 <= 60:
        neuron_color = colors_palette[1]
    else:
        neuron_color = colors_palette[2]

    num_spikes = spike_counts_per_neuron[i]
    colors_raster.extend([neuron_color] * int(num_spikes))

print("Attribution des couleurs terminée. Génération du graphique Bokeh...")

# --- ÉTAPE 3 : Création de la figure interactive ---
source_raster = ColumnDataSource(data=dict(x=xs, y0=y0s, y1=y1s, color=colors_raster))

p = figure(
    width=1000, height=650,
    title=f"Raster Plot de 100 neurones (Couleur par plage d’index, bins={bin_size_ms}ms)",
    x_axis_label="Temps (ms)",
    y_axis_label="Index du neurone",
    tools="pan,wheel_zoom,box_zoom,reset,save",
    active_scroll="wheel_zoom",
)

# Dessiner les segments de spikes
p.segment(
    x0="x", y0="y0",
    x1="x", y1="y1",
    source=source_raster,
    color="color",
    line_width=1.2,
    line_alpha=0.8
)

# Ajouter l’outil de survol
hover = HoverTool(tooltips=[
    ("Index du neurone", "@y0"),
    ("Temps du spike", "@x{0.1f} ms")
])
p.add_tools(hover)

# Ajuster la plage de l’axe Y
p.y_range.start = 0
p.y_range.end = 102

show(p)

from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource, HoverTool
from bokeh.palettes import Viridis3
from bokeh.io import output_notebook
import pandas as pd
import numpy as np

# Afficher les graphiques Bokeh dans le notebook Jupyter
output_notebook()

# --- ÉTAPE 1 : Traitement des données brutes depuis le dataframe DATA ---
# Création de la liste des noms de colonnes des neurones
neurone_cols = [f"neurone{str(i).zfill(2)}" for i in range(1, 101)]
time_vector = DATA["temps-ms"].values
total_time = time_vector[-1]

# Définition des fenêtres temporelles pour le calcul de densité de décharge
bin_size_ms = 100
time_bins = np.arange(0, total_time + bin_size_ms, bin_size_ms)
num_bins = len(time_bins) - 1

# Matrice pour stocker les vecteurs de densité de décharge
X_raw_density = np.zeros((100, num_bins))

# Listes pour les segments du raster plot
xs, y0s, y1s = [], [], []
h = 0.8  # hauteur des barres de spikes
spike_counts_per_neuron = []

print("Traitement des spikes bruts et attribution des couleurs selon l’index du neurone...")

for i, col in enumerate(neurone_cols):
    # Récupérer les temps de spike pour le neurone courant
    spike_times = DATA.loc[DATA[col] == 1, "temps-ms"].values
    num_spikes = len(spike_times)
    spike_counts_per_neuron.append(num_spikes)

    # Calcul de l’histogramme de densité de décharge
    density_vector, _ = np.histogram(spike_times, bins=time_bins)
    X_raw_density[i, :] = density_vector

    # Ajouter les segments du raster plot
    xs.extend(spike_times.tolist())
    y0s.extend([i + 1] * num_spikes)
    y1s.extend([i + 1 + h] * num_spikes)

print("Attribution des couleurs selon les plages d’index...")

# --- ÉTAPE 2 : Attribution manuelle des couleurs selon l’index du neurone ---
colors_palette = Viridis3  # 3 couleurs




# --- ÉTAPE 3 : Création de la figure interactive ---
source_raster = ColumnDataSource(data=dict(x=xs, y0=y0s, y1=y1s, color=colors_raster))

p = figure(
    width=1000, height=650,
    title=f"Raster Plot de 100 neurones (Couleur par plage d’index, bins={bin_size_ms}ms)",
    x_axis_label="Temps (ms)",
    y_axis_label="Index du neurone",
    tools="pan,wheel_zoom,box_zoom,reset,save",
    active_scroll="wheel_zoom",
)

# Dessiner les segments de spikes
p.segment(
    x0="x", y0="y0",
    x1="x", y1="y1",
    source=source_raster,
    color="color",
    line_width=1.2,
    line_alpha=0.8
)

# Ajouter l’outil de survol
hover = HoverTool(tooltips=[
    ("Index du neurone", "@y0"),
    ("Temps du spike", "@x{0.1f} ms")
])
p.add_tools(hover)

# Ajuster la plage de l’axe Y
p.y_range.start = 0
p.y_range.end = 102

show(p)
# Création des feature 
# --- STEP 1: PREPARE DATA FOR CLUSTERING (Updated for 3 Populations) ---
neuron_cols = [c for c in DATA.columns if 'neurone' in c]
cluster_data = pd.DataFrame(index=neuron_cols)

# FEATURE 1: Average Activity (Firing Rate)
# La neurone parle-t‑elle beaucoup ou peu ? la fréquence
cluster_data['mean_activity'] = DATA[neuron_cols].mean()

# FEATURE 2: Variability (Standard Deviation)
# La neurone est‑elle constante ou change? variabilité
cluster_data['std_activity'] = DATA[neuron_cols].std()

# FEATURE 3: Persistence (Probability of consecutive spikes)
# Improved: we only check the next spike if the current state is 1
#Probabilité qu'un neurone reste actif à l'instant  t+1  sachant qu'il est actif à l'instant  t
# c'est là ou il prent en compte la dymanique temporelle
def calc_persistence(series):
    current_is_spike = (series == 1)
    if current_is_spike.sum() == 0: return 0
    next_is_spike = (series.shift(-1) == 1)
    # Probability: P(spike at t+1 | spike at t)
    return (current_is_spike & next_is_spike).sum() / current_is_spike.sum()

cluster_data['persistence'] = DATA[neuron_cols].apply(calc_persistence)
cluster_data
#  PCA 

# --- STEP 2: SCALE THE FEATURES ---
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_scaled = scaler.fit_transform(cluster_data)
from sklearn.decomposition import PCA # il manquait ça
pca = PCA(n_components=2)
pca_results = pca.fit_transform(X_scaled)

# 4. Visualization using the K-means labels for comparison
plt.figure(figsize=(10, 7))
scatter = plt.scatter(pca_results[:, 0],
                      pca_results[:, 1],

                      cmap='viridis', s=100, edgecolors='k')

plt.title('PCA: Neural Classification based on Statistical Features', fontsize=14)
plt.xlabel(f'PC1 ({pca.explained_variance_ratio_[0]*100:.1f}% variance)')
plt.ylabel(f'PC2 ({pca.explained_variance_ratio_[1]*100:.1f}% variance)')
plt.colorbar(scatter, label='K-means Group')
plt.grid(True, alpha=0.3)
plt.show()
# KMEANS PCA

Porquoi regrouper avec KMeans et visualiser avec PCA?

Sans les étiquettes du K-means, nous verrions dans le PCA des groupes de points isolés mais sans distinction de catégorie. En combinant les deux, nous pouvons distinguer clairement les différentes classes (Sporadique, Burst, Tonique) et valider que l'algorithme de classification a correctement identifié les frontières entre chaque population.

# 1. Choose k=3 because we know there are 3 populations (Sporadic, Burst, Tonic)
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
cluster_labels = kmeans.fit_predict(X_scaled)

# 2. Add the result to our cluster_data
cluster_data['cluster'] = cluster_labels

# 3. Reduce 3D (mean, std, persistence) to 2D (PCA 1, PCA 2) for plotting
# pca = PCA(n_components=2)
# X_pca = pca.fit_transform(X_scaled)

# 4. Create the plot
plt.figure(figsize=(10, 7))
scatter = plt.scatter(pca_results[:, 0], pca_results[:, 1], c=cluster_labels, cmap='viridis', s=100, edgecolors='k', alpha=0.8)

# Add labels and styling
plt.title('Visualisation des 3 Populations Neuronales (KMeans+PCA)', fontsize=15)
plt.xlabel('Principal Component 1 (Représente l\'activité globale)', fontsize=12)
plt.ylabel('Principal Component 2 (Représente le rythme/variabilité)', fontsize=12)
plt.colorbar(scatter, label='Cluster ID')
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()
from codecarbon import EmissionsTracker
from sklearn.cluster import KMeans

# 1. Initialiser un tracker spécifique pour KMeans
tracker_kmeans = EmissionsTracker(
    project_name="Clustering_KMeans_Neurones",
    measure_power_secs=1  # On réduit à 1 seconde car KMeans est très rapide
)

# 2. Démarrer le tracker juste avant le calcul
tracker_kmeans.start()

try:
    print("Calcul du KMeans en cours...")
    
    # Votre code KMeans original
    kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
    cluster_labels = kmeans.fit_predict(X_scaled)
    
finally:
    # 3. Arrêter le tracker dès que c'est fini
    emissions_kmeans = tracker_kmeans.stop()
    print(f"\n--- RAPPORT ÉNERGÉTIQUE KMEANS ---")
    print(f"Énergie consommée : {emissions_kmeans:.10f} kWh")
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource, HoverTool, CategoricalColorMapper
from bokeh.palettes import Viridis3

from bokeh.io import output_notebook
from bokeh.plotting import figure, show
# ... (el resto de tus imports)

# IMPORTANT: This command tells Bokeh to render inside the Jupyter Notebook cells
output_notebook()

# 1. Data Preparation (Ensure column names match your dataframe)
plot_df = cluster_data.copy()
plot_df['pca_1'] = pca_results[:, 0]
plot_df['pca_2'] = pca_results[:, 1]
plot_df['cluster'] = plot_df['cluster'].astype(str)

source = ColumnDataSource(plot_df)

# 2. Color Mapping
# Mapping the three clusters ('0', '1', '2') to a specific 3-color palette
mapper = CategoricalColorMapper(factors=['0', '1', '2'], palette=Viridis3)

# 3. Figure Initialization
# Defining the plot title, axis labels, and interactive tools (zoom, pan, select)
p = figure(title="Exploration Interactive des Clusters (PCA)",
           x_axis_label='Principal Component 1',
           y_axis_label='Principal Component 2',
           width=800, height=600,
           tools="pan,wheel_zoom,box_select,reset,save")

# 4. Glyph Rendering (Scatter plot)
# Creating the circles; 'field' tells Bokeh to look inside the 'source' object
p.scatter('pca_1', 'pca_2', source=source,
          color={'field': 'cluster', 'transform': mapper},
          legend_field='cluster',
          size=12, alpha=0.7, line_color="black")

# 5. Interactive Inspection: HoverTool
# Tooltips show specific data values when hovering over a point
# Note: replace 'frequence' and 'cv' with your actual column names if they differ
hover = HoverTool(tooltips=[
    ("Neurone ID", "@index"),
    ("Cluster", "@cluster"),

])
p.add_tools(hover)

# 6. Legend Styling
p.legend.title = "Populations"
p.legend.location = "top_right"

# Render the interactive plot in the notebook or a new browser tab
show(p)
# VAE (self attention) avec KERAS

La structure de l'input (Samples, Window, Features) est un choix architectural crucial :

Approche Univariée (Feature = 1): Nous traitons chaque neurone comme une instance indépendante d'un comportement biologique. Cela multiplie par 100 la taille de notre dataset d'entraînement, permettant au VAE de capturer avec une grande précision la morphologie des spikes et des silences.

Approche Multivariée (Feature = 100) : Elle serait privilégiée si notre objectif était d'analyser la connectivité ou la synchronisation globale du réseau à chaque instant  t .

Pour ce projet, nous privilégions l'approche univariée afin de construire un espace latent robuste capable de discriminer les signatures individuelles de chaque type neuronal.

Note sur la Variabilité du VAE (Reproductibilité)
#  Ce code  c'est pour fixe  les résultat du variational autoencoder, car les pints son inicialiser par hazar au debut de l'entraienement
import numpy as np
import tensorflow as tf
import random
import os

def set_reproducibility(seed=42):
    # 1. Set Python hash seed
    os.environ['PYTHONHASHSEED'] = str(seed)

    # 2. Set Python random seed
    random.seed(seed)

    # 3. Set NumPy random seed
    np.random.seed(seed)

    # 4. Set TensorFlow random seed
    tf.random.set_seed(seed)

    # 5. Force TensorFlow to use single-thread (Optional, for absolute precision)
    os.environ['TF_DETERMINISTIC_OPS'] = '1'

# Call the function before building your VAE
set_reproducibility(42)

print(" Reproducibility seeds set. Results should be consistent now.")
# Enlever la colonne temps_normaliser de cette dataset
df= DATA.iloc[:, 3:103]
df.head()
Creation des fenétres
from sklearn.preprocessing import StandardScaler
import numpy as np

WINDOW = 50
STRIDE = 10  # <--- WE ADD THIS: Skip 10ms between windows to reduce redundancy

X_raw = df.values
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_raw)

all_windows = []

# Updated function to include STRIDE
def get_windows_optimized(signal, window, stride):
    # Calculate the number of windows possible with the stride
    num_windows = (signal.size - window) // stride + 1
    shape = (num_windows, window)
    # The strides define how many bytes to skip to find the next window
    strides = (signal.strides[0] * stride, signal.strides[0])
    return np.lib.stride_tricks.as_strided(signal, shape=shape, strides=strides)

# 2. Iterate through each neuron
for i in range(X_raw.shape[1]):
    neuron_signal = X_scaled[:, i]
    # Apply the stride here
    neuron_windows = get_windows_optimized(neuron_signal, WINDOW, STRIDE)
    all_windows.append(neuron_windows)

# 3. Concatenate (Now much lighter!)
train = np.vstack(all_windows).astype('float32')

# 4. Add feature dimension
train = np.expand_dims(train, axis=-1)

print("Final Training shape (Optimized):", train.shape)
# Expected: ~500,000 windows instead of 5,000,000
Encoder

construction de l'encoder avec attention L’encoder transforme la série en représentation latente.

Les étapes :

1️ Conv1D: capture des motifs temporels.

2️ MaxPooling: réduit la dimension.

3️ Attention le modèle apprend :quels moments du temps sont importants

4️ Dense produit :

z_mean

z_log_var

qui définissent la distribution latente du VAE.
# Define input dimensions
timesteps = train.shape[1]
features =train.shape[2]
latent_dim = 2

# Input layer
inputs = keras.Input(shape=(timesteps, features))

# Temporal feature extraction
x = layers.Conv1D(32, 3, padding="same", activation="relu")(inputs)
x = layers.MaxPooling1D(2)(x)

# Self-attention mechanism (TRASFORMERS)
attention = layers.Attention()([x, x])

# Combine convolution and attention outputs
x = layers.Concatenate()([x, attention])

# Flatten representation
x = layers.Flatten()(x)

# Latent distribution parameters
z_mean = layers.Dense(latent_dim)(x)
z_log_var = layers.Dense(latent_dim)(x)
Parametrisation

KL Loss : Cette fonction de perte force l'espace latent à ressembler à une distribution normale standard. Sans cela, le modèle pourrait simplement "mémoriser" les neurones au lieu d'apprendre leurs similitudes biologiques. C'est ce qui rend la séparation des groupes plus nette que dans un PCA classique.
class Sampling(layers.Layer):
    """Uses (z_mean, z_log_var) to sample z, the vector encoding a digit."""

    def call(self, inputs):
        z_mean, z_log_var = inputs

        # Reparameterization trick
        batch = keras.ops.shape(z_mean)[0]
        dim = keras.ops.shape(z_mean)[1]
        epsilon = keras.random.normal(shape=(batch, dim))
        z = z_mean + keras.ops.exp(0.5 * z_log_var) * epsilon

        # --- BETA-VAE ADJUSTMENT ---
        # We introduce beta to prevent "Posterior Collapse"
        # 0.001 helps the model prioritize reconstruction over regularisation
        beta = 0.001

        kl_loss = -0.5 * keras.ops.mean(
            1 + z_log_var - keras.ops.square(z_mean) - keras.ops.exp(z_log_var)
        )
        # Apply beta weight to the KL divergence loss
        self.add_loss(beta * kl_loss)

        return z

# Implementation in the model flow
z = Sampling()([z_mean, z_log_var])
Décodeur

Le décodeur a pour mission de reconstruire le signal original à partir des coordonnées compressées dans l'espace latent. Son architecture est le miroir inversé de l'encodeur
# Decoder network
decoder_inputs = layers.Dense((timesteps // 2) * 32, activation="relu")(z)

a = layers.Reshape((timesteps // 2, 32))(decoder_inputs)

a = layers.UpSampling1D(2)(a)
# Upsampling déploie les caracteristique aprisse sur l'axe du temps du temps
# Reconstruct original signal
# Nous utilisons une fonction d'activation Sigmoïde sur la dernière couche de convolution.
# Comme nos signaux d'entrée ont été normalisés entre 0 et 1 (MinMax) ou centrés,
#la sigmoïde garantit que la reconstruction respecte la plage de valeurs du signal biologique d'origine.
outputs = layers.Conv1D(1, 3, padding="same")(a)
# Define VAE model
vae = keras.Model(inputs, outputs, name= "VAE_Neuronal")
vae.compile(
    optimizer=keras.optimizers.Adam(),
    loss="mse")
# history = vae.fit(
#    train,
#    train,
#     epochs=30,
#     batch_size=512, # aumenter pour plus de rapidité
#     validation_split=0.1,
#     shuffle=True # très important pour que le modèle n'apprend pas l'ordre de des neurones
# )

# on va traker la consomation d'énergie
from codecarbon import EmissionsTracker

# --- 1. Initialiser le tracker ---
tracker = EmissionsTracker(
    project_name="Consommation_Energie_VAE_Keras",
    measure_power_secs=15
)

# --- 2. Démarrer la mesure ---
tracker.start()

print("Mesure de la consommation énergétique du VAE Keras...")

# --- 3. Entraînement mesuré ---
history = vae.fit(
    train,
    train,
    epochs=30,
    batch_size=512,
    validation_split=0.1,
    shuffle=True
)

# --- 4. Arrêter la mesure ---
energy_kwh = tracker.stop()

print("\n--- RÉSULTAT ---")
print(f"Énergie consommée par le VAE Keras (entraînement complet) : {energy_kwh:.6f} kWh")

plt.plot(history.history["loss"], label="Training Loss")
plt.plot(history.history["val_loss"], label="Validation Loss")
plt.legend()
plt.show()
print("MODÈLE VAE COMPLET")

vae.summary()
Une fois l'entraînement terminé, nous extrayons uniquement la partie Encodeur du VAE. Ce sous-modèle nous permet de projeter n'importe quelle fenêtre temporelle de 50ms vers notre espace latent de dimension 2. Nous utiliserons principalement z_mean car il représente la position la plus probable du signal dans cet espace.

# Create a sub-model that only includes the Encoder part
# This model takes the windowed signal and returns (z_mean, z_log_var, z)
encoder_model = keras.Model(inputs, [z_mean, z_log_var, z])

# Explanation: We only need the 'z_mean' (the coordinates) for our representation
Pour obtenir une classification robuste, nous calculons la signature latente moyenne de chaque neurone. Étant donné qu'un neurone est représenté par des milliers de fenêtres, nous calculons le centroïde (la moyenne) de toutes ses projections. Ce point moyen stabilise la représentation et élimine les variations locales du signal pour ne garder que le comportement intrinsèque de la cellule.
# Calculate how many windows we have in total and how many per neuron
total_windows = train.shape[0]
num_neurons = 100
windows_per_neuron = total_windows // num_neurons

neuron_representations = []

# Loop through each neuron to extract its specific latent signature
for i in range(num_neurons):
    # Dynamically define indices to avoid "Variable not defined" or "Out of bounds" errors
    start_idx = i * windows_per_neuron
    end_idx = (i + 1) * windows_per_neuron

    # Get all windows for the current neuron
    neuron_windows = train[start_idx:end_idx]

    # Check if the slice is not empty
    if len(neuron_windows) > 0:
        # Pass windows through the encoder to get latent space coordinates (z_mean)
        z_m, _, _ = encoder_model.predict(neuron_windows, batch_size=512, verbose=0)

        # Compute the centroid (mean position) of all windows for this neuron
        neuron_representations.append(np.mean(z_m, axis=0))

# Convert the list of centroids into a final 2D array for plotting
neuron_representations = np.array(neuron_representations)

print(f"Final representation shape: {neuron_representations.shape}") # Should be (100, 2)
La figure finale affiche les 100 neurones dans l'espace appris par le VAE.Séparation Non-Linéaire : Contrairement au PCA, cet espace a été construit en apprenant la dynamique complexe du temps.Interprétation des Axes : Les axes  z1  et  z2  ne sont pas de simples combinaisons linéaires, mais des abstractions des caractéristiques temporelles (rythme, burstiness, régularité).Validation : Si les groupes (Sporadiques, Bursts, Toniques) apparaissent plus compacts et mieux séparés qu'avec l'UMAP, cela prouve que le Deep Learning a réussi à extraire des descripteurs biologiques plus profonds que les simples statistiques descriptives.
import matplotlib.pyplot as plt
import numpy as np

# --- STEP 1: Fix the variable name error ---
# We retrieve the cluster labels from your previous K-means analysis
# Replace 'cluster_data' with the name of your main DataFrame if it is different
if 'cluster_data' in locals() or 'cluster_data' in globals():
    original_labels = cluster_data['cluster'].values
else:
    # Fallback: if the variable is not found, we assume the initial order
    # of the 100 neurons (30 Sporadic, 30 Bursts, 40 Toniques)
    original_labels = np.concatenate([np.zeros(30), np.ones(30), np.full(40, 2)])

# --- STEP 2: Visualization ---
plt.figure(figsize=(10, 7))

# Check if neuron_representations exists and has the correct shape (100, 2)
if 'neuron_representations' in locals() and neuron_representations.shape[0] == 100:

    # Plotting the 100 neurons in the Latent Space
    scatter = plt.scatter(neuron_representations[:, 0],
                          neuron_representations[:, 1],
                          c=original_labels,
                          cmap='viridis',
                          s=150,           # Increased size for better visibility
                          edgecolors='white', # White edges look cleaner than black
                          alpha=0.8)       # Slight transparency to see overlaps

    # Customizing the plot
    plt.title('VAE Latent Space: Neural Population Classification', fontsize=15, pad=20)
    plt.xlabel('Latent Dimension 1 (z_mean[0])', fontsize=12)
    plt.ylabel('Latent Dimension 2 (z_mean[1])', fontsize=12)

    # Adding a colorbar with labels
    cbar = plt.colorbar(scatter)
    cbar.set_label('Functional Group (K-means Cluster)', fontsize=12)

    plt.grid(True, linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.show()
else:
    print("Error: 'neuron_representations' not found or size is not 100. Please run the centroid calculation code first.")
# Visualisation interactive avec Bokeh
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource, ColorBar, LinearColorMapper, HoverTool
from bokeh.transform import transform
from bokeh.palettes import Viridis256
from bokeh.io import output_notebook
import numpy as np


output_notebook()


if 'cluster_data' in locals() or 'cluster_data' in globals():
    original_labels = cluster_data['cluster'].values
else:
    original_labels = np.concatenate([np.zeros(30), np.ones(30), np.full(40, 2)])


if 'neuron_representations' in locals() and neuron_representations.shape[0] == 100:

    x = neuron_representations[:,0]
    y = neuron_representations[:,1]

    source = ColumnDataSource(data=dict(
        x=x,
        y=y,
        cluster=original_labels,
        neuron_id=np.arange(len(x))
    ))

    # Color mapping
    color_mapper = LinearColorMapper(palette=Viridis256,
                                     low=min(original_labels),
                                     high=max(original_labels))


    p = figure(
        width=700,
        height=500,
        title="VAE Latent Space: Neural Population Classification",
        tools="pan,wheel_zoom,box_zoom,reset,hover,save"
    )

    # Scatter plot
    p.circle(
        x='x',
        y='y',
        size=12,
        source=source,
        fill_color=transform('cluster', color_mapper),
        line_color="white",
        alpha=0.8
    )

    # Hover tool
    hover = p.select_one(HoverTool)
    hover.tooltips = [
        ("Neuron", "@neuron_id"),
        ("Latent Z1", "@x"),
        ("Latent Z2", "@y"),
        ("Cluster", "@cluster"),
    ]

    # Colorbar
    color_bar = ColorBar(color_mapper=color_mapper, location=(0,0))
    p.add_layout(color_bar, 'right')

    # Labels
    p.xaxis.axis_label = "Latent Dimension 1 (z_mean[0])"
    p.yaxis.axis_label = "Latent Dimension 2 (z_mean[1])"

    show(p)

else:
    print("Error: 'neuron_representations' not found or size is not 100.")
# LA DETECTION

centroids = {}
for label in np.unique(original_labels):
    
    centroids[label] = neuron_representations[original_labels == label].mean(axis=0)


distances = []
for i in range(100):
    label = original_labels[i]
   
    dist = np.linalg.norm(neuron_representations[i] - centroids[label])
    distances.append(dist)

# Identify the absolute outlier (expected to be Neuron 31, index 30)
outlier_idx = np.argmax(distances)
print(f"Statistically identified outlier: Neuron {outlier_idx + 1}")


plt.figure(figsize=(12, 8))


scatter = plt.scatter(neuron_representations[:, 0],
                      neuron_representations[:, 1],
                      c=original_labels,
                      cmap='viridis', s=150, edgecolors='white', alpha=0.7)


plt.scatter(neuron_representations[30, 0],
            neuron_representations[30, 1],
            color='red', s=400, marker='X', label='Target: Neuron(Outlier)')


for i in range(100):
   
    if i == 30:  
        plt.annotate(f"N{i+1}",
                 (neuron_representations[i, 0], neuron_representations[i, 1]),
                 xytext=(8,8), textcoords='offset points',
                 fontsize=11, fontweight='bold')


# Formatting the plot
plt.title('Outlier Detection: Distance Analysis in VAE Latent Space', fontsize=16)
plt.xlabel('Latent Dimension 1 (z_mean[0])', fontsize=12)
plt.ylabel('Latent Dimension 2 (z_mean[1])', fontsize=12)
plt.legend(loc='best', frameon=True, shadow=True)
plt.grid(True, linestyle='--', alpha=0.4)
plt.colorbar(scatter, label='K-means Cluster ID')
plt.tight_layout()
plt.show()
# Modèle encodeur : de l'entrée jusqu'à z_mean
encoder = keras.Model(inputs, z_mean, name="encoder")

# Extraction des représentations latentes (z_mean)
latent_representations = encoder.predict(train)

import numpy as np

# Indices des neurones
idx_31 = 30
idx_36 = 52

# Distance euclidienne dans l’espace latent du VAE
distance_31_36 = np.linalg.norm(latent_representations[idx_31] -
                                latent_representations[idx_36])

print("Distance VAE entre Neurone 31 et Neurone 53 :", distance_31_36)

## VAE self-Attention 3 époques
# Decoder network
decoder_inputs = layers.Dense((timesteps // 2) * 32, activation="relu")(z)

a = layers.Reshape((timesteps // 2, 32))(decoder_inputs)

a = layers.UpSampling1D(2)(a)
# Upsampling déploie les caracteristique aprisse sur l'axe du temps du temps
# Reconstruct original signal
# Nous utilisons une fonction d'activation Sigmoïde sur la dernière couche de convolution.
# Comme nos signaux d'entrée ont été normalisés entre 0 et 1 (MinMax) ou centrés,
#la sigmoïde garantit que la reconstruction respecte la plage de valeurs du signal biologique d'origine.
outputs = layers.Conv1D(1, 3, padding="same")(a)
# Define VAE model
vae = keras.Model(inputs, outputs, name= "VAE_Neuronal")
vae.compile(
    optimizer=keras.optimizers.Adam(),
    loss="mse")
 
from codecarbon import EmissionsTracker

# --- 1. Initialiser le tracker ---
tracker = EmissionsTracker(
    project_name="Consommation_Energie_VAE_Keras",
    measure_power_secs=15
)

# --- 2. Démarrer la mesure ---
tracker.start()

print("Mesure de la consommation énergétique du VAE Keras...")

# --- 3. Entraînement mesuré ---
history = vae.fit(
    train,
    train,
    epochs=3,
    batch_size=512,
    validation_split=0.1,
    shuffle=True
)

# --- 4. Arrêter la mesure ---
energy_kwh = tracker.stop()

print("\n--- RÉSULTAT ---")
print(f"Énergie consommée par le VAE Keras (entraînement complet) : {energy_kwh:.6f} kWh")

plt.plot(history.history["loss"], label="Training Loss")
plt.plot(history.history["val_loss"], label="Validation Loss")
plt.legend()
plt.show()

# Create a sub-model that only includes the Encoder part
# This model takes the windowed signal and returns (z_mean, z_log_var, z)
encoder_model = keras.Model(inputs, [z_mean, z_log_var, z])

# Explanation: We only need the 'z_mean' (the coordinates) for our representation
# Calculate how many windows we have in total and how many per neuron
total_windows = train.shape[0]
num_neurons = 100
windows_per_neuron = total_windows // num_neurons

neuron_representations = []

# Loop through each neuron to extract its specific latent signature
for i in range(num_neurons):
    # Dynamically define indices to avoid "Variable not defined" or "Out of bounds" errors
    start_idx = i * windows_per_neuron
    end_idx = (i + 1) * windows_per_neuron

    # Get all windows for the current neuron
    neuron_windows = train[start_idx:end_idx]

    # Check if the slice is not empty
    if len(neuron_windows) > 0:
        # Pass windows through the encoder to get latent space coordinates (z_mean)
        z_m, _, _ = encoder_model.predict(neuron_windows, batch_size=512, verbose=0)

        # Compute the centroid (mean position) of all windows for this neuron
        neuron_representations.append(np.mean(z_m, axis=0))

# Convert the list of centroids into a final 2D array for plotting
neuron_representations = np.array(neuron_representations)

print(f"Final representation shape: {neuron_representations.shape}") # Should be (100, 2)

import matplotlib.pyplot as plt
import numpy as np

# --- STEP 1: Fix the variable name error ---
# We retrieve the cluster labels from your previous K-means analysis
# Replace 'cluster_data' with the name of your main DataFrame if it is different
if 'cluster_data' in locals() or 'cluster_data' in globals():
    original_labels = cluster_data['cluster'].values
else:
    # Fallback: if the variable is not found, we assume the initial order
    # of the 100 neurons (30 Sporadic, 30 Bursts, 40 Toniques)
    original_labels = np.concatenate([np.zeros(30), np.ones(30), np.full(40, 2)])

# --- STEP 2: Visualization ---
plt.figure(figsize=(10, 7))

# Check if neuron_representations exists and has the correct shape (100, 2)
if 'neuron_representations' in locals() and neuron_representations.shape[0] == 100:

    # Plotting the 100 neurons in the Latent Space
    scatter = plt.scatter(neuron_representations[:, 0],
                          neuron_representations[:, 1],
                          c=original_labels,
                          cmap='viridis',
                          s=150,           # Increased size for better visibility
                          edgecolors='white', # White edges look cleaner than black
                          alpha=0.8)       # Slight transparency to see overlaps

    # Customizing the plot
    plt.title('VAE Latent Space: Neural Population Classification', fontsize=15, pad=20)
    plt.xlabel('Latent Dimension 1 (z_mean[0])', fontsize=12)
    plt.ylabel('Latent Dimension 2 (z_mean[1])', fontsize=12)

    # Adding a colorbar with labels
    cbar = plt.colorbar(scatter)
    cbar.set_label('Functional Group (K-means Cluster)', fontsize=12)

    plt.grid(True, linestyle='--', alpha=0.5)
    plt.tight_layout()
    #plt.scatter(neuron_centroids[30, 0], neuron_centroids[30, 1], color='red', marker='X', s=300, label='Outlier Target (N31)')
    plt.show()
else:
    print("Error: 'neuron_representations' not found or size is not 100. Please run the centroid calculation code first.")

from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource, ColorBar, LinearColorMapper, HoverTool
from bokeh.transform import transform
from bokeh.palettes import Viridis256
from bokeh.io import output_notebook
import numpy as np


output_notebook()


if 'cluster_data' in locals() or 'cluster_data' in globals():
    original_labels = cluster_data['cluster'].values
else:
    original_labels = np.concatenate([np.zeros(30), np.ones(30), np.full(40, 2)])


if 'neuron_representations' in locals() and neuron_representations.shape[0] == 100:

    x = neuron_representations[:,0]
    y = neuron_representations[:,1]

    source = ColumnDataSource(data=dict(
        x=x,
        y=y,
        cluster=original_labels,
        neuron_id=np.arange(len(x))
    ))

    # Color mapping
    color_mapper = LinearColorMapper(palette=Viridis256,
                                     low=min(original_labels),
                                     high=max(original_labels))


    p = figure(
        width=700,
        height=500,
        title="VAE Latent Space: Neural Population Classification",
        tools="pan,wheel_zoom,box_zoom,reset,hover,save"
    )

    # Scatter plot
    p.circle(
        x='x',
        y='y',
        size=12,
        source=source,
        fill_color=transform('cluster', color_mapper),
        line_color="white",
        alpha=0.8
    )

    # Hover tool
    hover = p.select_one(HoverTool)
    hover.tooltips = [
        ("Neuron", "@neuron_id"),
        ("Latent Z1", "@x"),
        ("Latent Z2", "@y"),
        ("Cluster", "@cluster"),
    ]

    # Colorbar
    color_bar = ColorBar(color_mapper=color_mapper, location=(0,0))
    p.add_layout(color_bar, 'right')

    # Labels
    p.xaxis.axis_label = "Latent Dimension 1 (z_mean[0])"
    p.yaxis.axis_label = "Latent Dimension 2 (z_mean[1])"

    show(p)

else:
    print("Error: 'neuron_representations' not found or size is not 100.")
# Pytorch Mult-Attention
import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from torch.utils.data import DataLoader, TensorDataset, random_split
from codecarbon import EmissionsTracker

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print("Using:", device)

# --- 1. PRÉPARATION DES DONNÉES ---
df_neurons = DATA.iloc[:, 3:103]
num_neurons = df_neurons.shape[1]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(df_neurons.values)

# --- 2. FENÊTRAGE (Optimisé avec DataLoader) ---
def get_windows_optimized(data_array, window, stride):
    all_windows = []
    for i in range(data_array.shape[1]):
        signal = data_array[:, i]
        num_w = (len(signal) - window) // stride + 1
        shape = (num_w, window)
        strides = (signal.strides[0] * stride, signal.strides[0])
        neuron_windows = np.lib.stride_tricks.as_strided(
            signal, shape=shape, strides=strides
        )
        all_windows.append(neuron_windows)

    final_data = np.vstack(all_windows).astype('float32')
    return torch.tensor(final_data).unsqueeze(1)

WINDOW, STRIDE = 50, 10
train_tensor = get_windows_optimized(X_scaled, WINDOW, STRIDE)

# --- SÉPARATION ENTRAÎNEMENT / VALIDATION (80% / 20%) ---
dataset_total = TensorDataset(train_tensor)
train_size = int(0.8 * len(dataset_total))
val_size = len(dataset_total) - train_size

train_dataset, val_dataset = random_split(dataset_total, [train_size, val_size])

batch_size = 1024
train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
val_loader = DataLoader(val_dataset, batch_size=batch_size, shuffle=False)

# --- 3. ARCHITECTURE VAE ATTENTION ---
class VAE_Attention(nn.Module):
    def __init__(self, window_size, latent_dim=2):
        super(VAE_Attention, self).__init__()
        self.conv1 = nn.Conv1d(1, 32, kernel_size=3, padding=1)
        self.pool = nn.MaxPool1d(2)
        self.attention = nn.MultiheadAttention(
            embed_dim=32, num_heads=4, batch_first=True
        )
        self.flatten_dim = (window_size // 2) * 64
        self.fc_mu = nn.Linear(self.flatten_dim, latent_dim)
        self.fc_logvar = nn.Linear(self.flatten_dim, latent_dim)
        self.dec_fc = nn.Linear(latent_dim, (window_size // 2) * 32)
        self.upsample = nn.Upsample(scale_factor=2)
        self.conv_out = nn.Conv1d(32, 1, kernel_size=3, padding=1)

    def reparameterize(self, mu, logvar):
        std = torch.exp(0.5 * logvar)
        eps = torch.randn_like(std)
        return mu + eps * std

    def forward(self, x):
        x_c = F.relu(self.conv1(x))
        x_p = self.pool(x_c)
        x_attn_in = x_p.transpose(1, 2)
        attn_out, _ = self.attention(x_attn_in, x_attn_in, x_attn_in)
        x_flat = torch.cat([x_attn_in, attn_out], dim=-1).reshape(x.size(0), -1)
        mu, logvar = self.fc_mu(x_flat), self.fc_logvar(x_flat)
        z = self.reparameterize(mu, logvar)
        d = F.relu(self.dec_fc(z)).view(z.size(0), 32, -1)
        recon = self.conv_out(self.upsample(d))
        return recon, mu, logvar

# --- 4. ENTRAÎNEMENT + TRACKING ÉNERGÉTIQUE ---
model = VAE_Attention(window_size=WINDOW).to(device)
optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)

epochs = 30
history_train_loss = []
history_val_loss = []

tracker_train = EmissionsTracker(
    project_name="Consommation_Energie_VAE_Attention_Training",
    measure_power_secs=15
)

print("Mesure de la consommation énergétique du VAE multi-Attention (entraînement)...")
tracker_train.start()

for epoch in range(epochs):
    model.train()
    total_train_loss = 0
    for batch in train_loader:
        batch_data = batch[0].to(device)
        optimizer.zero_grad()

        recon, mu, logvar = model(batch_data)
        mse_loss = F.mse_loss(recon, batch_data, reduction='sum')
        kl_loss = -0.5 * torch.sum(1 + logvar - mu.pow(2) - logvar.exp())
        loss = mse_loss + 0.001 * kl_loss

        loss.backward()
        optimizer.step()
        total_train_loss += loss.item()

    model.eval()
    total_val_loss = 0
    with torch.no_grad():
        for batch in val_loader:
            batch_data = batch[0].to(device)
            recon, mu, logvar = model(batch_data)
            mse_loss = F.mse_loss(recon, batch_data, reduction='sum')
            kl_loss = -0.5 * torch.sum(1 + logvar - mu.pow(2) - logvar.exp())
            loss = mse_loss + 0.001 * kl_loss
            total_val_loss += loss.item()

    epoch_train_loss = total_train_loss / len(train_loader.dataset)
    epoch_val_loss = total_val_loss / len(val_loader.dataset)

    history_train_loss.append(epoch_train_loss)
    history_val_loss.append(epoch_val_loss)

    if epoch % 5 == 0 or epoch == epochs - 1:
        print(f"Époque {epoch:02d} | Train Loss: {epoch_train_loss:.4f} | Val Loss: {epoch_val_loss:.4f}")

energy_train = tracker_train.stop()
print("\n--- RÉSULTAT ---")
print(f"Énergie consommée par le VAE multi-Attention (entraînement complet) : {energy_train:.6f} kWh")

# --- 4bis. INFÉRENCE + TRACKING ÉNERGÉTIQUE ---
tracker_inf = EmissionsTracker(
    project_name="Consommation_Energie_VAE_multiAttention_Inference",
    measure_power_secs=15
)

print("\nMesure de la consommation énergétique du VAE multi-Attention (inférence)...")
tracker_inf.start()

model.eval()
with torch.no_grad():
    for i in range(0, len(train_tensor), batch_size):
        batch_eval = train_tensor[i:i+batch_size].to(device)
        recon, mu_batch, _ = model(batch_eval)

energy_inf = tracker_inf.stop()
print(f"Énergie consommée par le VAE multi-Attention (inférence) : {energy_inf:.6f} kWh")

energie_totale = energy_train + energy_inf
print(f"\nÉnergie totale du VAE multi-Attention (train + inférence) : {energie_totale:.6f} kWh")

# --- 5. COURBES D'APPRENTISSAGE ---
plt.figure(figsize=(8, 5))
plt.plot(history_train_loss, label='Training Loss', color='#1f77b4', linewidth=2)
plt.plot(history_val_loss, label='Validation Loss', color='#ff7f0e', linewidth=2)
plt.xlabel('Epochs', fontsize=12)
plt.ylabel('Loss', fontsize=12)
plt.legend(fontsize=12, loc='upper right')
plt.show()

# --- 6. VISUALISATION (Espace Latent) ---
model.eval()
z_list = []
with torch.no_grad():
    for i in range(0, len(train_tensor), batch_size):
        batch_eval = train_tensor[i:i+batch_size].to(device)
        _, mu_batch, _ = model(batch_eval)
        z_list.append(mu_batch.cpu().numpy())

z_points = np.vstack(z_list)

windows_per_neuron = z_points.shape[0] // num_neurons
neuron_centroids = np.array([
    np.mean(z_points[i*windows_per_neuron:(i+1)*windows_per_neuron], axis=0)
    for i in range(num_neurons)
])

dist_to_center = np.linalg.norm(
    neuron_centroids - np.mean(neuron_centroids, axis=0), axis=1
)

plt.figure(figsize=(10, 7))
plt.scatter(
    neuron_centroids[:, 0], neuron_centroids[:, 1],
    c=dist_to_center, cmap='viridis', s=150, edgecolors='white'
)
plt.scatter(
    neuron_centroids[30, 0], neuron_centroids[30, 1],
    color='red', marker='X', s=300, label='Outlier Target (N31)'
)
plt.title("Latent Space (PyTorch + Batch Training)")
plt.colorbar(label="Anomaly Score")
plt.legend()
plt.show()

# VISUALISATION INRETACTIVE AVEC BOKEH
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource, ColorBar, LinearColorMapper, HoverTool
from bokeh.io import output_notebook
from bokeh.palettes import Viridis256
import numpy as np

output_notebook()

# --- Numéro du neurone anormal ---
neurone_anormal = 30

# --- Identifiants des neurones ---
neurone_ids = np.arange(len(neuron_centroids))

# --- Source pour tous les neurones ---
source = ColumnDataSource(data=dict(
    x = neuron_centroids[:, 0],
    y = neuron_centroids[:, 1],
    score = dist_to_center,
    neurone = neurone_ids
))

# --- Source séparée pour le neurone anormal ---
source_anormal = ColumnDataSource(data=dict(
    x = [neuron_centroids[neurone_anormal, 0]],
    y = [neuron_centroids[neurone_anormal, 1]],
    score = [dist_to_center[neurone_anormal]],
    neurone = [neurone_anormal]
))

# --- Mapper couleur pour les neurones normaux ---
color_mapper = LinearColorMapper(
    palette=Viridis256,
    low=np.min(dist_to_center),
    high=np.max(dist_to_center)
)

# --- Figure ---
p = figure(
    width=800,
    height=600,
    title="Espace latent du VAE (anormal en rouge)",
    x_axis_label="Dimension latente 1",
    y_axis_label="Dimension latente 2",
    tools="pan,wheel_zoom,box_zoom,reset,save",
    active_scroll="wheel_zoom"
)

# --- HoverTool (fonctionne pour les deux sources) ---
hover = HoverTool(tooltips=[
    ("Neurone", "@neurone"),
    ("Score anomalie", "@score{0.000}")
])
p.add_tools(hover)

# --- Neurones normaux ---
p.circle(
    x="x",
    y="y",
    size=12,
    source=source,
    color={'field': 'score', 'transform': color_mapper},
    line_color=None
)

# --- Neurone anormal (rouge vif, avec hover correct) ---
p.circle(
    x="x",
    y="y",
    size=22,
    source=source_anormal,
    color="#ff0000",
    line_color=None,
    legend_label="Neurone anormal"
)

# --- Barre de couleur ---
color_bar = ColorBar(color_mapper=color_mapper, label_standoff=12, width=12)
p.add_layout(color_bar, 'right')

p.legend.location = "top_left"

show(p)

## Pytorch Multi-Attention 3 époques
import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from torch.utils.data import DataLoader, TensorDataset, random_split
from codecarbon import EmissionsTracker

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print("Using:", device)

# --- 1. PRÉPARATION DES DONNÉES ---
df_neurons = DATA.iloc[:, 3:103]
num_neurons = df_neurons.shape[1]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(df_neurons.values)

# --- 2. FENÊTRAGE (Optimisé avec DataLoader) ---
def get_windows_optimized(data_array, window, stride):
    all_windows = []
    for i in range(data_array.shape[1]):
        signal = data_array[:, i]
        num_w = (len(signal) - window) // stride + 1
        shape = (num_w, window)
        strides = (signal.strides[0] * stride, signal.strides[0])
        neuron_windows = np.lib.stride_tricks.as_strided(
            signal, shape=shape, strides=strides
        )
        all_windows.append(neuron_windows)

    final_data = np.vstack(all_windows).astype('float32')
    return torch.tensor(final_data).unsqueeze(1)

WINDOW, STRIDE = 50, 10
train_tensor = get_windows_optimized(X_scaled, WINDOW, STRIDE)

# --- SÉPARATION ENTRAÎNEMENT / VALIDATION (80% / 20%) ---
dataset_total = TensorDataset(train_tensor)
train_size = int(0.8 * len(dataset_total))
val_size = len(dataset_total) - train_size

train_dataset, val_dataset = random_split(dataset_total, [train_size, val_size])

batch_size = 1024
train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
val_loader = DataLoader(val_dataset, batch_size=batch_size, shuffle=False)

# --- 3. ARCHITECTURE VAE ATTENTION ---
class VAE_Attention(nn.Module):
    def __init__(self, window_size, latent_dim=2):
        super(VAE_Attention, self).__init__()
        self.conv1 = nn.Conv1d(1, 32, kernel_size=3, padding=1)
        self.pool = nn.MaxPool1d(2)
        self.attention = nn.MultiheadAttention(
            embed_dim=32, num_heads=4, batch_first=True
        )
        self.flatten_dim = (window_size // 2) * 64
        self.fc_mu = nn.Linear(self.flatten_dim, latent_dim)
        self.fc_logvar = nn.Linear(self.flatten_dim, latent_dim)
        self.dec_fc = nn.Linear(latent_dim, (window_size // 2) * 32)
        self.upsample = nn.Upsample(scale_factor=2)
        self.conv_out = nn.Conv1d(32, 1, kernel_size=3, padding=1)

    def reparameterize(self, mu, logvar):
        std = torch.exp(0.5 * logvar)
        eps = torch.randn_like(std)
        return mu + eps * std

    def forward(self, x):
        x_c = F.relu(self.conv1(x))
        x_p = self.pool(x_c)
        x_attn_in = x_p.transpose(1, 2)
        attn_out, _ = self.attention(x_attn_in, x_attn_in, x_attn_in)
        x_flat = torch.cat([x_attn_in, attn_out], dim=-1).reshape(x.size(0), -1)
        mu, logvar = self.fc_mu(x_flat), self.fc_logvar(x_flat)
        z = self.reparameterize(mu, logvar)
        d = F.relu(self.dec_fc(z)).view(z.size(0), 32, -1)
        recon = self.conv_out(self.upsample(d))
        return recon, mu, logvar

# --- 4. ENTRAÎNEMENT + TRACKING ÉNERGÉTIQUE ---
model = VAE_Attention(window_size=WINDOW).to(device)
optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)

epochs = 4
history_train_loss = []
history_val_loss = []

tracker_train = EmissionsTracker(
    project_name="Consommation_Energie_VAE_Attention_Training",
    measure_power_secs=15
)

print("Mesure de la consommation énergétique du VAE multi-Attention (entraînement)...")
tracker_train.start()

for epoch in range(epochs):
    model.train()
    total_train_loss = 0
    for batch in train_loader:
        batch_data = batch[0].to(device)
        optimizer.zero_grad()

        recon, mu, logvar = model(batch_data)
        mse_loss = F.mse_loss(recon, batch_data, reduction='sum')
        kl_loss = -0.5 * torch.sum(1 + logvar - mu.pow(2) - logvar.exp())
        loss = mse_loss + 0.001 * kl_loss

        loss.backward()
        optimizer.step()
        total_train_loss += loss.item()

    model.eval()
    total_val_loss = 0
    with torch.no_grad():
        for batch in val_loader:
            batch_data = batch[0].to(device)
            recon, mu, logvar = model(batch_data)
            mse_loss = F.mse_loss(recon, batch_data, reduction='sum')
            kl_loss = -0.5 * torch.sum(1 + logvar - mu.pow(2) - logvar.exp())
            loss = mse_loss + 0.001 * kl_loss
            total_val_loss += loss.item()

    epoch_train_loss = total_train_loss / len(train_loader.dataset)
    epoch_val_loss = total_val_loss / len(val_loader.dataset)

    history_train_loss.append(epoch_train_loss)
    history_val_loss.append(epoch_val_loss)

    if epoch % 5 == 0 or epoch == epochs - 1:
        print(f"Époque {epoch:02d} | Train Loss: {epoch_train_loss:.4f} | Val Loss: {epoch_val_loss:.4f}")

energy_train = tracker_train.stop()
print("\n--- RÉSULTAT ---")
print(f"Énergie consommée par le VAE multi-Attention (entraînement complet) : {energy_train:.6f} kWh")

# --- 4bis. INFÉRENCE + TRACKING ÉNERGÉTIQUE ---
tracker_inf = EmissionsTracker(
    project_name="Consommation_Energie_VAE_multiAttention_Inference",
    measure_power_secs=15
)

print("\nMesure de la consommation énergétique du VAE multi-Attention (inférence)...")
tracker_inf.start()

model.eval()
with torch.no_grad():
    for i in range(0, len(train_tensor), batch_size):
        batch_eval = train_tensor[i:i+batch_size].to(device)
        recon, mu_batch, _ = model(batch_eval)

energy_inf = tracker_inf.stop()
print(f"Énergie consommée par le VAE multi-Attention (inférence) : {energy_inf:.6f} kWh")

energie_totale = energy_train + energy_inf
print(f"\nÉnergie totale du VAE multi-Attention (train + inférence) : {energie_totale:.6f} kWh")

# --- 5. COURBES D'APPRENTISSAGE ---
plt.figure(figsize=(8, 5))
plt.plot(history_train_loss, label='Training Loss', color='#1f77b4', linewidth=2)
plt.plot(history_val_loss, label='Validation Loss', color='#ff7f0e', linewidth=2)
plt.xlabel('Epochs', fontsize=12)
plt.ylabel('Loss', fontsize=12)
plt.legend(fontsize=12, loc='upper right')
plt.show()

# --- 6. VISUALISATION (Espace Latent) ---
model.eval()
z_list = []
with torch.no_grad():
    for i in range(0, len(train_tensor), batch_size):
        batch_eval = train_tensor[i:i+batch_size].to(device)
        _, mu_batch, _ = model(batch_eval)
        z_list.append(mu_batch.cpu().numpy())

z_points = np.vstack(z_list)

windows_per_neuron = z_points.shape[0] // num_neurons
neuron_centroids = np.array([
    np.mean(z_points[i*windows_per_neuron:(i+1)*windows_per_neuron], axis=0)
    for i in range(num_neurons)
])

dist_to_center = np.linalg.norm(
    neuron_centroids - np.mean(neuron_centroids, axis=0), axis=1
)

plt.figure(figsize=(10, 7))
plt.scatter(
    neuron_centroids[:, 0], neuron_centroids[:, 1],
    c=dist_to_center, cmap='viridis', s=150, edgecolors='white'
)
plt.scatter(
    neuron_centroids[30, 0], neuron_centroids[30, 1],
    color='red', marker='X', s=300, label='Outlier Target (N31)'
)
plt.title("Latent Space (PyTorch + Batch Training)")
plt.colorbar(label="Anomaly Score")
plt.legend()
plt.show()

# visualisation

from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource, ColorBar, LinearColorMapper, HoverTool
from bokeh.io import output_notebook
from bokeh.palettes import Viridis256
import numpy as np

output_notebook()

# --- Numéro du neurone anormal ---
neurone_anormal = 30

# --- Identifiants des neurones ---
neurone_ids = np.arange(len(neuron_centroids))

# --- Source pour tous les neurones ---
source = ColumnDataSource(data=dict(
    x = neuron_centroids[:, 0],
    y = neuron_centroids[:, 1],
    score = dist_to_center,
    neurone = neurone_ids
))

# --- Source séparée pour le neurone anormal ---
source_anormal = ColumnDataSource(data=dict(
    x = [neuron_centroids[neurone_anormal, 0]],
    y = [neuron_centroids[neurone_anormal, 1]],
    score = [dist_to_center[neurone_anormal]],
    neurone = [neurone_anormal]
))

# --- Mapper couleur pour les neurones normaux ---
color_mapper = LinearColorMapper(
    palette=Viridis256,
    low=np.min(dist_to_center),
    high=np.max(dist_to_center)
)

# --- Figure ---
p = figure(
    width=800,
    height=600,
    title="Espace latent du VAE (anormal en rouge)",
    x_axis_label="Dimension latente 1",
    y_axis_label="Dimension latente 2",
    tools="pan,wheel_zoom,box_zoom,reset,save",
    active_scroll="wheel_zoom"
)

# --- HoverTool (fonctionne pour les deux sources) ---
hover = HoverTool(tooltips=[
    ("Neurone", "@neurone"),
    ("Score anomalie", "@score{0.000}")
])
p.add_tools(hover)

# --- Neurones normaux ---
p.circle(
    x="x",
    y="y",
    size=12,
    source=source,
    color={'field': 'score', 'transform': color_mapper},
    line_color=None
)

# --- Neurone anormal (rouge vif, avec hover correct) ---
p.circle(
    x="x",
    y="y",
    size=22,
    source=source_anormal,
    color="#ff0000",
    line_color=None,
    legend_label="Neurone anormal"
)

# --- Barre de couleur ---
color_bar = ColorBar(color_mapper=color_mapper, label_standoff=12, width=12)
p.add_layout(color_bar, 'right')

p.legend.location = "top_left"

show(p)
# snntorch
import torch
import torch.nn as nn
import snntorch as snn
from snntorch import surrogate
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
import torch.nn.functional as F
from torch.utils.data import DataLoader, TensorDataset, random_split
from codecarbon import EmissionsTracker

# --- 1. PRÉPARATION DES DONNÉES ---
df_neurons = DATA.iloc[:, 3:103]
num_neurons = df_neurons.shape[1]

scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(df_neurons.values)

def get_windows_snn(data_array, window, stride):
    all_windows = []
    for i in range(data_array.shape[1]):
        signal = data_array[:, i]
        num_w = (len(signal) - window) // stride + 1
        shape = (num_w, window)
        strides = (signal.strides[0] * stride, signal.strides[0])
        neuron_windows = np.lib.stride_tricks.as_strided(
            signal, shape=shape, strides=strides
        )
        all_windows.append(neuron_windows)
    return torch.tensor(np.vstack(all_windows).astype('float32'))

WINDOW, STRIDE = 50, 10
train_tensor = get_windows_snn(X_scaled, WINDOW, STRIDE)

# --- DIVISION ENTRAÎNEMENT / VALIDATION (80% / 20%) ---
dataset_total = TensorDataset(train_tensor)
train_size = int(0.8 * len(dataset_total))
val_size = len(dataset_total) - train_size

train_dataset, val_dataset = random_split(dataset_total, [train_size, val_size])

batch_size = 256
train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
val_loader = DataLoader(val_dataset, batch_size=batch_size, shuffle=False)

# --- 2. ARCHITECTURE SNN VAE ---
device = torch.device("cuda") if torch.cuda.is_available() else torch.device("cpu")

class SpikingVAE(nn.Module):
    def __init__(self, window_size, latent_dim=2):
        super().__init__()

        beta_lif = 0.9
        spike_grad = surrogate.fast_sigmoid()

        # Encoder
        self.fc_enc = nn.Linear(window_size, 128)
        self.lif_enc = snn.Leaky(beta=beta_lif, spike_grad=spike_grad)

        self.fc_mu = nn.Linear(128, latent_dim)
        self.fc_logvar = nn.Linear(128, latent_dim)

        # Decoder
        self.fc_dec = nn.Linear(latent_dim, 128)
        self.lif_dec = snn.Leaky(beta=beta_lif, spike_grad=spike_grad)
        self.fc_out = nn.Linear(128, window_size)

    def reparameterize(self, mu, logvar):
        std = torch.exp(0.5 * logvar)
        eps = torch.randn_like(std)
        return mu + eps * std

    def forward(self, x):
        mem_enc = self.lif_enc.init_leaky()
        mem_dec = self.lif_dec.init_leaky()

        cur = self.fc_enc(x)
        spk, mem_enc = self.lif_enc(cur, mem_enc)
        latent_avg = spk

        mu = self.fc_mu(latent_avg)
        logvar = self.fc_logvar(latent_avg)
        z = self.reparameterize(mu, logvar)

        d_cur = self.fc_dec(z)
        spk_dec, mem_dec = self.lif_dec(d_cur, mem_dec)
        recon = self.fc_out(spk_dec)

        return recon, mu, logvar

# --- 3. ENTRAÎNEMENT + MESURE ÉNERGÉTIQUE ---
model = SpikingVAE(window_size=WINDOW).to(device)
optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)

epochs = 31
history_train_loss = []
history_val_loss = []

tracker_train = EmissionsTracker(
    project_name="Consommation_Energie_SNN_Training",
    measure_power_secs=15
)

print("Mesure de la consommation énergétique du VAE SNN (entraînement)...")
tracker_train.start()

print("Début entraînement snnTorch...")
for epoch in range(epochs):
    # Phase d'entraînement
    model.train()
    total_train_loss = 0
    for batch in train_loader:
        data_batch = batch[0].to(device)
        optimizer.zero_grad()

        recon, mu, logvar = model(data_batch)

        loss_recon = F.mse_loss(recon, data_batch, reduction='sum')
        loss_kld = -0.5 * torch.sum(1 + logvar - mu.pow(2) - logvar.exp())
        loss = loss_recon + 0.001 * loss_kld

        loss.backward()
        optimizer.step()
        total_train_loss += loss.item()

    # Phase de validation
    model.eval()
    total_val_loss = 0
    with torch.no_grad():
        for batch in val_loader:
            data_batch = batch[0].to(device)
            recon, mu, logvar = model(data_batch)

            loss_recon = F.mse_loss(recon, data_batch, reduction='sum')
            loss_kld = -0.5 * torch.sum(1 + logvar - mu.pow(2) - logvar.exp())
            loss = loss_recon + 0.001 * loss_kld
            total_val_loss += loss.item()

    epoch_train_loss = total_train_loss / len(train_loader.dataset)
    epoch_val_loss = total_val_loss / len(val_loader.dataset)
    
    history_train_loss.append(epoch_train_loss)
    history_val_loss.append(epoch_val_loss)

    if epoch % 10 == 0 or epoch == epochs - 1:
        print(f"Époque {epoch:02d} | Train Loss: {epoch_train_loss:.4f} | Val Loss: {epoch_val_loss:.4f}")

energy_train = tracker_train.stop()
print("\n--- RÉSULTAT ---")
print(f"Énergie consommée par le VAE SNN (entraînement complet) : {energy_train:.6f} kWh")

# --- 3bis. MESURE ÉNERGÉTIQUE INFÉRENCE ---
tracker_inf = EmissionsTracker(
    project_name="Consommation_Energie_SNN_Inference",
    measure_power_secs=15
)

print("\nMesure de la consommation énergétique du VAE SNN (inférence)...")
tracker_inf.start()

model.eval()
with torch.no_grad():
    for i in range(0, len(train_tensor), 512):
        b = train_tensor[i:i+512].to(device)
        _ , mu_b, _ = model(b)

energy_inf = tracker_inf.stop()
print(f"Énergie consommée par le VAE SNN (inférence) : {energy_inf:.6f} kWh")

energie_totale = energy_train + energy_inf
print(f"\nÉnergie totale du VAE SNN (train + inférence) : {energie_totale:.6f} kWh")

# --- 4. COURBES D'APPRENTISSAGE ---
plt.figure(figsize=(8, 5))
plt.plot(history_train_loss, label='Training Loss', color='#1f77b4', linewidth=2)
plt.plot(history_val_loss, label='Validation Loss', color='#ff7f0e', linewidth=2)
plt.xlabel('Epochs', fontsize=12)
plt.ylabel('Loss', fontsize=12)
plt.legend(fontsize=12, loc='upper right')
plt.title("Courbe d'apprentissage (Spiking VAE)")
plt.show()

# --- 5. ANALYSE LATENTE + CENTROÏDES ---
model.eval()
z_list = []
with torch.no_grad():
    for i in range(0, len(train_tensor), 512):
        b = train_tensor[i:i+512].to(device)
        _, mu_b, _ = model(b)
        z_list.append(mu_b.cpu().numpy())

z_points = np.vstack(z_list)
windows_per_neuron = z_points.shape[0] // num_neurons
neuron_centroids = np.array([
    np.mean(z_points[i*windows_per_neuron:(i+1)*windows_per_neuron], axis=0)
    for i in range(num_neurons)
])

# --- 6. GRAPHIQUE ESPACE LATENT ---
plt.figure(figsize=(10, 6))
plt.scatter(neuron_centroids[:, 0], neuron_centroids[:, 1],
            c='purple', alpha=0.6, s=100, label='Neurones SNN')
plt.scatter(neuron_centroids[30, 0], neuron_centroids[30, 1],
            c='red', marker='X', s=300, label='Outlier Target (N31)')
plt.title("Espace Latent snnTorch (Spiking VAE)")
plt.xlabel("Dim Z1")
plt.ylabel("Dim Z2")
plt.legend()
plt.show()

## SNN avec 3 époques
# epoque energie traking
import torch
import torch.nn as nn
import snntorch as snn
from snntorch import surrogate
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
import torch.nn.functional as F
from torch.utils.data import DataLoader, TensorDataset, random_split
from codecarbon import EmissionsTracker

# --- 1. PRÉPARATION DES DONNÉES ---
df_neurons = DATA.iloc[:, 3:103]
num_neurons = df_neurons.shape[1]

scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(df_neurons.values)

def get_windows_snn(data_array, window, stride):
    all_windows = []
    for i in range(data_array.shape[1]):
        signal = data_array[:, i]
        num_w = (len(signal) - window) // stride + 1
        shape = (num_w, window)
        strides = (signal.strides[0] * stride, signal.strides[0])
        neuron_windows = np.lib.stride_tricks.as_strided(
            signal, shape=shape, strides=strides
        )
        all_windows.append(neuron_windows)
    return torch.tensor(np.vstack(all_windows).astype('float32'))

WINDOW, STRIDE = 50, 10
train_tensor = get_windows_snn(X_scaled, WINDOW, STRIDE)

# --- DIVISION ENTRAÎNEMENT / VALIDATION ---
dataset_total = TensorDataset(train_tensor)
train_size = int(0.8 * len(dataset_total))
val_size = len(dataset_total) - train_size

train_dataset, val_dataset = random_split(dataset_total, [train_size, val_size])

batch_size = 256
train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
val_loader = DataLoader(val_dataset, batch_size=batch_size, shuffle=False)

# --- 2. ARCHITECTURE SNN VAE ---
device = torch.device("cuda") if torch.cuda.is_available() else torch.device("cpu")

class SpikingVAE(nn.Module):
    def __init__(self, window_size, latent_dim=2):
        super().__init__()

        beta_lif = 0.9
        spike_grad = surrogate.fast_sigmoid()

        # Encoder
        self.fc_enc = nn.Linear(window_size, 128)
        self.lif_enc = snn.Leaky(beta=beta_lif, spike_grad=spike_grad)

        self.fc_mu = nn.Linear(128, latent_dim)
        self.fc_logvar = nn.Linear(128, latent_dim)

        # Decoder
        self.fc_dec = nn.Linear(latent_dim, 128)
        self.lif_dec = snn.Leaky(beta=beta_lif, spike_grad=spike_grad)
        self.fc_out = nn.Linear(128, window_size)

    def reparameterize(self, mu, logvar):
        std = torch.exp(0.5 * logvar)
        eps = torch.randn_like(std)
        return mu + eps * std

    def forward(self, x):
        mem_enc = self.lif_enc.init_leaky()
        mem_dec = self.lif_dec.init_leaky()

        cur = self.fc_enc(x)
        spk, mem_enc = self.lif_enc(cur, mem_enc)
        latent_avg = spk

        mu = self.fc_mu(latent_avg)
        logvar = self.fc_logvar(latent_avg)
        z = self.reparameterize(mu, logvar)

        d_cur = self.fc_dec(z)
        spk_dec, mem_dec = self.lif_dec(d_cur, mem_dec)
        recon = self.fc_out(spk_dec)

        return recon, mu, logvar

# --- 3. ENTRAÎNEMENT + MESURE ÉNERGÉTIQUE ---
model = SpikingVAE(window_size=WINDOW).to(device)
optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)

epochs = 4
history_train_loss = []
history_val_loss = []

# --- TRACKER TRAIN ---
tracker_train = EmissionsTracker(
    project_name="Consommation_Energie_SNN_Training",
    measure_power_secs=15
)

print("Mesure énergétique : entraînement complet du SNN...")
tracker_train.start()

print("Début entraînement snnTorch...")
for epoch in range(epochs):

    # --- Entraînement ---
    model.train()
    total_train_loss = 0
    for batch in train_loader:
        data_batch = batch[0].to(device)
        optimizer.zero_grad()

        recon, mu, logvar = model(data_batch)
        loss_recon = F.mse_loss(recon, data_batch, reduction='sum')
        loss_kld = -0.5 * torch.sum(1 + logvar - mu.pow(2) - logvar.exp())
        loss = loss_recon + 0.001 * loss_kld

        loss.backward()
        optimizer.step()
        total_train_loss += loss.item()

    # --- Validation ---
    model.eval()
    total_val_loss = 0
    with torch.no_grad():
        for batch in val_loader:
            data_batch = batch[0].to(device)
            recon, mu, logvar = model(data_batch)
            loss_recon = F.mse_loss(recon, data_batch, reduction='sum')
            loss_kld = -0.5 * torch.sum(1 + logvar - mu.pow(2) - logvar.exp())
            loss = loss_recon + 0.001 * loss_kld
            total_val_loss += loss.item()

    epoch_train_loss = total_train_loss / len(train_loader.dataset)
    epoch_val_loss = total_val_loss / len(val_loader.dataset)

    history_train_loss.append(epoch_train_loss)
    history_val_loss.append(epoch_val_loss)

    print(f"Époque {epoch:02d} | Train Loss: {epoch_train_loss:.4f} | Val Loss: {epoch_val_loss:.4f}")

energy_train = tracker_train.stop()
print("\n--- RÉSULTAT ---")
print(f"Énergie consommée par le SNN (entraînement complet) : {energy_train:.6f} kWh")

# --- 3bis. INFÉRENCE + ÉNERGIE ---
tracker_inf = EmissionsTracker(
    project_name="Consommation_Energie_SNN_Inference",
    measure_power_secs=15
)

print("\nMesure énergétique : inférence du SNN...")
tracker_inf.start()

model.eval()
with torch.no_grad():
    for i in range(0, len(train_tensor), 512):
        b = train_tensor[i:i+512].to(device)
        _ , mu_b, _ = model(b)

energy_inf = tracker_inf.stop()
print(f"Énergie consommée par l’inférence : {energy_inf:.6f} kWh")

energie_totale = energy_train + energy_inf
print(f"\nÉnergie totale du SNN (train + inférence) : {energie_totale:.6f} kWh")

# --- 4. COURBES D'APPRENTISSAGE ---
plt.figure(figsize=(8, 5))
plt.plot(history_train_loss, label='Training Loss', color='#1f77b4', linewidth=2)
plt.plot(history_val_loss, label='Validation Loss', color='#ff7f0e', linewidth=2)
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.title("Courbe d'apprentissage (Spiking VAE)")
plt.show()

# --- 5. ANALYSE LATENTE ---
model.eval()
z_list = []
with torch.no_grad():
    for i in range(0, len(train_tensor), 512):
        b = train_tensor[i:i+512].to(device)
        _, mu_b, _ = model(b)
        z_list.append(mu_b.cpu().numpy())

z_points = np.vstack(z_list)
windows_per_neuron = z_points.shape[0] // num_neurons
neuron_centroids = np.array([
    np.mean(z_points[i*windows_per_neuron:(i+1)*windows_per_neuron], axis=0)
    for i in range(num_neurons)
])

# --- 6. GRAPHIQUE ESPACE LATENT ---
plt.figure(figsize=(10, 6))
plt.scatter(neuron_centroids[:, 0], neuron_centroids[:, 1],
            c='purple', alpha=0.6, s=100, label='Neurones SNN')
plt.scatter(neuron_centroids[30,0], neuron_centroids[30,1],
            c='red', marker='X', s=300, label='Outlier Target (N31)')
plt.title("Espace Latent snnTorch (Spiking VAE)")
plt.xlabel("Dim Z1")
plt.ylabel("Dim Z2")
plt.legend()
plt.show()

from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource, HoverTool
from bokeh.io import output_notebook

output_notebook()

# Datos: solo los centroides del VAE
source = ColumnDataSource(data=dict(
    z1=neuron_centroids[:, 0],
    z2=neuron_centroids[:, 1],
    idx=list(range(len(neuron_centroids)))
))

# Figura interactiva
p = figure(
    width=800,
    height=500,
    title="Espace Latent snnTorch (Spiking VAE)",
    x_axis_label="Dim Z1",
    y_axis_label="Dim Z2",
    tools="pan,wheel_zoom,box_zoom,reset,save"
)

# Puntos normales (solo resultados)
p.circle(
    x="z1",
    y="z2",
    size=10,
    fill_color="purple",
    fill_alpha=0.6,
    line_color=None,
    source=source
)

# Hover interactivo
hover = HoverTool(tooltips=[
    ("Neurone", "@idx"),
    ("Z1", "@z1{0.000}"),
    ("Z2", "@z2{0.000}")
])
p.add_tools(hover)

p.legend.location = "top_left"

show(p)

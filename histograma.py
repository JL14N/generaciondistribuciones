import matplotlib.pyplot as plt
import io
import random


def generar_color():
    return "#{:06x}".format(random.randint(0, 0xFFFFFF))


def graficar_histograma(vector, intervalos):
    fig, ax = plt.subplots(figsize=(10, 6))  # Adjust figure size for better visibility
    
    # Generate a random color for the histogram bars
    color = generar_color()
    
    # Create the histogram
    n, bins, patches = ax.hist(vector, bins=intervalos, edgecolor='black', color=color)
    
    # Set labels and title
    ax.set_xlabel('Intervalos')
    ax.set_ylabel('Frecuencia')
    ax.set_title('Histograma de Frecuencias')
    
    # Annotate bars with their height (frequency)
    for i in range(len(patches)):
        height = patches[i].get_height()
        ax.text(patches[i].get_x() + patches[i].get_width() / 2, height, f'{int(height)}', 
                ha='center', va='bottom')
    
    # Label x-axis with interval limits
    interval_labels = [f'{bins[i]:.2f}' for i in range(len(bins)-1)]
    
    # Ensure all boundaries are included in x-ticks
    ax.set_xticks(bins)
    
    # Make sure the number of labels matches the number of ticks
    if len(interval_labels) < len(bins):
        interval_labels.append(f'{bins[-1]:.2f}')  # Add last boundary label if needed
    
    ax.set_xticklabels(interval_labels, rotation=45, ha='right')
    
    # Adjust layout to prevent label clipping
    plt.tight_layout()
    
    # Save the histogram image to a BytesIO buffer
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    plt.close(fig)
    
    return buf


def guardar_imagen(buf, filename):
    # filepath = os.path.join("static", filename)
    with open("static/" + filename, 'wb') as f:
        f.write(buf.getvalue())
    return "static/" + filename
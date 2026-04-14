import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

# 📸 obraz wejściowy
image = np.array([
    [1, 2, 3, 0, 1],
    [0, 1, 2, 3, 1],
    [1, 2, 1, 0, 0],
    [0, 1, 3, 1, 2],
    [2, 0, 1, 3, 1]
])

# 🔲 kernel (pionowe krawędzie)
kernel = np.array([
    [1, 0, -1],
    [1, 0, -1],
    [1, 0, -1]
])

k = kernel.shape[0]
out_size = image.shape[0] - k + 1
output = np.zeros((out_size, out_size))

# lista kroków (pozycje kernela)
positions = [(i, j) for i in range(out_size) for j in range(out_size)]

fig, ax = plt.subplots()

def update(frame):
    ax.clear()
    
    i, j = positions[frame]
    
    # fragment obrazu
    patch = image[i:i+k, j:j+k]
    value = np.sum(patch * kernel)
    output[i, j] = value

    # rysujemy obraz
    ax.imshow(image, cmap='gray')
    
    # zaznaczamy aktualny obszar kernela
    rect = plt.Rectangle((j-0.5, i-0.5), k, k, 
                         edgecolor='red', facecolor='none', linewidth=2)
    ax.add_patch(rect)
    
    # tytuł
    ax.set_title(f"Pozycja ({i},{j}) | wartość = {value:.1f}")
    
    # ukrywamy osie
    ax.set_xticks([])
    ax.set_yticks([])

# tworzymy animację
ani = animation.FuncAnimation(
    fig,
    update,
    frames=len(positions),
    interval=1000,  # czas między klatkami (ms)
    repeat=False
)

plt.show()
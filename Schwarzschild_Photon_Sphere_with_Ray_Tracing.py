import numpy as np
import matplotlib.pyplot as plt

# ==========================
# Figure Setup
# ==========================
fig, ax = plt.subplots(figsize=(10, 10))
fig.patch.set_facecolor("black")
ax.set_facecolor("black")

# ==========================
# Background Stars
# ==========================
np.random.seed(42)

star_x = np.random.uniform(-10, 10, 300)
star_y = np.random.uniform(-10, 10, 300)

ax.scatter(
    star_x,
    star_y,
    s=np.random.uniform(1, 10, 300),
    color="white",
    alpha=0.8
)

# ==========================
# Event Horizon
# ==========================
event_horizon = plt.Circle(
    (0, 0),
    1,
    color="black",
    zorder=10
)
ax.add_artist(event_horizon)

# ==========================
# Photon Sphere
# ==========================
theta = np.linspace(0, 2*np.pi, 1000)

photon_radius = 1.5

ax.plot(
    photon_radius*np.cos(theta),
    photon_radius*np.sin(theta),
    'r--',
    lw=2,
    label="Photon Sphere"
)

# ==========================
# Accretion Disk
# ==========================
for r in np.linspace(2, 3, 30):

    ax.plot(
        r*np.cos(theta),
        r*np.sin(theta),
        color='orange',
        alpha=0.05,
        lw=8
    )

# ==========================
# Curved Photon Rays
# ==========================
angles = np.linspace(0, 2*np.pi, 24)

for angle in angles:

    t = np.linspace(0, 8, 500)

    r = photon_radius + 0.08*t**2

    x = r*np.cos(angle + 0.15*np.log(t+1))
    y = r*np.sin(angle + 0.15*np.log(t+1))

    ax.plot(
        x,
        y,
        color='cyan',
        lw=1.5,
        alpha=0.8
    )

# ==========================
# Labels
# ==========================
ax.annotate(
    "Photon Sphere",
    xy=(1.5, 0),
    xytext=(4, 1),
    color="white",
    arrowprops=dict(
        arrowstyle="->",
        color="white"
    )
)

ax.annotate(
    "Black Hole",
    xy=(0, 0),
    xytext=(-5, -2),
    color="white",
    arrowprops=dict(
        arrowstyle="->",
        color="white"
    )
)

# ==========================
# Formatting
# ==========================
ax.set_title(
    "Schwarzschild Black Hole with Photon Sphere",
    color="white",
    fontsize=16
)

ax.set_xlabel("x", color="white")
ax.set_ylabel("y", color="white")

ax.tick_params(colors="white")

ax.set_aspect("equal")

ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)

ax.legend(facecolor="black")

plt.show()
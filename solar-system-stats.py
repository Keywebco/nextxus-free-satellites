# solar_system_stats.py
# Source: an AI Mode conversation Roger pasted 2026-11-19 (his request:
# "Free code to make an orbital solar system graphic with statistics").
# Desktop program: Python + matplotlib. Run: pip install matplotlib,
# then: python solar_system_stats.py
# The web version of this graphic lives in the Federation science gallery
# (science-gallery.html, same planet data and statistics).
import math
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Planet data: (name, semi-major axis in AU, orbital period in Earth days,
#               orbital speed in km/s, radius in km, color)
PLANETS = [
    ("Mercury", 0.39, 87.97, 47.36, 2439.7, "#A5A5A5"),
    ("Venus", 0.72, 224.70, 35.02, 6051.8, "#E3BB76"),
    ("Earth", 1.00, 365.25, 29.78, 6371.0, "#4F94CD"),
    ("Mars", 1.52, 686.98, 24.07, 3389.5, "#D95F43"),
    ("Jupiter", 5.20, 4332.59, 13.07, 69911.0, "#D8CA9D"),
    ("Saturn", 9.58, 10759.22, 9.68, 58232.0, "#EAD6B8"),
    ("Uranus", 19.20, 30688.50, 6.80, 25362.0, "#72B5C4"),
    ("Neptune", 30.05, 60195.00, 5.43, 24622.0, "#3E66F9"),
]

fig, (ax_orb, ax_stat) = plt.subplots(
    1, 2, figsize=(12, 6), gridspec_kw={"width_ratios": [2.2, 1]}
)
fig.patch.set_facecolor("#0B0E17")

# Left subplot: Orbital graphic
ax_orb.set_facecolor("#0B0E17")
ax_orb.set_aspect("equal")
lim = 33
ax_orb.set_xlim(-lim, lim)
ax_orb.set_ylim(-lim, lim)
ax_orb.set_xlabel("Distance (AU)", color="white")
ax_orb.set_ylabel("Distance (AU)", color="white")
ax_orb.tick_params(colors="white")
ax_orb.scatter([0], [0], s=260, color="#FDB813", label="Sun", zorder=5)

theta_circle = [2 * math.pi * i / 360 for i in range(361)]
planet_dots = []
for name, au, period, speed, radius, color in PLANETS:
    ox = [au * math.cos(t) for t in theta_circle]
    oy = [au * math.sin(t) for t in theta_circle]
    ax_orb.plot(ox, oy, linestyle=":", linewidth=0.8, color=color, alpha=0.5)
    dot, = ax_orb.plot([], [], marker="o", markersize=6, color=color, label=name)
    planet_dots.append(dot)

# Right subplot: Statistics panel
ax_stat.set_facecolor("#131826")
ax_stat.set_xticks([])
ax_stat.set_yticks([])
ax_stat.set_title("Orbital Statistics", color="white", fontsize=12, pad=10)
stats_text = ax_stat.text(
    0.05, 0.95, "", transform=ax_stat.transAxes,
    va="top", ha="left", color="#E6EDF3", fontsize=9.5, family="monospace"
)

# Advance 15 Earth days per frame
DT_DAYS = 15.0

def update(frame):
    days = frame * DT_DAYS
    lines = [
        f"Elapsed Time: {days:,.0f} days",
        f"Approx. Years: {days / 365.25:.2f} yr",
        "-" * 31,
        f"{'Planet':<8} {'AU':>5} {'km/s':>6} {'Rad(km)':>8}",
        "-" * 31,
    ]
    for idx, (name, au, period, speed, radius, color) in enumerate(PLANETS):
        angle = 2 * math.pi * (days / period)
        x = au * math.cos(angle)
        y = au * math.sin(angle)
        planet_dots[idx].set_data([x], [y])
        lines.append(f"{name:<8} {au:>5.2f} {speed:>6.2f} {radius:>8.0f}")

    stats_text.set_text("\n".join(lines))
    return planet_dots + [stats_text]

ani = FuncAnimation(fig, update, frames=400, interval=40, blit=True)
plt.tight_layout()
plt.show()

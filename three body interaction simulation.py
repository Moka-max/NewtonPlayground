import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, FFMpegWriter # Added FFMpegWriter

# =================== CONFIG ===================

G = 3  # Gravitational constant
initial_N = 3  # Initial number of bodies

# Assign different masses
masses = np.array([100.0, 100.0, 200.0])
radius_thresh = 0.001  # Distance threshold for collisions and force singularity fix

# Initial positions (equilateral triangle)
positions = np.array([
    [0.0, 1.0],
    [-np.sqrt(3)/2, -0.5],
    [np.sqrt(3)/2, -0.5]
], dtype=float)

# Initial velocities (rough orbital balance)
momenta = np.array([
    [0.0, 1.5],
    [-0.8660254037844387, -0.5],
    [0.8660254037844387, -0.5],
]) * masses[:, None]

# =================== PHYSICS ===================

def compute_accelerations(pos, mass):
    acc = np.zeros_like(pos)
    for i in range(len(pos)):
        for j in range(len(pos)):
            if i != j:
                r_vec = pos[j] - pos[i]
                r = np.linalg.norm(r_vec)
                if r < radius_thresh:
                    r = radius_thresh
                acc[i] += G * mass[j] * r_vec / r**3
    return acc

def leapfrog_step(pos, mom, mass, dt):
    acc = compute_accelerations(pos, mass)
    mom += 0.5 * acc * dt
    pos += (mom / mass[:, None]) * dt
    acc = compute_accelerations(pos, mass)
    mom += 0.5 * acc * dt
    return pos, mom

def compute_energy(pos, mom, mass):
    KE = 0.5 * np.sum(np.sum((mom / mass[:, None])**2, axis=1) * mass)
    PE = 0.0
    for i in range(len(pos)):
        for j in range(i+1, len(pos)):
            r = np.linalg.norm(pos[i] - pos[j])
            if r < radius_thresh:
                r = radius_thresh
            PE -= G * mass[i] * mass[j] / r
    return KE + PE

def check_collisions(pos, mom, mass):
    new_pos, new_mom, new_mass = [], [], []
    merged = [False] * len(pos)

    for i in range(len(pos)):
        if merged[i]:
            continue
        for j in range(i+1, len(pos)):
            if merged[j]:
                continue
            dist = np.linalg.norm(pos[i] - pos[j])
            if dist < radius_thresh:
                total_mass = mass[i] + mass[j]
                com_pos = (mass[i]*pos[i] + mass[j]*pos[j]) / total_mass
                com_mom = mom[i] + mom[j]
                new_pos.append(com_pos)
                new_mom.append(com_mom)
                new_mass.append(total_mass)
                merged[i] = merged[j] = True
                break
        if not merged[i]:
            new_pos.append(pos[i])
            new_mom.append(mom[i])
            new_mass.append(mass[i])

    return np.array(new_pos), np.array(new_mom), np.array(new_mass)

# =================== SIMULATION ===================

dt = 0.01
steps = 2000

history = []
energy_hist = []

pos = positions.copy()
mom = momenta.copy()
mass = masses.copy()

for _ in range(steps):
    pos, mom = leapfrog_step(pos, mom, mass, dt)
    pos, mom, mass = check_collisions(pos, mom, mass)
    history.append(pos.copy())
    energy_hist.append(compute_energy(pos, mom, mass))

max_particles = initial_N

# =================== ANIMATION ===================

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
colors = ['cyan', 'magenta', 'orange', 'lime', 'yellow']

lines, dots, waves = [], [], []

for i in range(max_particles):
    line, = ax1.plot([], [], lw=2, color=colors[i % len(colors)], alpha=0.7)
    dot, = ax1.plot([], [], 'o', color=colors[i % len(colors)], markersize=6)
    wave, = ax1.plot([], [], lw=1, color=colors[i % len(colors)], alpha=0.3)
    lines.append(line)
    dots.append(dot)
    waves.append(wave)

ax1.set_xlim(-4, 4)
ax1.set_ylim(-4, 4)
ax1.set_title("N-Body Gravitational Simulation with Collision & Waves")
ax1.set_facecolor("black")
ax1.set_xticks([])
ax1.set_yticks([])
ax1.set_aspect('equal')

ax2.set_xlim(0, steps)
# Ensure energy_hist is not empty before finding min/max
if energy_hist:
    ax2.set_ylim(min(energy_hist) * 1.05 if min(energy_hist) < 0 else min(energy_hist) * 0.95,
                 max(energy_hist) * 1.05 if max(energy_hist) > 0 else max(energy_hist) * 0.95)
else:
    ax2.set_ylim(-1, 1) # Default if no energy data

energy_line, = ax2.plot([], [], color='white')
ax2.set_title("Total Energy Over Time")
ax2.set_facecolor("black")
ax2.set_xlabel("Time Step")
ax2.set_ylabel("Energy")

def init():
    for line, dot, wave in zip(lines, dots, waves):
        line.set_data([], [])
        dot.set_data([], [])
        wave.set_data([], [])
    energy_line.set_data([], [])
    return lines + dots + waves + [energy_line]

def update(frame):
    current_pos = history[frame]
    n_particles = len(current_pos)
    trail_length = 100
    start = max(0, frame - trail_length)

    for i in range(max_particles):
        if i < n_particles:
            trail = []
            for h_idx in range(start, frame + 1): # Iterate using index for history
                if i < len(history[h_idx]):
                    trail.append(history[h_idx][i])
                else:
                    # This particle might have merged and disappeared before this frame in the trail
                    pass # Or break, depending on desired trail behavior for merged particles
            trail = np.array(trail)

            if len(trail) > 0:
                lines[i].set_data(trail[:, 0], trail[:, 1])
                dots[i].set_data([trail[-1, 0]], [trail[-1, 1]])

                r_wave = 0.2 + 0.5 * abs(np.sin(0.1 * frame))
                theta = np.linspace(0, 2 * np.pi, 100)
                waves[i].set_data(trail[-1, 0] + r_wave * np.cos(theta),
                                  trail[-1, 1] + r_wave * np.sin(theta))
            else:
                lines[i].set_data([], [])
                dots[i].set_data([], [])
                waves[i].set_data([], [])
        else:
            lines[i].set_data([], [])
            dots[i].set_data([], [])
            waves[i].set_data([], [])

    x_vals = np.arange(frame + 1)
    y_vals = energy_hist[:frame + 1]
    if len(x_vals) == len(y_vals) and len(y_vals) > 0: # Ensure data consistency for energy plot
        energy_line.set_data(x_vals, y_vals)
    else:
        energy_line.set_data([], []) # Clear if inconsistent

    return lines + dots + waves + [energy_line]

ani = FuncAnimation(fig, update, frames=range(steps), init_func=init,
                    blit=True, interval=10)

plt.tight_layout()

# --- SAVING THE ANIMATION ---
try:
    # You can adjust fps (frames per second) and bitrate for quality/size
    writer = FFMpegWriter(fps=30, metadata=dict(artist='Me'), bitrate=1800)
    ani.save("n_body_simulation_video.mp4", writer=writer)
    print("Animation saved successfully as n_body_simulation_video.mp4")
except RuntimeError as e:
    print(f"Error saving animation: {e}")
    print("Make sure FFmpeg is installed and in your system's PATH.")
    print("Alternatively, you can save as a GIF using PillowWriter:")
     #from matplotlib.animation import PillowWriter
     #writer_gif = PillowWriter(fps=30)
     #ani.save("n_body_simulation_animation.gif", writer=writer_gif)
     #print("Animation saved as n_body_simulation_animation.gif")
except Exception as e:
    print(f"An unexpected error occurred while saving: {e}")


plt.show()

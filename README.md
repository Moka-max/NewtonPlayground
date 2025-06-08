# N-Body Gravitational Simulation with Collision and Energy Tracking

This project simulates the motion of celestial bodies under the influence of gravity using the **Leapfrog integration method**, with support for **collisions (merging bodies)** and **energy tracking** over time.

---

## Features

* **Leapfrog Integration**: Accurate and stable time integration suitable for gravitational simulations.
* **Collision Detection and Merging**: Bodies that come too close are merged into one, conserving mass and momentum.
* **Dynamic Trail Visualization**: Tracks and plots recent paths of all bodies.
* **Energy Tracking**: Computes total kinetic and potential energy at every step.
* **Radiating Wave Effect**: Adds aesthetic oscillating circles to represent motion.
* **Animation Output**: Generates a high-quality MP4 or GIF animation of the simulation.

---

## Simulation Setup

* **Gravitational Constant (G)**: 3
* **Number of Bodies**: 3 (modifiable)
* **Initial Conditions**: Positioned in an equilateral triangle with velocities set for approximate orbital behavior.
* **Collision Threshold**: `0.001` units (prevents singularities and triggers merging).
* **Steps**: 2000
* **Timestep (dt)**: 0.01

---

## Libraries Used

* `numpy`
* `matplotlib`
* `matplotlib.animation` (FuncAnimation, FFMpegWriter, PillowWriter)

---

## How to Run

1. Make sure you have **Python 3.7+** installed.
2. Install the dependencies:

   ```bash
   pip install numpy matplotlib
   ```
3. Ensure **FFmpeg** is installed and available in your system's PATH to save MP4.

   * Alternative: Comment out MP4 writer and use `PillowWriter` to save as GIF.
4. Run the script:

   ```bash
   python n_body_simulation.py
   ```

---

## Output

* **Live Animation Window**: Opens during simulation.
* **Saved File**:

  * `n_body_simulation_video.mp4` (preferred, high-quality)
  * `n_body_simulation_animation.gif` (fallback)

---

## File Breakdown

* `compute_accelerations(...)`: Computes net gravitational acceleration.
* `leapfrog_step(...)`: Applies leapfrog update rule.
* `compute_energy(...)`: Computes kinetic and potential energy.
* `check_collisions(...)`: Detects and merges close particles.
* `update(...)`: Handles per-frame drawing.

---

## Customization Tips

* Change `initial_N`, `positions`, `momenta`, and `masses` to explore different initial conditions.
* Increase `steps` or `trail_length` for longer simulation and trails.
* Add more aesthetic visuals like vector arrows, velocity indicators, etc.

---

## License

MIT License. Free to use, modify, and share.

---

## Author

Moka Uday Bhushanam - 2025

Happy simulating! ✨

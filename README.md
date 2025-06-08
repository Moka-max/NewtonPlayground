# 🌌 N-Body Gravitational Simulator

An interactive, scalable, and scientifically grounded Python-based N-body simulation that visualizes gravitational interactions between multiple celestial bodies in 2D. Developed using efficient numerical methods and visualized through real-time animations and data plots.

---

## ✨ Key Features

* 🔀 **Leapfrog Integration**: Symplectic, time-reversible integrator ideal for orbital mechanics.
* 🪐 **Variable Mass Particles**: Simulates planets, stars, asteroids, or custom bodies with realistic masses.
* ⚡ **Collision Handling**: Particles collide and merge using mass and momentum conservation laws.
* 🌊 **Gravitational Wave FX**: Simulates shockwave-like effects to highlight high-energy interactions.
* 🎥 **Real-Time Visualization**: Animate orbital dynamics with trails and live energy graphs.
* 📉 **Energy Conservation Tracker**: Plots kinetic, potential, and total energy over time.

---

## 🧠 Physics Behind the Code

This simulator solves Newton's law of universal gravitation for a system of $N$ bodies:

$$
F = G \cdot \frac{m_1 m_2}{r^2}
$$

The **Leapfrog Integrator** is chosen for its stability and energy-conserving properties:

* Position and velocity are staggered in time.
* Ideal for long-term simulations in celestial mechanics.

### Energy Calculations:

* **Kinetic Energy**:

  $$
  KE = \frac{1}{2}mv^2
  $$
* **Potential Energy**:

  $$
  PE = -\sum_{i<j} \frac{G m_i m_j}{r_{ij}}
  $$
* **Total Energy Conservation** is tracked in real-time.

---

## 📚 Applications

This project is a sandbox for:

* 🔭 Simulating galaxy formation
* 🚀 Modeling orbital mechanics for satellites
* 🧠 Educational demos in physics classrooms
* 💻 Stress-testing numerical solvers
* 🚗 Game or simulation backend engines

---

## 🔧 Customization Guide

Modify `main.py` or `config.py` to tweak:

```python
# Number of bodies
N_BODIES = 50

# Time step and total simulation duration
DT = 0.01
SIM_TIME = 100

# Collision mode (True = merge, False = bounce)
ENABLE_COLLISIONS = True

# Gravitational constant (scaled)
G = 6.67430e-11
```

---

## 🧪 Installation & Usage

### 📦 Install dependencies

```bash
pip install numpy matplotlib tqdm
```

### ▶️ Run the simulator

```bash
python main.py
```

---

## 🖥️ Performance Tips

* Reduce `N_BODIES` for faster simulations.
* Disable trails or plots for headless runs.
* Use `Numba` or `CuPy` for GPU acceleration (planned).
* Optimize with Barnes-Hut Tree (future enhancement).

---

## 🧱 Project Architecture

```
n_body_simulation/
├── main.py              # Simulation loop
├── config.py            # Configuration parameters
├── physics.py           # Force, velocity, integration logic
├── collision.py         # Merging & collision handling
├── visualize.py         # Animations & plots
├── utils.py             # Math utilities
├── assets/              # Simulation GIFs, media
├── README.md
└── requirements.txt
```

---

## 🙇‍♂️ Frequently Asked Questions (FAQ)

**Q: Can I use this in 3D?**
→ Currently 2D only, but 3D support is planned.

**Q: Can I run this on GPU?**
→ Not yet, but it's designed for easy integration with CuPy or PyTorch.

**Q: Will this work in real-time?**
→ Depends on particle count and CPU. <100 particles should run smoothly.

**Q: How are collisions handled?**
→ Masses and momenta are conserved. Radius scales with mass post-merger.

---

## 🤝 Contributing

Want to contribute? Open an issue, fork the repo, and submit a PR.

```bash
# Clone your fork
git clone https://github.com/yourusername/n-body-simulator.git

# Create a feature branch
git checkout -b add-feature-x

# Push and PR!
```

---

## 📜 License

This project is under the **MIT License**. See [LICENSE](LICENSE) for full terms.

---

## 👨‍💼 Author

**Moka Uday Bhushanam**
*ECE & Data Science Student | Aerospace Visionary | AI & Physics Enthusiast*

* 💼 [LinkedIn](https://www.linkedin.com/)
* 💡 [GitHub](https://github.com/)
* 📢 Drop a message for collab or feedback!

---

> *"Simulations may be synthetic—but the learning they spark is very real."* 🚀

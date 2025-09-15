# Isothermal Wind Solutions

This repository contains a Python implementation for solving and visualizing isothermal wind solutions, a classic model for stellar winds first described by Eugene Parker. The model provides a simplified framework for understanding the supersonic expansion of a star's corona into a stellar wind.

---

## Key Concepts & Solutions

The isothermal wind model assumes that the expanding stellar gas remains at a constant temperature. This simplifies the fluid dynamics equations, leading to a single differential equation for the velocity of the wind. A key feature of this model is the existence of a critical point at a specific radius, known as the sonic point. This point dictates the wind's behavior, and the physically realistic stellar wind solution is one that passes through this critical point, accelerating from subsonic to supersonic speeds.

This Python package generates a total of six different solutions to the momentum equation:

### Transonic Solutions
Only two solutions pass through the critical (sonic) point.

- **The Physically Realistic Solution**: This is the only physically viable solution, where the wind begins at a low (subsonic) speed near the star's surface and accelerates to supersonic speeds as it travels outwards. This is the solution that describes the actual solar wind.
- **The Supersonic-to-Subsonic Solution**: This is a purely mathematical curve. Although it passes through the sonic point, it describes a hypothetical flow that starts supersonic and decelerates to subsonic speeds, which is not observed in nature.

### Non-transonic Solutions
The remaining four solutions are considered unphysical.

- **Non-transonic Subsonic Solutions**: These solutions remain subsonic at all radii and do not cross the sonic point. They are unphysical as they require a finite density and pressure at large r values, which cannot be contained by the extremely small interstellar pressure.
- **Non-transonic Supersonic Solutions**: These solutions remain supersonic at all radii. They are unphysical as they suggest supersonic flows at the base of the corona, which is not acceptable as such high-velocity flows would cause shocks in the denser, lower corona.

### Multi-valued Solutions
The multi-valued solutions are purely mathematical (the curves describe wind trajectories that either don't extend into the heliosphere or do not connect to the base of the corona). The Runge-Kutta algorithm doesn't allow for calculating multi-valued solutions, and, for this reason, multi-valued solutions are not represented by the generated graph and there are no outputted text files with their values.

---

## The Physics

The model solves the momentum equation for the isothermal stellar wind, expressed as a first-order differential equation:

$$ \Large \frac{1}{v} \frac{dv}{dr} = \frac{\frac{2a^2}{r} - \frac{GM}{r^2}}{v^2 - a^2} $$

where:

- $\Large v$ is the wind velocity
- $\Large r$ is the radial distance from the center of the star
- $\Large G$ is the gravitational constant
- $\Large M$ is the mass of the star
- $\Large a$ is the isothermal speed of sound, defined by:

$$ \Large a = \sqrt{\frac{\mathcal{R} T}{\mu}} $$

where:

- $\Large \mathcal{R}$ is the universal gas constant
- $\Large \mu$ is the mean atomic weight of the particles expressed in units of mass of a mole of hydrogen
- $\Large T$ is the temperature of the star
  
The code uses values typical for the sun, but these parameters can be modified within the `stellar_physics.py` file to model different stars. The package can return results either normalized or raw using International System units (km and km/s).

---

## File Structure

The project is organized into a modular structure for clarity and maintainability:
```
rk4-wind-solution/ 
├── main.py 
└── scripts/ 
    ├── init.py 
    ├── rk4_solver.py 
    ├── plot_output.py 
    └── stellar_physics.py 
```
- **main.py**: The entry point for the program. It handles user input and orchestrates the calls to the other scripts.
- **rk4_solver.py**: Contains the RK4 function, a fourth-order Runge-Kutta numerical solver used to integrate the ordinary differential equation.
- **stellar_physics.py**: Contains the physical constants, the differential equation for the solar wind, and the logic for generating the six different solutions.
- **plot_output.py**: Handles all the output, including generating the plot and creating text files for each solution.

---

## Getting Started

### Prerequisites

To run the Python script, you will need to have the following libraries installed:

- **NumPy**: For numerical computations.
- **Matplotlib**: For plotting the results.

You can install these dependencies using pip:

```bash
pip install numpy matplotlib
```
### Running the Code
1. Clone this repository to your local machine:

```bash
git clone https://github.com/indigodrigo/rk4-wind-solution.git
cd rk4-wind-solution
```
2. Run the main Python script from your terminal:

```bash
python main.py
```
3. The program will ask if you want normalized or raw results. Type Y for normalized (v/a and r/R_c) or N for raw (km/s and km) and press Enter. A plot will be displayed, and text files containing the data for each solution will be generated.

---

### Source
The main source of information about the physics of stellar winds for this project was the book Introduction to Stellar Winds by Henny J.G.L.M Lamers and Joseph P. Casinelli.

---
### License
This project is licensed under the Apache 2.0 License.

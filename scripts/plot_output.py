import matplotlib.pyplot as plt

def plot_solutions(solutions, Rc, a, is_normalized):
    """
    Plots the solutions using values based on the user's preference (normalized or raw values)

    Args:
        solution: Dictionary with the data from each solution. (returned by isothermal_wind_solutions())
        Rc: The critical radius. (returned by isothermal_wind_solutions())
        a: The isothermal speed of sound. (returned by isothermal_wind_solutions())
        
        is_normalized: Boolean value that determines whether to use raw or normalized values. (Returned by user input)
    """
    plt.figure(figsize=[10, 10])
    
    conversion_factor = 1000.0
    
    # Defines axis labels and values to be used as limits when plotting
    if is_normalized:                               # normalized values
        x_min, x_max = 0, 5
        y_min, y_max = 0, 4
        x_label = r'Raio ($\frac{r}{R_c}$)'
        y_label = r'Velocidade ($\frac{v}{a}$)'
    else:                                           # raw values converted to km and km/s
        x_min, x_max = 0, 5 * Rc / conversion_factor
        y_min, y_max = 0, 4 * a / conversion_factor
        x_label = 'Raio (r) km'
        y_label = 'Velocidade (v) km/s'
    
    # Dictionary defining the colors and legend text for each solution
    plot_styles = {
        'Transonic subsonic': {'color': 'b', 'label': 'Transonic subsonic -> supersonic'},
        'Transonic supersonic': {'color': 'r', 'label': 'Transonic supersonic -> subsonic'},
        'Non-transonic subsonic solution I': {'color': 'g', 'label': 'Non-transonic subsonic solution I'},
        'Non-transonic subsonic solution II': {'color': 'c', 'label': 'Non-transonic subsonic solution II'},
        'Non-transonic supersonic solution I': {'color': 'm', 'label': 'Non-transonic supersonic solution I'},
        'Non-transonic supersonic solution II': {'color': 'y', 'label': 'Non-transonic supersonic solution II'}
    }

    # Iterates over each solution, picking only the values within the limits determined previously, and plots them.
    for name, data in solutions.items():
        if is_normalized:
            r_data = [r / Rc for r in data['r']]
            v_data = [v / a for v in data['v']]
        else:
            r_data = [r / conversion_factor for r in data['r']]   # raw data converted to km
            v_data = [v / conversion_factor for v in data['v']]   # raw data converted to km/s
        
        clipped_r = []
        clipped_v = []
        
        for r_val, v_val in zip(r_data, v_data):
            # The condition below selects only the values within the limits
            if x_min <= r_val <= x_max and y_min <= v_val <= y_max:
                clipped_r.append(r_val)
                clipped_v.append(v_val)
        
        plt.plot(
            clipped_r, 
            clipped_v, 
            plot_styles[name]['color'] + '.', 
            markersize='1.1', 
            label=plot_styles[name]['label']
        )
    
    # Draws a marker over the sonic point (1,1) along with a textual indication
    if is_normalized:
        plt.plot(1, 1, 'ko', markersize=8)
        plt.text(1.08, 0.96, 'Sonic Point', ha='left', va='bottom', fontsize=11)
    else:
        plt.plot(Rc / conversion_factor, a / conversion_factor, 'ko', markersize=8)
        plt.text(Rc / conversion_factor * 1.08, a / conversion_factor * 0.96, 'Sonic Point', ha='left', va='bottom', fontsize=11)

    # Defines the axis limits
    plt.xlim(x_min, x_max)
    plt.ylim(y_min, y_max)
    
    plt.title('Solutions to the Momentum Equation of an Isothermal Wind')
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.grid(True)
    plt.legend(markerscale=10)
    plt.savefig("isothermal_wind_solutions.png", format="png")
    plt.show()

def generate_text_files(solutions, Rc, a, is_normalized):
    """
    Generates a separate text file with the values of "r" and "v" for each solution.
    
    Args:
        solution: Dictionary with the data from each solution. (returned by isothermal_wind_solutions())
        Rc: The critical radius. (returned by isothermal_wind_solutions())
        a: The isothermal speed of sound. (returned by isothermal_wind_solutions())
        
        is_normalized: Boolean value that determines whether to use raw or normalized values. (Returned by user input)
    """
    conversion_factor = 1000.0
    
    for name, data in solutions.items():
        filename = f"{name.replace(' ', '_').replace('->', 'to')}.txt"
        with open(filename, 'w') as f:
            if is_normalized:                       # normalized values
                f.write("r/R_c v/a\n")            # writes the column headers (normalized)
                # Normalizes the values before writing them to the files
                normalized_r = [r / Rc for r in data['r']]
                normalized_v = [v / a for v in data['v']]
                
                # Rounds eventual negative values to zero (this occurs as a consequence of the RK4 integration method when computing values near zero)
                for i in range(len(normalized_v)):
                    if normalized_v[i] < 0:
                        normalized_v[i] = 0.0

                # Writes the normalized values to two separate columns in the text file
                for r_val, v_val in zip(normalized_r, normalized_v):
                    f.write(f"{r_val:.6e} {v_val:.6e}\n")
            else:
                f.write("r(km) v(km/s)\n")               # writes the column headers (raw)
                
                # Rounds eventual negative values to zero (this occurs as a consequence of the RK4 integration method when computing values near zero)
                v_raw = list(data['v']) # Create a mutable copy
                for i in range(len(v_raw)):
                    if v_raw[i] < 0:
                        v_raw[i] = 0.0
                        
                # Writes the raw values to two separate columns in the text file
                for r_val, v_val in zip(data['r'], v_raw):
                    f.write(f"{r_val / conversion_factor:.6e} {v_val / conversion_factor:.6e}\n")
        print(f"Solution data '{name}' saved to '{filename}'")
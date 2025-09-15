def RK4(ODE, x_initial, y_initial, x_final, n):
    """
    Fourth order Runge-Kutta solver for ODEs.
    It calculates the next step in a curve based on the current and previous values of the slope.

    Args:
        ODE: The RIGHT side of the ODE.
        x_initial: Initial value of the independent variable.
        y_initial: Initial value of the dependent variable.
        x_final: Final value of the independent variable.
        n (int): The number of steps to be used in the numerical integration.

    """
    x_values = [x_initial]
    y_values = [y_initial]
    h = (x_final - x_initial) / n

    for _ in range(n):

        current_x = x_values[-1]    # Attributes the last value in x_values to current_x
        current_y = y_values[-1]    # Attributes the last value in y_values to current_y

        k1 = h * ODE(current_x, current_y)
        k2 = h * ODE(current_x + 0.5 * h, current_y + 0.5 * k1)
        k3 = h * ODE(current_x + 0.5 * h, current_y + 0.5 * k2)
        k4 = h * ODE(current_x + h, current_y + k3)
        
        # Attributes the newfound values of x and y to x_values and y_values, respectively
        y_values.append(current_y + (k1 + 2 * k2 + 2 * k3 + k4) / 6)
        x_values.append(current_x + h)
        
    return x_values, y_values
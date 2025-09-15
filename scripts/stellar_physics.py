from math import sqrt
from .rk4_solver import RK4

def isothermal_wind_solutions():
    """
    Utilizes the RK4 script to calculate different solutions to the momentum equation of an isothermal wind.

    Returns:
        solutions: A dictionary with the solutions for each curve (two columns with coordinates for r and v)
        Rc: The critical radius.
        a: The isothermal speed of sound.
    """
    # Physical constants of the Sun in the International System
    G = 6.674e-11   # Gravitational constant (m3 kg-1 s-2)
    M = 1.989e30    # Mass of the star (kg)
    R = 8.314       # Universal gas constant (J K-1 mol-1)
    T = 5772        # Temperature (Kelvin)
    R0 = 6.957e8    # Radius of the star (m)
    
    # u is the mean molecular weight in kg/mol of the plasma of the solar corona.
    # u (0.6) must be multiplied by the molar mass of H (1.008 g/mol = 1.008e-3 kg/mol), because it is expressed in units of mass of a mole of hydrogen.
    # As such, the value of u is given by "molar_mass_u" below
    molar_mass_u = 0.0006 # (kg/mol)
    
    # Conversion factor from m to km and m/s to km/s
    conversion_factor = 1000.0
    
    # Calculated values
    a = sqrt((R * T) / molar_mass_u)    # Isothermal speed of sound
    Rc = (G * M) / (2 * (a**2))     # Critical radius
    n = 50000       # number of steps to be used as an arg in the function RK4
    x_final = 5 * Rc      # Final value of the independent variable to be used as an arg in the function RK4

    # The right side of the momentum equation of an isothermal wind. Will be used as the "ODE" arg in the RK4 function
    def solar_wind_ode(r, v):
        numerator = v * ((2 * a**2) / r - (G * M) / r**2)
        denominator = v**2 - a**2
        
        # This avoids the case in which the denominator is infinitesimally close to 0.
        if abs(denominator) < 1e-12:
            return 0.0
        return numerator / denominator

    solutions = {}
    
    # Transonic Solutions
    
    # Transonic wind solution (subsonic start)
    r_tsonic_sub_inward, v_tsonic_sub_inward = RK4(solar_wind_ode, Rc, a * (1 - 1e-6), R0, n)
    r_tsonic_sub_inward.reverse(); v_tsonic_sub_inward.reverse()
    r_tsonic_sub_outward, v_tsonic_sub_outward = RK4(solar_wind_ode, Rc, a * (1 + 1e-6), x_final, n)
    solutions['Transonic subsonic'] = {'r': r_tsonic_sub_inward[:-1] + r_tsonic_sub_outward, 'v': v_tsonic_sub_inward[:-1] + v_tsonic_sub_outward}

    # Transonic wind solution (supersonic start)
    r_tsonic_sup_inward, v_tsonic_sup_inward = RK4(solar_wind_ode, Rc, a * (1 + 1e-6), R0, n)
    r_tsonic_sup_inward.reverse(); v_tsonic_sup_inward.reverse()
    r_tsonic_sup_outward, v_tsonic_sup_outward = RK4(solar_wind_ode, Rc, a * (1 - 1e-6), x_final, n)
    solutions['Transonic supersonic'] = {'r': r_tsonic_sup_inward[:-1] + r_tsonic_sup_outward, 'v': v_tsonic_sup_inward[:-1] + v_tsonic_sup_outward}

    
    # Non-transonic solutions

    # Subsonic solutions
    
    r_ntsonic_sub_inward, v_ntsonic_sub_inward = RK4(solar_wind_ode, Rc, a * 0.75, R0, n)
    r_ntsonic_sub_inward.reverse(); v_ntsonic_sub_inward.reverse()
    r_ntsonic_sub_outward, v_ntsonic_sub_outward = RK4(solar_wind_ode, Rc, a * 0.75, x_final, n)
    solutions['Non-transonic subsonic solution I'] = {'r': r_ntsonic_sub_inward[:-1] + r_ntsonic_sub_outward, 'v': v_ntsonic_sub_inward[:-1] + v_ntsonic_sub_outward}

    r_ntsonic_sub_inward_2, v_ntsonic_sub_inward_2 = RK4(solar_wind_ode, Rc, a * 0.4, R0, n)
    r_ntsonic_sub_inward_2.reverse(); v_ntsonic_sub_inward_2.reverse()
    r_ntsonic_sub_outward_2, v_ntsonic_sub_outward_2 = RK4(solar_wind_ode, Rc, a * 0.4, x_final, n)
    solutions['Non-transonic subsonic solution II'] = {'r': r_ntsonic_sub_inward_2[:-1] + r_ntsonic_sub_outward_2, 'v': v_ntsonic_sub_inward_2[:-1] + v_ntsonic_sub_outward_2}

    
    # Supersonic solutions
    
    r_ntsonic_sup_inward, v_ntsonic_sup_inward = RK4(solar_wind_ode, Rc, a * 1.25, R0, n)
    r_ntsonic_sup_inward.reverse(); v_ntsonic_sup_inward.reverse()
    r_ntsonic_sup_outward, v_ntsonic_sup_outward = RK4(solar_wind_ode, Rc, a * 1.25, x_final, n)
    solutions['Non-transonic supersonic solution I'] = {'r': r_ntsonic_sup_inward[:-1] + r_ntsonic_sup_outward, 'v': v_ntsonic_sup_inward[:-1] + v_ntsonic_sup_outward}

    r_ntsonic_sup_inward_2, v_ntsonic_sup_inward_2 = RK4(solar_wind_ode, Rc, a * 1.6, R0, n)
    r_ntsonic_sup_inward_2.reverse(); v_ntsonic_sup_inward_2.reverse()
    r_ntsonic_sup_outward_2, v_ntsonic_sup_outward_2 = RK4(solar_wind_ode, Rc, a * 1.6, x_final, n)
    solutions['Non-transonic supersonic solution II'] = {'r': r_ntsonic_sup_inward_2[:-1] + r_ntsonic_sup_outward_2, 'v': v_ntsonic_sup_inward_2[:-1] + v_ntsonic_sup_outward_2}
      
    print(f"Stellar radius (R0): {R0/conversion_factor:.2e} km")
    print(f"Isothermal speed of sound (a): {a/conversion_factor:.2e} km/s")
    print(f"Critical Radius (Rc): {Rc/conversion_factor:.2e} km")
    print("-" * 20)


    return solutions, Rc, a

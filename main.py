from stellar_physics import isothermal_wind_solutions
from plot_output import plot_solutions, generate_text_files

if __name__ == "__main__":
    
    while True:
        normalization_choice = input("Would you like the normalized results? Y (Yes) or N (No) ").upper()
        if normalization_choice in ['Y', 'N']:
            break
        print("Invalid option. Please, type 'Y' or 'N'.")
        
    is_normalized = normalization_choice == 'Y'
    
    # Calls the main function that calculates the solutions
    calculated_solutions, Rc_val, a_val = isothermal_wind_solutions()

    # Generates the text files for each solution
    generate_text_files(calculated_solutions, Rc_val, a_val, is_normalized)
    
    # Plots the solutions
    plot_solutions(calculated_solutions, Rc_val, a_val, is_normalized)
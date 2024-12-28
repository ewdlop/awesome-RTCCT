import numpy as np
import matplotlib.pyplot as plt

# Constants
R = 8.314  # Gas constant in J/(mol·K)
delta_H = -50000  # Standard enthalpy change in J/mol (exothermic reaction)
delta_S = -100  # Standard entropy change in J/(mol·K)

def equilibrium_constant(T):
    """
    Calculate the equilibrium constant K_eq at temperature T using the van 't Hoff equation.
    
    Parameters:
    T (float): Temperature in Kelvin

    Returns:
    float: Equilibrium constant K_eq
    """
    return np.exp(-delta_H / (R * T) + delta_S / R)

# Temperature range from 250 K to 350 K
temperatures = np.linspace(250, 350, 100)
K_eq_values = equilibrium_constant(temperatures)

# Plot the equilibrium constant as a function of temperature
plt.figure(figsize=(8, 6))
plt.plot(temperatures, K_eq_values, label='Equilibrium Constant (K_eq)')
plt.xlabel('Temperature (K)')
plt.ylabel('Equilibrium Constant (K_eq)')
plt.title('Temperature Dependence of Equilibrium Constant')
plt.legend()
plt.grid(True)
plt.show()

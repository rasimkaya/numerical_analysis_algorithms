import numpy as np
import matplotlib.pyplot as plt

def bisection_method(func, a, b, tol=None, max_iter=None):
    if tol is None and max_iter is None:
        max_iter = int(input("Enter the maximum number of iterations: "))

    # Check if the initial interval is valid
    if func(a) * func(b) > 0:
        raise ValueError("No root found in the given interval. f(a) and f(b) must have opposite signs.")
    
    print(f"\nf({a}) = {func(a):.6f} , f({b}) = {func(b):.6f}")
    print(f"A root exists in [{a}, {b}] because f({a}) * f({b}) < 0\n")

    iteration = 0
    c = a
    
    while True:
        c = (a + b) / 2
        fa, fb, fc = func(a), func(b), func(c)
        current_error = abs(b - a) / 2

        print(f"--- Iteration {iteration + 1} ---")
        print(f"a = {a:.6f}, f(a) = {fa:.6f}")
        print(f"b = {b:.6f}, f(b) = {fb:.6f}")
        print(f"c = (a + b) / 2 = {c:.6f}, f(c) = {fc:.6f}")
        print(f"Error = {current_error:.6f}\n")

        # Convergence check
        if fc == 0 or (tol is not None and current_error < tol):
            print("Root found successfully.")
            break

        # Max iteration check
        if max_iter is not None and (iteration + 1) >= max_iter:
            print("Maximum iterations reached. Returning the best approximation.")
            break

        # Update intervals
        if fa * fc < 0:
            b = c
            print(f"Since f(a) * f(c) < 0, the new interval is [{a:.6f}, {b:.6f}]\n")
        else:
            a = c
            print(f"Since f(b) * f(c) < 0, the new interval is [{a:.6f}, {b:.6f}]\n")

        iteration += 1

    return c, iteration + 1

def plot_function(func, a, b, root, equation_str):
    """Generates a plot of the function, the interval, and the found root."""
    # Create an array of x values for plotting, with a margin around [a, b]
    margin = abs(b - a) * 0.5
    x_vals = np.linspace(a - margin, b + margin, 400)
    y_vals = func(x_vals)

    plt.figure(figsize=(10, 6))
    plt.plot(x_vals, y_vals, label=f"f(x) = {equation_str}", color='#1f77b4', linewidth=2)
    plt.axhline(0, color='black', linewidth=1, linestyle='--') # x-axis

    # Mark the initial interval [a, b]
    plt.axvline(a, color='#d62728', linestyle=':', label=f'Interval Start (a={a})')
    plt.axvline(b, color='#2ca02c', linestyle=':', label=f'Interval End (b={b})')

    # Mark the root
    plt.scatter([root], [func(root)], color='#9467bd', s=100, zorder=5, label=f'Root ≈ {root:.5f}')

    plt.title("Bisection Method Visualization", fontsize=14, fontweight='bold')
    plt.xlabel("x", fontsize=12)
    plt.ylabel("f(x)", fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    print("=== Bisection Method Root Finder ===")
    
    # 1. Error Tolerance Selection
    tol_choice = input("Do you want to use an error tolerance? (1: Yes, 2: No): ")
    
    tol = None
    max_iter = None
    
    if tol_choice == '1':
        tol_input = input("Enter the error tolerance (e.g., 1e-5 or 0.0001): ")
        tol = float(eval(tol_input))
        if tol < 0:
            raise ValueError("Error tolerance cannot be negative.")
    elif tol_choice == '2':
        max_iter = int(input("Enter the maximum number of iterations: "))
    else:
        raise ValueError("Invalid selection. Please run the script again.")

    # 2. Interval Input
    print("\nEnter the initial interval [a, b]:")
    a = float(input("a: "))
    b = float(input("b: "))

    # 3. Equation Input
    equation_str = input("\nEnter the equation (e.g., 3*x + sin(x) - exp(x)): ")

    # Use NumPy's mathematical functions for safe evaluation and vectorized plotting
    allowed_funcs = {
        'x': None, # will be replaced during evaluation
        'sin': np.sin, 'cos': np.cos, 'tan': np.tan,
        'exp': np.exp, 'log': np.log, 'log10': np.log10,
        'sqrt': np.sqrt, 'pi': np.pi, 'e': np.e
    }

    def func(x):
        allowed_funcs['x'] = x
        return eval(equation_str, {"__builtins__": None}, allowed_funcs)

    # 4. Execution and Plotting
    try:
        root, total_iterations = bisection_method(func, a, b, tol=tol, max_iter=max_iter)
        
        print("-" * 30)
        print(f"Final Root: {root:.8f}")
        print(f"Total Iterations: {total_iterations}")
        print("-" * 30)
        
        print("Generating plot...")
        plot_function(func, a, b, root, equation_str)
        
    except Exception as e:
        print(f"An error occurred: {e}")
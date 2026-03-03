import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
import sys

def newton_raphson(f_callable, df_callable, x0, max_iter=10, tol=1e-8):
    """
    Finds the root of a function using the Newton-Raphson method.
    Formula: x_{n+1} = x_n - f(x_n) / f'(x_n)
    """
    x_n = x0
    print("\n--- Newton-Raphson Iterations ---")
    
    for i in range(max_iter):
        f_x = f_callable(x_n)
        df_x = df_callable(x_n)
        
        if df_x == 0:
            print(f"Error: Derivative became zero at iteration {i+1}. Stopping.")
            return None
            
        x_next = x_n - (f_x / df_x)
        print(f"Iteration {i + 1}: x_{i+1} = {x_n:.6f} - ({f_x:.6f}) / ({df_x:.6f}) = {x_next:.15f}")
        
        # Convergence check
        if abs(x_next - x_n) < tol:
            print(f"\n✅ Converged to root after {i + 1} iterations.")
            return x_next
            
        x_n = x_next
        
    print(f"\n⚠️ Maximum iterations ({max_iter}) reached without full convergence.")
    return x_n

def plot_function(f_callable, root, x0):
    """
    Plots the function, the root, and the starting point.
    """
    # Create a dynamic range for the x-axis based on the root and start point
    margin = max(abs(root - x0) * 1.5, 2)
    x_vals = np.linspace(min(root, x0) - margin, max(root, x0) + margin, 400)
    y_vals = f_callable(x_vals)
    
    plt.figure(figsize=(10, 6))
    
    # Plot the main function
    plt.plot(x_vals, y_vals, label="f(x)", color="#239120", linewidth=2)
    plt.axhline(0, color='black', linewidth=1)  # x-axis
    
    # Plot the starting point and the found root
    plt.scatter([x0], [f_callable(x0)], color="blue", zorder=5, label=f"Start (x0 = {x0})")
    plt.scatter([root], [0], color="red", zorder=5, label=f"Root (x = {root:.4f})")
    
    # Annotate the root
    plt.annotate(f"{root:.4f}", (root, 0), textcoords="offset points", xytext=(0,10), ha='center', color="red")

    plt.title("Newton-Raphson Method Visualization", fontsize=14, fontweight='bold')
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()
    plt.tight_layout()
    plt.show()

def main():
    print("=== Newton-Raphson Root Finder ===")
    user_input = input("Enter the function (e.g., x**2 - 4, exp(x) - sin(x) - 3*x): \n> ")
    
    try:
        x0 = float(input("Enter the starting value (x0): \n> "))
        max_iter = int(input("Enter maximum iterations: \n> "))
    except ValueError:
        print("Error: Please enter valid numerical values for starting point and iterations.")
        sys.exit(1)

    # Core Symbolic Operations
    x_sym = sp.Symbol('x')
    
    try:
        # sympify safely converts string to a mathematical expression
        f_expr = sp.sympify(user_input)
        df_expr = sp.diff(f_expr, x_sym)
        print(f"\nCalculated Derivative: {df_expr}")
        
        # lambdify converts sympy expressions to fast numpy-compatible functions
        f_callable = sp.lambdify(x_sym, f_expr, modules=['numpy', 'sympy'])
        df_callable = sp.lambdify(x_sym, df_expr, modules=['numpy', 'sympy'])
        
    except Exception as e:
        print(f"Error processing the function: {e}")
        sys.exit(1)

    # Execute Algorithm
    root = newton_raphson(f_callable, df_callable, x0, max_iter)

    # Plotting
    if root is not None:
        print(f"Final Result: Root = {root}")
        plot_function(f_callable, root, x0)

if __name__ == "__main__":
    main()
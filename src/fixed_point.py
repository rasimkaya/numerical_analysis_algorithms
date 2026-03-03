"""
Fixed-Point Iteration Method Solver
Author: raska
Description: A robust numerical method script to find the fixed point of a given function.
Designed for both educational purposes and mathematical modeling.
"""

import math

def get_function():
    """Prompts the user to input a valid mathematical function."""
    while True:
        func_str = input("Enter the function for iteration (e.g., 'math.exp(-x)' or 'x**2 - 2*x - 3'): ")
        try:
            # Compiling the string into a code object for safe evaluation
            code = compile(func_str, "<string>", "eval")
            
            # Restricting the environment for security
            safe_env = {"__builtins__": None, "math": math}
            
            # Test the function with a dummy variable to ensure it works
            test_func = lambda x: eval(code, {"x": x, **safe_env})
            test_func(1.0) # Dry run
            
            return test_func, func_str
        except Exception as e:
            print(f"Error parsing function: {e}. Please check your syntax and try again.")

def get_float_input(prompt):
    """Handles float inputs robustly."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def get_int_input(prompt):
    """Handles integer inputs robustly."""
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("Value must be greater than zero.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def fixed_point_iteration():
    """Main function to execute the fixed-point iteration algorithm."""
    print("="*50)
    print("   Fixed-Point Iteration Solver - Developed by raska   ")
    print("="*50)

    f, func_str = get_function()
    p0 = get_float_input("Enter the initial guess (p0): ")
    max_iter = get_int_input("Enter the maximum number of iterations: ")
    
    # Adding a tolerance parameter for mathematical precision
    tol_input = input("Enter the tolerance for convergence (e.g., 1e-6) or press Enter to skip: ")
    tol = float(tol_input) if tol_input.strip() else 0.0

    print(f"\n--- Starting Iteration for f(x) = {func_str} ---")
    print(f"Initial guess (p0): {p0}")
    
    p_prev = p0
    for i in range(1, max_iter + 1):
        try:
            p_next = f(p_prev)
            print(f"Iteration {i:02d}: p = {p_next:.8f}")
            
            # Stopping criteria: if the difference is smaller than tolerance
            if tol > 0 and abs(p_next - p_prev) < tol:
                print(f"\n✅ Converged successfully to {p_next:.8f} after {i} iterations.")
                return
            
            p_prev = p_next
            
        except OverflowError:
            print("\n❌ Error: Math overflow. The function might be diverging.")
            return
        except Exception as e:
            print(f"\n❌ Error during calculation: {e}")
            return

    print(f"\n⚠️ Reached maximum iterations ({max_iter}) without strict convergence.")
    print(f"Final approximated value: {p_prev:.8f}")

if __name__ == "__main__":
    fixed_point_iteration()
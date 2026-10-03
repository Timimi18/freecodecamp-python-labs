# Description: Employs binary boundary convergence (Bisection Method) to approximate numerical square roots down to minor tolerances.
def square_root_bisection(number, tolerance=1e-7, max_iterations=100):
    if number < 0:
        raise ValueError("Square root of negative number is not defined in real numbers")
        
    if number == 0 or number == 1:
        print(f"The square root of {number} is {number}")
        return number

    if number < 1:
        low = number
        high = 1.0
    else:
        low = 0.0
        high = number

    for iteration in range(max_iterations):
        mid = (low + high) / 2.0
        square = mid * mid
        
        if (high - low) <= tolerance:
            print(f"The square root of {number} is approximately {mid}")
            return mid
            
        if square < number:
            low = mid
        else:
            high = mid
            
    print(f"Failed to converge within {max_iterations} iterations")
    return None

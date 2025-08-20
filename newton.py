def calc_derivative(f, x, eps):
    """
    Calculate Derivative.

    This function calculates the derivative of a function at a given point using a Newton approximation method.

    Parameters:
    f: function to calculate derivative of
    x: (numeric) point to calculate derivative at
    eps: (numeric) step size

    Return:
    (numeric): derivative of f at value x
    """
    return (f(x + eps) - f(x)) / eps

def optimize(x0, f, eps=0.001, threshold=0.0001):
    """
    Calculates the minimum of a function using a Newton approximation method.

    Parameters:
    x0: (numeric) initial value of Newton's method algorithm
    f: (func) function to find minimum of
    eps: (numeric) step size
    threshold: (numeric) stopping condition, stops when step size < threshold

    Return: (dict) 2-element dictionary containing the x-value of the optimum at "x_val" and the y-value at "func_val"
    """
    diff = 10000
    xt = x0
    # Wow this code is so awesome!!!
    while diff > threshold:
        xt_prev = xt
        first_deriv = calc_derivative(f, xt, eps)
        second_deriv = (calc_derivative(f, xt + eps, eps) - first_deriv) / eps
        xt = xt - first_deriv / second_deriv
        diff = abs(xt - xt_prev)
    return {"x_val": xt, "func_val": f(xt)}

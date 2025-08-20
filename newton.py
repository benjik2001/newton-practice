def deriv(f, x, eps):
    return (f(x + eps) - f(x)) / eps

def optimize(x0, f, eps = 0.01, threshold = 0.0001):
    diff = 10000
    xt = x0
    while diff > threshold:
        xt_prev = xt
        first_deriv = deriv(f, xt, eps)
        second_deriv = (deriv(f, xt + eps, eps) - first_deriv) / eps
        # second_deriv = deriv(deriv, xt, eps)
        xt = xt - first_deriv/second_deriv
        diff = abs(xt - xt_prev)
    return (xt, f(xt))
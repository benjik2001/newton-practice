import numdifftools as nd
import numpy as np

def optimize(x_0, f, eps=1e-4, tol=1e-5):
    x_t = x_0
    dist = tol + 1
    while dist > tol:
        x_prev = x_t
        hessian = nd.Hessian(f)(x_t)
        gradient = nd.Gradient(f)(x_t)
        x_t = x_t - np.matmul(np.linalg.inv(hessian), gradient)
        dist = np.linalg.norm(x_t - x_prev)
    return {
        "x_val": x_t,
        "func_val": f(x_t)
    }
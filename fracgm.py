import numpy as np
from scipy.optimize import minimize_scalar

class FracGM:
    """ 
    FracGM solver for the optimization problem
    min x^2 / (x^2 + 1),
    where the optimal solution is x* = 0.
    """
    def __init__(self, max_iteration=10, tolerance=1e-7, verbose=False):
        
        self.max_iter = max_iteration
        self.tol = tolerance

        self.verbose = verbose

    @staticmethod
    def f(x):
        return x**2
    
    @staticmethod
    def h(x):
        return x**2 + 1

    def solve_beta_mu(self, x):
        "Solve beta & mu by a linear system."
        beta = self.f(x)/self.h(x)
        mu = 1/self.h(x)
        return beta, mu

    def solve_x(self, beta, mu):
        "Solve dual problem by Scipy minimizer for scalar function of one variable.."
        def dual_problem(x):
            return mu*(x**2 - beta*(x**2 + 1)) 

        res = minimize_scalar(dual_problem)

        return res.x

    def compute_psi_norm(self, beta, mu, x):
        "Compute the norm of psi for stopping criteria."
        psi_1 = -self.f(x) + beta*self.h(x)
        psi_2 = -1 + mu*self.h(x)
        return np.linalg.norm([psi_1, psi_2])

    def solve(self, initial):

        if self.verbose:
            print("initial guess:", initial)

        x = initial

        for i in range(self.max_iter):  
            if not i:
                beta, mu = self.solve_beta_mu(x)
            else:
                x = self.solve_x(beta, mu)
                beta, mu = self.solve_beta_mu(x)
                # stopping criteria
                norm = self.compute_psi_norm(beta, mu, x)
                if norm < self.tol:
                    break

        if self.verbose:
            print("solution:", x)
        return x
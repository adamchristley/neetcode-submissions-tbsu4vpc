class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        x = float(init)
        if iterations == 0:
            return round(x)
        else:
            for _ in range(iterations):
                grad = 2 * x
                x = x - grad * learning_rate
            return round(x, 5)

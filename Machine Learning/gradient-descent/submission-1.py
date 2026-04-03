class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        grad = init

        for _ in range(iterations):
            derivative = 2 * grad
            grad = grad - learning_rate * derivative
        return round(grad, 5)
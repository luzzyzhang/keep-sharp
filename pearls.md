# Pearls

1. [Beautiful use case of `enumerate()`](https://www.quora.com/What-are-the-uses-of-the-enumerate-function-on-Python)
    ```python
    def polynomial(x, coefficients):
        return sum(c * x ** i for (i, c) in enumerate(coefficients))
    r = polynomial(2, [10, 3, 4])
    ```

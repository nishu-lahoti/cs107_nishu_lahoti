# Exercise 1

| Trace | Elementary Operation | Numerical Value | derivative of elementary function | value in respect to x | value in respect to y |
| :------: | :----------------------: | :------------------------------: | :------: | :------: | :------: |
| x1 | x | pi/2 | x1. | 1 | 0 |
| x2 | y | pi/3 | x2. | 0 | 1 |
| v2 | sin(x1) | 1 | cos(x1)*x1. | 0 | 0 |
| v3 | -cos(x2) | -0.5 | sin(x2)*x2. | 0 | sqrt(3)/2 |
| v4 | v3 + v2 | 0.5 |  v2. + v3. | 0 | sqrt(3)/2 |
| v5 | v4^2 | 1/4 | 2\* v4 \* v4. |0  | .5 * sqrt(3)/2 | 
| v6 | -v5 | 1/4 | -v5. | 0 |- .5 * sqrt(3)/2 | 
| v7 | exp(v6) | e^(-.5^2) | exp(v6)\*v6.  | 0 | e^(1.5^2) * - .5 * sqrt(3)/2 | 

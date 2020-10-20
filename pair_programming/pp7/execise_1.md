# First function x^2 + y^2
| Trace Position | Current Operation | Function Value | Derivative         | Derivative Value (x) | Derivative Value (y) |
|----------------|-------------------|----------------|--------------------|----------------------|----------------------|
| x1             |     x1            |        1       |      x1_dot        |          1           |         1            |
| x2             |     x2            |        1       |      x2_dot        |         -2           |         1            |
| v1             |     x^2           |        1       |     2x*x_dot       |          2           |         2            |
| v2             |     y^2           |        1       |     2y*y_dot       |         -4           |         2            |
| f1             |     v1+v2         |        2       |   v1_dot+v2_dot    |         -2           |         4            |

# Second function e^(x+y)
| Trace Position | Current Operation | Function Value | Derivative         | Derivative Value (x) | Derivative Value (y) |
|----------------|-------------------|----------------|--------------------|----------------------|----------------------|
| x1             |     x1            |        1       |      x1_dot        |          1           |         1            |
| x2             |     x2            |        1       |      x2_dot        |         -2           |         1            |
| v1             |     x+y           |        2       |    x_dot + y_dot   |         -1           |         2            |
| f2             |     e^(v1)        |      e^2       |     v1_dot*e^(v1)  |        -e^2          |       2*e^2          |
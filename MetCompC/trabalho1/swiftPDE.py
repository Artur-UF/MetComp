import pde

grid = pde.CartesianGrid([[0, 50], [0, 50]], [0, 1], periodic=[True, True])
state = pde.ScalarField.random_uniform(grid)

import pde
import tqdm
import ffmpeg



grid = pde.CartesianGrid([[0, 50], [0, 50]], [50, 50], periodic=[True, True])
state = pde.ScalarField.random_uniform(grid)
eq = pde.PDE({"u": "-gradient_squared(u) / 2 - laplace(u + laplace(u))"})
storage = pde.MemoryStorage()
trackers = ["progress",
            "plot",
            storage.tracker(1),
]
result = eq.solve(state, t_range=10, dt=1e-3, tracker=trackers)
pde.movie(storage, 'KS.gif')


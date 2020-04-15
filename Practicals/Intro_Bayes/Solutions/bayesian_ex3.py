# W L W W W L W L W
data = np.array([1,0,1,1,1,0,1,0,1])

# Make bounded laplace function
bounded_laplace = pm.Bound(pm.Laplace, lower = 0.0, upper = 1.0)

with pm.Model():
    p = bounded_laplace('p', mu = 0.5, b = 0.1) # prior
    k = pm.Binomial('k', n = len(data), p = p, observed = data.sum()) # likelihood
    trace = pm.sample(tune = 2500)

pm.traceplot(trace)
pm.summary(trace)
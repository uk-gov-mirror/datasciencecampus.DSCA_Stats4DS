# W L W W W L W L W
data = np.array([1,0,1,1,1,0,1,0,1])

with pm.Model():
    p = pm.Uniform('p', lower = 0.5, upper = 1) # prior
    k = pm.Binomial('k', n = len(data), p = p, observed = data.sum()) # likelihood
    trace = pm.sample(tune = 1000)

pm.traceplot(trace)
pm.summary(trace)
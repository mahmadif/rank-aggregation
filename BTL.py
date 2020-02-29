def BTL(Data, probs=False, max_iter=10**5):
    '''
    computes the parameters using maximum likelihood principle.
    This function is adapted from the Matlab version provided by David Hunter
    http://personal.psu.edu/drh20/code/btmatlab
    '''
    wm = Data
    if probs:
        np.fill_diagonal(wm, 1)
        wm = wm/(wm+wm.T)
        np.fill_diagonal(wm, 0)
    n = wm.shape[0]
    nmo = n-1
    pi = np.ones(nmo, dtype=float)
    gm = (wm[:,range(nmo)]).T + wm[range(nmo),:]
    wins = np.sum(wm[range(nmo),], axis=1)
    gind = gm>0
    z = np.zeros((nmo,n))
    pisum = z
    for _ in range(max_iter):
        pius = np.repeat(pi, n).reshape(nmo, -1)
        piust = (pius[:,range(nmo)]).T
        piust = np.column_stack((piust, np.repeat(1,nmo)))
        pisum[gind] = pius[gind]+piust[gind]
        z[gind] = gm[gind] / pisum[gind]
        newpi = wins / np.sum(z, axis=1)
        if np.linalg.norm(newpi - pi, ord=np.inf) <= 1e-6:
            newpi = np.append(newpi, 1)
            return newpi/sum(newpi)
        pi = newpi
    raise RuntimeError('did not converge')

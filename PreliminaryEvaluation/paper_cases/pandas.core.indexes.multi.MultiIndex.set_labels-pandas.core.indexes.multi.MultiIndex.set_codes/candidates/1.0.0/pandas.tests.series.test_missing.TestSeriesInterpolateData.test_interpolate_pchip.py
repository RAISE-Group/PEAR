@td.skip_if_no_scipy
def test_interpolate_pchip(self):
    ser = Series(np.sort(np.random.uniform(size=100)))
    new_index = ser.index.union(Index([49.25, 49.5, 49.75, 50.25, 50.5, 50.75])).astype(float)
    interp_s = ser.reindex(new_index).interpolate(method='pchip')
    interp_s[49:51]
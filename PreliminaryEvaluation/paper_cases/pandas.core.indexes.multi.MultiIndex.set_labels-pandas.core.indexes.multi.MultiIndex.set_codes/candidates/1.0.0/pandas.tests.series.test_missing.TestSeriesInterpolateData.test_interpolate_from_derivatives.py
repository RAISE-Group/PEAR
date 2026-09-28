@td.skip_if_no_scipy
def test_interpolate_from_derivatives(self):
    ser = Series([10, 11, 12, 13])
    expected = Series([11.0, 11.25, 11.5, 11.75, 12.0, 12.25, 12.5, 12.75, 13.0], index=Index([1.0, 1.25, 1.5, 1.75, 2.0, 2.25, 2.5, 2.75, 3.0]))
    new_index = ser.index.union(Index([1.25, 1.5, 1.75, 2.25, 2.5, 2.75])).astype(float)
    interp_s = ser.reindex(new_index).interpolate(method='from_derivatives')
    tm.assert_series_equal(interp_s[1:3], expected)
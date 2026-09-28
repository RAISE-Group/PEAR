def test_index_cast_datetime64_other_units(self):
    arr = np.arange(0, 100, 10, dtype=np.int64).view('M8[D]')
    idx = Index(arr)
    assert (idx.values == conversion.ensure_datetime64ns(arr)).all()
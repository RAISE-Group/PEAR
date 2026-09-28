@td.xfail_non_writeable
def test_tuple_index(self, setup_path):
    col = np.arange(10)
    idx = [(0.0, 1.0), (2.0, 3.0), (4.0, 5.0)]
    data = np.random.randn(30).reshape((3, 10))
    DF = DataFrame(data, index=idx, columns=col)
    with catch_warnings(record=True):
        simplefilter('ignore', pd.errors.PerformanceWarning)
        self._check_roundtrip(DF, tm.assert_frame_equal, path=setup_path)
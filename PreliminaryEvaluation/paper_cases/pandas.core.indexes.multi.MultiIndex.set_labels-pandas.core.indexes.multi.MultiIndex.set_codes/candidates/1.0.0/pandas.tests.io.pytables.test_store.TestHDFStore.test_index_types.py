@td.xfail_non_writeable
@pytest.mark.filterwarnings('ignore::pandas.errors.PerformanceWarning')
def test_index_types(self, setup_path):
    with catch_warnings(record=True):
        values = np.random.randn(2)
        func = lambda l, r: tm.assert_series_equal(l, r, check_dtype=True, check_index_type=True, check_series_type=True)
    with catch_warnings(record=True):
        ser = Series(values, [0, 'y'])
        self._check_roundtrip(ser, func, path=setup_path)
    with catch_warnings(record=True):
        ser = Series(values, [datetime.datetime.today(), 0])
        self._check_roundtrip(ser, func, path=setup_path)
    with catch_warnings(record=True):
        ser = Series(values, ['y', 0])
        self._check_roundtrip(ser, func, path=setup_path)
    with catch_warnings(record=True):
        ser = Series(values, [datetime.date.today(), 'a'])
        self._check_roundtrip(ser, func, path=setup_path)
    with catch_warnings(record=True):
        ser = Series(values, [0, 'y'])
        self._check_roundtrip(ser, func, path=setup_path)
        ser = Series(values, [datetime.datetime.today(), 0])
        self._check_roundtrip(ser, func, path=setup_path)
        ser = Series(values, ['y', 0])
        self._check_roundtrip(ser, func, path=setup_path)
        ser = Series(values, [datetime.date.today(), 'a'])
        self._check_roundtrip(ser, func, path=setup_path)
        ser = Series(values, [1.23, 'b'])
        self._check_roundtrip(ser, func, path=setup_path)
        ser = Series(values, [1, 1.53])
        self._check_roundtrip(ser, func, path=setup_path)
        ser = Series(values, [1, 5])
        self._check_roundtrip(ser, func, path=setup_path)
        ser = Series(values, [datetime.datetime(2012, 1, 1), datetime.datetime(2012, 1, 2)])
        self._check_roundtrip(ser, func, path=setup_path)
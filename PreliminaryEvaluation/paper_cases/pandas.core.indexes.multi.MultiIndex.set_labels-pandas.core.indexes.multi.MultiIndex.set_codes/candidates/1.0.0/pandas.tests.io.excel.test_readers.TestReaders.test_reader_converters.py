def test_reader_converters(self, read_ext):
    basename = 'test_converters'
    expected = DataFrame.from_dict(OrderedDict([('IntCol', [1, 2, -3, -1000, 0]), ('FloatCol', [12.5, np.nan, 18.3, 19.2, 5e-09]), ('BoolCol', ['Found', 'Found', 'Found', 'Not found', 'Found']), ('StrCol', ['1', np.nan, '3', '4', '5'])]))
    converters = {'IntCol': lambda x: int(x) if x != '' else -1000, 'FloatCol': lambda x: 10 * x if x else np.nan, 2: lambda x: 'Found' if x != '' else 'Not found', 3: lambda x: str(x) if x else ''}
    actual = pd.read_excel(basename + read_ext, 'Sheet1', converters=converters)
    tm.assert_frame_equal(actual, expected)
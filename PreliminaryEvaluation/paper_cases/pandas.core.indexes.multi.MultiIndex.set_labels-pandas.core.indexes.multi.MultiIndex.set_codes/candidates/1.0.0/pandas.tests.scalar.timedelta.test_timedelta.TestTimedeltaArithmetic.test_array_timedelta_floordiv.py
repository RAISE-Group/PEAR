def test_array_timedelta_floordiv(self):
    ints = pd.date_range('2012-10-08', periods=4, freq='D').view('i8')
    with pytest.raises(TypeError, match='Invalid dtype'):
        ints // Timedelta(1, unit='s')
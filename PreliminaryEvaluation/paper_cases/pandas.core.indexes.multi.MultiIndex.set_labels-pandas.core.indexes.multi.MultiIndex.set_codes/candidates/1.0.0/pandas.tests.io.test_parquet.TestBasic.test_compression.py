@pytest.mark.parametrize('compression', [None, 'gzip', 'snappy', 'brotli'])
def test_compression(self, engine, compression):
    if compression == 'snappy':
        pytest.importorskip('snappy')
    elif compression == 'brotli':
        pytest.importorskip('brotli')
    df = pd.DataFrame({'A': [1, 2, 3]})
    check_round_trip(df, engine, write_kwargs={'compression': compression})
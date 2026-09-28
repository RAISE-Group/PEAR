@pytest.mark.parametrize('to_infer', [True, False])
@pytest.mark.parametrize('read_infer', [True, False])
def test_to_csv_compression(self, compression_only, read_infer, to_infer):
    compression = compression_only
    if compression == 'zip':
        pytest.skip(f'{compression} is not supported for to_csv')
    filename = 'test.'
    if compression == 'gzip':
        filename += 'gz'
    else:
        filename += compression
    df = DataFrame({'A': [1]})
    to_compression = 'infer' if to_infer else compression
    read_compression = 'infer' if read_infer else compression
    with tm.ensure_clean(filename) as path:
        df.to_csv(path, compression=to_compression)
        result = pd.read_csv(path, index_col=0, compression=read_compression)
        tm.assert_frame_equal(result, df)
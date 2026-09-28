def test_filter_row_groups(self, fp):
    d = {'a': list(range(0, 3))}
    df = pd.DataFrame(d)
    with tm.ensure_clean() as path:
        df.to_parquet(path, fp, compression=None, row_group_offsets=1)
        result = read_parquet(path, fp, filters=[('a', '==', 0)])
    assert len(result) == 1
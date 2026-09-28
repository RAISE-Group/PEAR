@pytest.mark.filterwarnings('ignore:\\nthe :pandas.io.pytables.AttributeConflictWarning')
def test_retain_index_attributes2(self, setup_path):
    with ensure_clean_path(setup_path) as path:
        with catch_warnings(record=True):
            df = DataFrame(dict(A=Series(range(3), index=date_range('2000-1-1', periods=3, freq='H'))))
            df.to_hdf(path, 'data', mode='w', append=True)
            df2 = DataFrame(dict(A=Series(range(3), index=date_range('2002-1-1', periods=3, freq='D'))))
            df2.to_hdf(path, 'data', append=True)
            idx = date_range('2000-1-1', periods=3, freq='H')
            idx.name = 'foo'
            df = DataFrame(dict(A=Series(range(3), index=idx)))
            df.to_hdf(path, 'data', mode='w', append=True)
        assert read_hdf(path, 'data').index.name == 'foo'
        with catch_warnings(record=True):
            idx2 = date_range('2001-1-1', periods=3, freq='H')
            idx2.name = 'bar'
            df2 = DataFrame(dict(A=Series(range(3), index=idx2)))
            df2.to_hdf(path, 'data', append=True)
        assert read_hdf(path, 'data').index.name is None
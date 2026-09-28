@pytest.mark.parametrize('idx', [date_range('2019', freq='D', periods=3, tz='UTC'), CategoricalIndex(list('abc'))])
def test_to_hdf_multiindex_extension_dtype(self, idx, setup_path):
    mi = MultiIndex.from_arrays([idx, idx])
    df = pd.DataFrame(0, index=mi, columns=['a'])
    with ensure_clean_path(setup_path) as path:
        with pytest.raises(NotImplementedError, match='Saving a MultiIndex'):
            df.to_hdf(path, 'df')
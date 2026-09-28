@pytest.mark.parametrize('case', [pd.Series([1], index=pd.Index([1], name='a'), name='a'), pd.DataFrame({'A': [1]}, index=pd.Index([1], name='A')), pd.DataFrame({'A': [1]}, index=pd.MultiIndex.from_arrays([['a'], [1]], names=['A', 'a']))])
def test_overlapping_names(self, case):
    with pytest.raises(ValueError, match='Overlapping'):
        case.to_json(orient='table')
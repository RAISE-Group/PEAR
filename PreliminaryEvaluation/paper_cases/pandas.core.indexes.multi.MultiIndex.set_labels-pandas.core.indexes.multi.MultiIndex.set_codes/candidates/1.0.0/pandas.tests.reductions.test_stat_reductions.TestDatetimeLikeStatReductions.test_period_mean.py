@pytest.mark.parametrize('box', [Series, pd.Index, PeriodArray])
def test_period_mean(self, box):
    dti = pd.date_range('2001-01-01', periods=11)
    dti = dti.take([4, 1, 3, 10, 9, 7, 8, 5, 0, 2, 6])
    parr = dti._data.to_period('H')
    obj = box(parr)
    with pytest.raises(TypeError, match='ambiguous'):
        obj.mean()
    with pytest.raises(TypeError, match='ambiguous'):
        obj.mean(skipna=True)
    parr[-2] = pd.NaT
    with pytest.raises(TypeError, match='ambiguous'):
        obj.mean()
    with pytest.raises(TypeError, match='ambiguous'):
        obj.mean(skipna=True)
@pytest.mark.parametrize('cls', [Categorical, CategoricalIndex])
@pytest.mark.parametrize('values', [[1, np.nan], [Timestamp('2000'), pd.NaT]])
def test_cast_nan_to_int(self, cls, values):
    s = cls(values)
    msg = 'Cannot (cast|convert)'
    with pytest.raises((ValueError, TypeError), match=msg):
        s.astype(int)
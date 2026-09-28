def test_only_1dim_accepted(self):
    arr = np.array([0, 1, 2, 3], dtype='M8[h]').astype('M8[ns]')
    with pytest.raises(ValueError, match='Only 1-dimensional'):
        DatetimeArray(arr.reshape(2, 2, 1))
    with pytest.raises(ValueError, match='Only 1-dimensional'):
        DatetimeArray(arr[[0]].squeeze())
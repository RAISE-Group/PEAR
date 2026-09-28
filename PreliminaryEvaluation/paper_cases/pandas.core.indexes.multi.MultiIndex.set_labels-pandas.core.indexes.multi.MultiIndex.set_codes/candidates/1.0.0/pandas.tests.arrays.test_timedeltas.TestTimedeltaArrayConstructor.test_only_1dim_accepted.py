def test_only_1dim_accepted(self):
    arr = np.array([0, 1, 2, 3], dtype='m8[h]').astype('m8[ns]')
    with pytest.raises(ValueError, match='Only 1-dimensional'):
        TimedeltaArray(arr.reshape(2, 2, 1))
    with pytest.raises(ValueError, match='Only 1-dimensional'):
        TimedeltaArray(arr[[0]].squeeze())
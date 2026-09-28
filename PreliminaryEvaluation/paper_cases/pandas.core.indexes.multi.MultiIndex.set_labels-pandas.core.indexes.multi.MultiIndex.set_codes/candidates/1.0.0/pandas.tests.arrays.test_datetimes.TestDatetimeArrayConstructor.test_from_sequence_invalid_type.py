def test_from_sequence_invalid_type(self):
    mi = pd.MultiIndex.from_product([np.arange(5), np.arange(5)])
    with pytest.raises(TypeError, match='Cannot create a DatetimeArray'):
        DatetimeArray._from_sequence(mi)
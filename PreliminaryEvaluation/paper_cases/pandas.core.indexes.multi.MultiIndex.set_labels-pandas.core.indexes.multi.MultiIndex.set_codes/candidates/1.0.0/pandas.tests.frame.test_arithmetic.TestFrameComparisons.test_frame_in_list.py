def test_frame_in_list(self):
    df = pd.DataFrame(np.random.randn(6, 4), columns=list('ABCD'))
    msg = 'The truth value of a DataFrame is ambiguous'
    with pytest.raises(ValueError, match=msg):
        df in [None]
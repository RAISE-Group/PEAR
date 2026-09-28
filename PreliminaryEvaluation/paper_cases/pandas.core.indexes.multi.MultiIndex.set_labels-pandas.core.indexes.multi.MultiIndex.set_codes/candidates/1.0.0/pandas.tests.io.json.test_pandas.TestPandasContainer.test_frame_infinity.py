@pytest.mark.parametrize('inf', [np.inf, np.NINF])
@pytest.mark.parametrize('dtype', [True, False])
def test_frame_infinity(self, orient, inf, dtype):
    df = DataFrame([[1, 2], [4, 5, 6]])
    df.loc[0, 2] = inf
    result = read_json(df.to_json(), dtype=dtype)
    assert np.isnan(result.iloc[0, 2])
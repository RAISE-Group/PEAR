def test_empty_nonzero(self):
    df = DataFrame([1, 2, 3])
    assert not df.empty
    df = DataFrame(index=[1], columns=[1])
    assert not df.empty
    df = DataFrame(index=['a', 'b'], columns=['c', 'd']).dropna()
    assert df.empty
    assert df.T.empty
    empty_frames = [DataFrame(), DataFrame(index=[1]), DataFrame(columns=[1]), DataFrame({1: []})]
    for df in empty_frames:
        assert df.empty
        assert df.T.empty
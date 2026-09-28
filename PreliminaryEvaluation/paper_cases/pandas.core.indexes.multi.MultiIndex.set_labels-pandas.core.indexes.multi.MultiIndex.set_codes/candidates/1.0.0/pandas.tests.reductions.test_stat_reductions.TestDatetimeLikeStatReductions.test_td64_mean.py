@pytest.mark.parametrize('box', [Series, pd.Index, TimedeltaArray])
def test_td64_mean(self, box):
    tdi = pd.TimedeltaIndex([0, 3, -2, -7, 1, 2, -1, 3, 5, -2, 4], unit='D')
    tdarr = tdi._data
    obj = box(tdarr)
    result = obj.mean()
    expected = np.array(tdarr).mean()
    assert result == expected
    tdarr[0] = pd.NaT
    assert obj.mean(skipna=False) is pd.NaT
    result2 = obj.mean(skipna=True)
    assert result2 == tdi[1:].mean()
    assert result2.round('us') == (result * 11.0 / 10).round('us')
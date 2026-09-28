def test_doesnt_contain_all_the_things(self):
    i = Float64Index([np.nan])
    assert not i.isin([0]).item()
    assert not i.isin([1]).item()
    assert i.isin([np.nan]).item()
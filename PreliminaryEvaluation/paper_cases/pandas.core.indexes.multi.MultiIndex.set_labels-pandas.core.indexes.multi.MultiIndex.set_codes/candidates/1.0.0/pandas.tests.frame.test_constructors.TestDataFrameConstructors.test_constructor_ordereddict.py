def test_constructor_ordereddict(self):
    import random
    nitems = 100
    nums = list(range(nitems))
    random.shuffle(nums)
    expected = ['A{i:d}'.format(i=i) for i in nums]
    df = DataFrame(OrderedDict(zip(expected, [[0]] * nitems)))
    assert expected == list(df.columns)
def test_can_hold_element(self):
    block = create_block('datetime', [0])
    arr = pd.array(block.values.ravel())
    assert block._can_hold_element(None)
    arr[0] = None
    assert arr[0] is pd.NaT
    vals = [np.datetime64('2010-10-10'), datetime(2010, 10, 10)]
    for val in vals:
        assert block._can_hold_element(val)
        arr[0] = val
    val = date(2010, 10, 10)
    assert not block._can_hold_element(val)
    with pytest.raises(TypeError):
        arr[0] = val
def test_constructor_unsortable(self):
    arr = np.array([1, 2, 3, datetime.now()], dtype='O')
    factor = Categorical(arr, ordered=False)
    assert not factor.ordered
    msg = "'values' is not ordered, please explicitly specify the categories order by passing in a categories argument."
    with pytest.raises(TypeError, match=msg):
        Categorical(arr, ordered=True)
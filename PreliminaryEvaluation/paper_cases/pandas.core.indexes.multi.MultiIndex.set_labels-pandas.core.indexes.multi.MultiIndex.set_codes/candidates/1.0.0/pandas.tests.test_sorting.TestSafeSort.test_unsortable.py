def test_unsortable(self):
    arr = np.array([1, 2, datetime.now(), 0, 3], dtype=object)
    msg = "unorderable types: .* [<>] .*|'[<>]' not supported between instances of .*"
    with pytest.raises(TypeError, match=msg):
        safe_sort(arr)
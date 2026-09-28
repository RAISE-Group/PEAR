def test_complex_sorting(self):
    x17 = np.array([complex(i) for i in range(17)], dtype=object)
    msg = "unorderable types: .* [<>] .*|'[<>]' not supported between instances of .*"
    with pytest.raises(TypeError, match=msg):
        algos.factorize(x17[::-1], sort=True)
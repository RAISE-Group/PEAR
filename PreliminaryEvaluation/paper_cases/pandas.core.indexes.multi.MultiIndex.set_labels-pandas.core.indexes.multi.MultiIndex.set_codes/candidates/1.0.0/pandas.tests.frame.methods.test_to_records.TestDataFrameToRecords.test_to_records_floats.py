def test_to_records_floats(self):
    df = DataFrame(np.random.rand(10, 10))
    df.to_records()
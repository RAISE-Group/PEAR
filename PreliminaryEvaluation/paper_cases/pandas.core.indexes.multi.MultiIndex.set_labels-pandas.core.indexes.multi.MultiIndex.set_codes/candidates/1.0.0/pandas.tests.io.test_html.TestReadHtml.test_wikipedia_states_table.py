def test_wikipedia_states_table(self, datapath):
    data = datapath('io', 'data', 'html', 'wikipedia_states.html')
    assert os.path.isfile(data), f'{repr(data)} is not a file'
    assert os.path.getsize(data), f'{repr(data)} is an empty file'
    result = self.read_html(data, 'Arizona', header=1)[0]
    assert result['sq mi'].dtype == np.dtype('float64')
def test_encode_big_escape(self):
    for _ in range(10):
        base = 'å'.encode('utf-8')
        escape_input = base * 1024 * 1024 * 2
        ujson.encode(escape_input)
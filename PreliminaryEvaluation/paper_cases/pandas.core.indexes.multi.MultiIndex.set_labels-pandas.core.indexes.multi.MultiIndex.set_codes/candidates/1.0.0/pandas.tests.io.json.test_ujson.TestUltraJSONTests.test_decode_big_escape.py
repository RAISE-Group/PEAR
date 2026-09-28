def test_decode_big_escape(self):
    for _ in range(10):
        base = 'å'.encode('utf-8')
        quote = b'"'
        escape_input = quote + base * 1024 * 1024 * 2 + quote
        ujson.decode(escape_input)
def _format_data(self):
    n = len(self)
    max_seq_items = min((get_option('display.max_seq_items') or n) // 10, 10)
    formatter = str
    if n == 0:
        summary = '[]'
    elif n == 1:
        first = formatter(self[0])
        summary = f'[{first}]'
    elif n == 2:
        first = formatter(self[0])
        last = formatter(self[-1])
        summary = f'[{first}, {last}]'
    elif n > max_seq_items:
        n = min(max_seq_items // 2, 10)
        head = [formatter(x) for x in self[:n]]
        tail = [formatter(x) for x in self[-n:]]
        head_str = ', '.join(head)
        tail_str = ', '.join(tail)
        summary = f'[{head_str} ... {tail_str}]'
    else:
        tail = [formatter(x) for x in self]
        tail_str = ', '.join(tail)
        summary = f'[{tail_str}]'
    return summary
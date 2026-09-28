def _validate_sort_keyword(self, sort):
    if sort not in [None, False]:
        raise ValueError(f"The 'sort' keyword only takes the values of None or False; {sort} was passed.")
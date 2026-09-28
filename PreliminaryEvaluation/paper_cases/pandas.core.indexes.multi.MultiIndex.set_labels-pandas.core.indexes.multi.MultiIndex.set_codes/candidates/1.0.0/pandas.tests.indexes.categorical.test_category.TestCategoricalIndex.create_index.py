def create_index(self, categories=None, ordered=False):
    if categories is None:
        categories = list('cab')
    return CategoricalIndex(list('aabbca'), categories=categories, ordered=ordered)
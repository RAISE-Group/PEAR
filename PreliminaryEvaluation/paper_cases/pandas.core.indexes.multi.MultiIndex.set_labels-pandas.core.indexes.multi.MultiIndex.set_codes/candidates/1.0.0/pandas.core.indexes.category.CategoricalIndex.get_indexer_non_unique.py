@Appender(_index_shared_docs['get_indexer_non_unique'] % _index_doc_kwargs)
def get_indexer_non_unique(self, target):
    target = ibase.ensure_index(target)
    if isinstance(target, CategoricalIndex):
        if target.categories is self.categories:
            target = target.codes
            indexer, missing = self._engine.get_indexer_non_unique(target)
            return (ensure_platform_int(indexer), missing)
        target = target.values
    codes = self.categories.get_indexer(target)
    indexer, missing = self._engine.get_indexer_non_unique(codes)
    return (ensure_platform_int(indexer), missing)
def _maybe_downcast(self, blocks: List['Block'], downcast=None) -> List['Block']:
    if downcast is not None:
        return blocks
    return _extend_blocks([b.convert(datetime=True, numeric=False) for b in blocks])
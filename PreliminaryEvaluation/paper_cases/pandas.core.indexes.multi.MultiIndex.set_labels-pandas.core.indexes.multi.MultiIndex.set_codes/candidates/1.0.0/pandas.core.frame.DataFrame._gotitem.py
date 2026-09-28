def _gotitem(self, key: Union[str, List[str]], ndim: int, subset: Optional[Union[Series, ABCDataFrame]]=None) -> Union[Series, ABCDataFrame]:
    """
        Sub-classes to define. Return a sliced object.

        Parameters
        ----------
        key : string / list of selections
        ndim : 1,2
            requested ndim of result
        subset : object, default None
            subset to act on
        """
    if subset is None:
        subset = self
    elif subset.ndim == 1:
        return subset
    return subset[key]
def __eq__(self, other: Any) -> bool:
    """
        Rules for CDT equality:
        1) Any CDT is equal to the string 'category'
        2) Any CDT is equal to itself
        3) Any CDT is equal to a CDT with categories=None regardless of ordered
        4) A CDT with ordered=True is only equal to another CDT with
           ordered=True and identical categories in the same order
        5) A CDT with ordered={False, None} is only equal to another CDT with
           ordered={False, None} and identical categories, but same order is
           not required. There is no distinction between False/None.
        6) Any other comparison returns False
        """
    if isinstance(other, str):
        return other == self.name
    elif other is self:
        return True
    elif not (hasattr(other, 'ordered') and hasattr(other, 'categories')):
        return False
    elif self.categories is None or other.categories is None:
        return True
    elif self.ordered or other.ordered:
        return self.ordered == other.ordered and self.categories.equals(other.categories)
    else:
        if self.categories.dtype == other.categories.dtype and self.categories.equals(other.categories):
            return True
        return hash(self) == hash(other)
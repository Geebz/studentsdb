from math import ceil
from django.utils import six
import collections

class PageNotInteger(Exception):
    pass

class EmptyPage(Exception):
    pass

class PaginatorCustom:

    def __init__(self, object_list, per_page):
        self.object_list = object_list
        self.per_page = per_page
        self.num_object = len(object_list)

    def valid_number(self, number):
        try:
            number = int(number)
        except (ValueError, TypeError):
            raise PageNotInteger('Page is not integer')
        if number > self.num_object:
            raise EmptyPage('Page is empty')
        return number

    def _num_pages(self):
        num = int(ceil(self.num_object/float(self.per_page)))
        return num
    num_pages = property(_num_pages)

    def page(self, number):
        number = self.valid_number(number)
        top = (number-1)*self.per_page
        bottom = top + self.per_page

        return self._get_pages_(self.object_list[top:bottom], number, self)

    def _get_pages_(self, *args, **kwargs):

        return Page(*args, **kwargs)

    def _get_page_range(self): #copypaste
        """
        Returns a 1-based range of pages for iterating through within
        a template for loop.
        """
        return list(six.moves.range(1, self.num_pages + 1))

    page_range = property(_get_page_range)


class Page(collections.Sequence):

    def __init__(self, object_list, number, paginator):
        self.object_list = object_list
        self.number = number
        self.paginator = paginator

    """copypaste"""
    def __len__(self):
        return len(self.object_list)

    def __getitem__(self, index):
        if not isinstance(index, (slice,) + six.integer_types):
            raise TypeError
        # The object_list is converted to a list so that if it was a QuerySet
        # it won't be a database hit per __getitem__.
        if not isinstance(self.object_list, list):
            self.object_list = list(self.object_list)
        return self.object_list[index]
    """copypaste"""

    def has_previous(self):
        return self.number > 1

    def has_next(self):
        return self.number < self.paginator.num_pages

    def has_other_pages(self):
        return self.has_previous() or self.has_next()

    def previous_page_number(self):
        return self.number-1

    def next_page_number(self):
        return self.number+1

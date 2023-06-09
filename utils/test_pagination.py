from unittest import TestCase
from utils.pagination import make_pagination_range


class PaginationTest(TestCase):
    def test_make_pagination_range_returns_a_pagination_range(self):
        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            qty_pages=4,
            current_page=1,
        )['pagination']
        self.assertEqual([1, 2, 3, 4], pagination)

    def test_first_range_is_static_if_current_page_is_less_than_middle_page(self):  # noqa E501
        pagination = make_pagination_range(
            # For page 2 in list of 4
            page_range=list(range(1, 21)),
            qty_pages=4,
            current_page=2,
        )['pagination']
        self.assertEqual([1, 2, 3, 4], pagination)

        pagination = make_pagination_range(
            # For page 1 in list of 5
            page_range=list(range(1, 21)),
            qty_pages=5,
            current_page=1,
        )['pagination']
        self.assertEqual([1, 2, 3, 4, 5], pagination)

    def test_middle_range_are_correct(self):
        pagination = make_pagination_range(
            # For page 10 in list of 5
            page_range=list(range(1, 21)),
            qty_pages=5,
            current_page=10,
        )['pagination']
        self.assertEqual([8, 9, 10, 11, 12], pagination)

        pagination = make_pagination_range(
            # For page 14 in 4 of a higher list
            page_range=list(range(1, 31)),
            qty_pages=4,
            current_page=14,
        )['pagination']
        self.assertEqual([13, 14, 15, 16], pagination)

    def test_range_of_the_lists_with_less_itens_than_pages(self):
        pagination = make_pagination_range(
            # For less page than qty
            page_range=list(range(1, 5)),
            qty_pages=11,
            current_page=3,
        )['pagination']
        self.assertEqual([1, 2, 3, 4], pagination)

        pagination = make_pagination_range(
            # For less page than qty
            page_range=list(range(1, 6)),
            qty_pages=50,
            current_page=2,
        )['pagination']
        self.assertEqual([1, 2, 3, 4, 5], pagination)

    def test_if_the_last_range_is_static(self):
        pagination = make_pagination_range(
            # For the last page
            page_range=list(range(1, 11)),
            qty_pages=4,
            current_page=10,
        )['pagination']
        self.assertEqual([7, 8, 9, 10], pagination)

        pagination = make_pagination_range(
            # For the last page
            page_range=list(range(1, 11)),
            qty_pages=6,
            current_page=9,
        )['pagination']
        self.assertEqual([5, 6, 7, 8, 9, 10], pagination)

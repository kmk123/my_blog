from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination

class MyPagination(PageNumberPagination):
    page_size=5
    page_query_param='mypage'
    page_size_query_param='num'
    max_page_size=10
    last_page_strings=('end_point',)


class MyPagination1(LimitOffsetPagination):
    default_limit=5
    limit_query_param='mylimit'
    offset_query_param='myoffset'
    max_limit=20

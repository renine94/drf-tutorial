from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination


class WatchListPagination(PageNumberPagination):
    page_size = 3
    # page_query_param = 'p'  # ?p=2 (default: page)
    page_size_query_param = 'size'  # ?size=10 (number of data per page)
    max_page_size = 10  # ?size=12 로 요청해도 최대개수 10개까지만 반환한다. (위 옵션이 있어야만 작동한다.)
    last_page_strings = ('last', )  # ?page=last


class WatchListLOPagination(LimitOffsetPagination):
    default_limit = 5
    limit_query_param = 'limit'  # default: limit
    offset_query_param = 'start'  # default: offset
    max_limit = 5


# Cursor 페이징은 Ordering Filter와 같이 사용할 수 없다. (주의)
class WatchListCursorPagination(CursorPagination):
    page_size = 5
    cursor_query_param = 'record'  # (default: cursor)
    ordering = '-number_rating'  # Model fields에 정의된 컬럼을 지정해줘야 한다.

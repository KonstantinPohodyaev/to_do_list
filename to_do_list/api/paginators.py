from rest_framework import pagination


TASK_PAGINATOR_PAGE_SIZE = 5
TASK_PAGINATOR_MAX_PAGE_SIZE = 32


class TaskPageNumberLimitPagination(pagination.PageNumberPagination):
    page_size = TASK_PAGINATOR_PAGE_SIZE
    max_page_size = TASK_PAGINATOR_MAX_PAGE_SIZE
    page_size_query_param = 'limit'

from rest_framework.pagination import LimitOffsetPagination

class CustomLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 5  # Default number of items per page
    max_limit = 100    # Maximum number of items allowed per page
    limit_query_param = 'limit'  # Custom query parameter for limit
    offset_query_param = 'offset'  # Custom query parameter for offset
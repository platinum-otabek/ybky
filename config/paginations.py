from rest_framework import pagination
from rest_framework.response import Response


class CustomPagination(pagination.PageNumberPagination):
    page_size = 9
    page_size_query_param = 'page_size'
    max_page_size = 50
    page_query_param = 'p'

    def get_paginated_response(self, data):
        page_size_param = self.request.query_params.get('page_size', None)
        if page_size_param:
            ps = int(page_size_param)
        else:
            ps = self.page_size

        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'count': self.page.paginator.count,
            'page_size': ps,
            'num_pages': self.page.paginator.num_pages,
            'current_page': self.page.number,
            'countItemsOnPage': len(data),
            'results': data,
        })

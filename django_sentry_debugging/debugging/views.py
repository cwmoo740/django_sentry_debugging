from rest_framework.decorators import api_view


@api_view(['POST'])
def uploads_to_sentry(request):
    request.body
    request.data
    raise TypeError('body is uploaded to sentry')


@api_view(['POST'])
def no_body(request):
    request.data
    raise TypeError('does not upload body to sentry')

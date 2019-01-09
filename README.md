A minimal reproduction of issues with sentry and django rest framework.

The request body is not being uploaded as expected unless request.body is read before request.data.

This is because DRF's request.data uses its own io parser and calls the 
request.read() method directly instead of going though request.body

[DRF request parsing](https://github.com/encode/django-rest-framework/blob/3.9.0/rest_framework/parsers.py#L68)

[Django's Request.body method](https://github.com/django/django/blob/2.1.5/django/http/request.py#L283)

To reproduce:

```bash
export SENTRY_DSN="your-sentry-dsn-value"
python manage.py runserver
```

```bash
curl -d '{"key1":"value1", "key2":"value2"}' -H "Content-Type: application/json" -X POST http://localhost:8000/test/works/
curl -d '{"x": 5, "y": 10}' -H "Content-Type: application/json" -X POST http://localhost:8000/test/broken/
```

Observe that sentry never uploaded the request body for the second request.



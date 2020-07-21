from functools import reduce
def Create_New_Washing_Mechine(*args, **kwargs):  # pylint: disable=invalid-name
    """
    Note: replace below mock implementation with your actual implementation

    Request:

    kwargs["user"]                  -> request user
    kwargs["user_dto"]              -> request user_dto
    kwargs["request_object"]        -> request body type object
    kwargs["request_data"]          -> request body data dict
    kwargs["request_headers_obj"]   -> request headers object
    kwargs["request_query_params"]  -> request query parameters object
    kwargs["query_params"]          -> request query parameters dict
    kwargs["path_params"            -> request path parameters dict

    Response :

    return: tuple(response_status_code, response_object,
                  response_headers_object)

    from django_swagger_utils.drf_server.utils.server_gen.endpoint_response \
            import endpoint_response
    return endpoint_response(response_object)

    """
    access_token = ''
    http_authorization = args[0].META.get("HTTP_AUTHORIZATION")
    if http_authorization is not None:
        if len(http_authorization.split(" ")) == 2:
            access_token = http_authorization.split(" ")[1]
    http_source = args[0].META.get("HTTP_X_SOURCE")
    kwargs.update({"access_token": access_token, 'source': http_source})

    from .api_wrapper import api_wrapper
    response_object = api_wrapper(*args, **kwargs)
    response_status_code = 200
    response_headers_obj = None

    allowed_primitive_types = [False, str, int, float]
    from functools import reduce  # pylint: disable=redefined-builtin
    if response_object is None:
        from django.http.response import HttpResponse
        response_object = HttpResponse()

    elif reduce((lambda a, b: a or isinstance(response_object, b)),
                allowed_primitive_types):
        from django.http.response import HttpResponse
        response_object = HttpResponse(str(response_object))

    elif isinstance(response_object, tuple):
        response_status_code, response_object, response_headers_obj = response_object

    from django_swagger_utils.drf_server.utils.server_gen.endpoint_response \
        import endpoint_response
    return endpoint_response(response_object,response_status_code, response_headers_obj)

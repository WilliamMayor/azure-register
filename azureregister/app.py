def application(environ, start_response):
    status = '200 OK'
    response_headers = [('Content-type', 'text/plain')]
    start_response(status, response_headers)
    yield environ + '\n'
    yield dir(environ) + '\n'
    yield dir(start_response) + '\n'
    yield start_response + '\n'
    yield 'Hello from Windows Azure Websites\n'

BASE = '''<html>
    <head><title>{title}</title></head>
    <body>{body}</body>
</html>
'''

ISE = BASE.format(
    title='Oh Noes! Something Went Wrong!',
    body=('<h1>500 Internal Server Error</h1>'
          '<p>Sorry, something went wrong on our end. Whoops.</p>')
    )


def build_page(url, query):
    if url == '/':
        return BASE.format(
            title='Welcome',
            body='Stuff'
        )


def application(environ, start_response):
    status = '200 OK'
    response_headers = [('Content-type', 'text/html')]
    try:
        html = build_page(environ['PATH_INFO'], environ['QUERY_STRING'])
    except:
        status = '500 Internal Server Error'
        html = ISE
    start_response(status, response_headers)
    return html

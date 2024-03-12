from django.http import HttpResponse


def index(request):
    host = request.META["HTTP_HOST"]  # get the server address
    user_agent = request.META["HTTP_USER_AGENT"]  # getting browser data
    path = request.path  # getting the requested path
    return HttpResponse(f"""<h1>Test Web-Project for the CI/CD.</h1>
                            <p>Host: {host}</p>
                            <p>User agent: {user_agent}</p>
                            <p>Path: {path}</p>""")


def about(request, name, age):
    return HttpResponse(f"""
                            <h1>About:</h1>
                            <p>Name: {name}</p>
                            <p>Age: {age}</p>
                        """)


def contact(request):
    return HttpResponse("<h1>Contacts</h1>")


def user(request, name="Undefined", age=0):
    return HttpResponse(f"<h2>Name: {name}, Age: {age}</h2>")

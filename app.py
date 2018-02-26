#wsgiref.simple_server  is a WSGI (Web server gateway interface)
#pyramid.config is used later to configure the pyramid application
#pyramid.response is used later to create a web response
from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response

#Accepts argument request and returns an instance
#of the  pyramid.response class, this is the view
#function
def hello_world(request):
    return Response('Hello %(name)s!' % request.matchdict)

if __name__ == '__main__':

    #Create an instance of the configurator class
    with Configurator() as config:

        #add_route() registers a new route
        config.add_route('hello', '/hello/{name}')

        #Register a view callable, A view callable is 
        #the primary mechanism by which a developer
        #writes user interface code within Pyramid
        config.add_view(hello_world, route_name='hello')

        #After configuring views and setting up config
        #create a WSGI application
        app = config.make_wsgi_app()

        #Serve the wsgi application on localhost port 8080
        server = make_server('0.0.0.0', 8080, app)

        #Start the main loop which listens for requests
        #from the outside world
        server.serve_forever()

#
# This modul is present flask web server
# 

# libs

from flask import Flask, request

class Flask_mod:

    # constructor
    def __init__(self, controller, app_name, app_adress:str, app_port:int, app_debug:bool = False) -> None:

        # create app
        app = Flask(app_name)

        # refirect all routes and allow get, post requests
        @app.route('/', defaults={'path': '/'})
        @app.route('/<path:path>', methods=['GET', 'POST'])

        # process page
        def catch_all(path):

            # path fixing (if last "/" it must be deleted)
            path = path[:len(path) - 1] if path[len(path) - 1] == '/' and len(path) > 1 else path

            # GET request
            if request.method == "GET":
                return controller.Router_mod.GET(path)

            # Post request
            else:
                return controller.Router_mod.POST(path)

        # start application
        app.run(app_adress, app_port, app_debug)
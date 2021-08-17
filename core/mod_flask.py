#
# This modul is present flask web server
# 

# libs

from flask import Flask, request

class Flask_mod:

    # constructor
    def __init__(self, controller, app_name, app_adress:str, app_port:int, app_debug:bool = False) -> None:

        # controller 
        self.controller = controller

        # create app
        app = Flask(app_name)

        # refirect all routes and allow get, post requests
        @app.route('/', defaults={'path': '/'})
        @app.route('/<path:path>', methods=['GET', 'POST'])

        # it must by 2 tables for get and post request 1 its path 2 its action

        # process page
        def catch_all(path):

            # path fixing (if last "/" it must be deleted)
            path = path[:len(path) - 1] if path[len(path) - 1] == '/' and len(path) > 1 else path

            # open connection to db
            self.controller.DB_mod.Open()

            # write info about request
            self.controller.request = request

            # 
            # check cookies
            # 

            # load from client
            cookies_user_name = request.cookies.get('user_name')
            cookies_password = request.cookies.get('password')

            # check credentions
            self.controller.user_is_auth =True if self.controller.user_config['user_name'] == cookies_user_name and self.controller.user_config['user_password'] == cookies_password else False

            # GET request
            if request.method == "GET":
                page_to_print = controller.Router_mod.GET(path)

            # Post request
            else:
                page_to_print = controller.Router_mod.POST(path)

            # close connection to db
            self.controller.DB_mod.Close()

            # show page
            return page_to_print

        # start application
        app.run(app_adress, app_port, app_debug)

        
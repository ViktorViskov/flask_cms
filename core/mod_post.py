# 
# This modul for processing users request
# 

import re
from flask.templating import render_template_string


class POST_mod:

    # constructor
    def __init__(self, controller) -> None:
        self.controller = controller

    # process request
    def Process(self, path, request):
        # open connection to db
        self.controller.DB_mod.Open()

        # make action

        # login page
        if path == 'login':
            # user input
            login = request.form['user_name']
            password = request.form['password']

            # search user in database
            user = self.controller.DB_mod.IO("SELECT * FROM admins_credentions WHERE user_name = '%s' AND password = '%s'" % (login, password))

            # if user is found set cookies
            if len(user) == 1:
                # import needed lib
                from flask import make_response

                # create response
                response_to_client = make_response(render_template_string(self.controller.Router_mod.GET("/")))
                response_to_client.set_cookie('user_name' , login)
                response_to_client.set_cookie('password' , password)

                # return to client
                return response_to_client
                
            
            # show error page
            else:
                page_name = "admin"


        # path not found
        else:
            # show page not found
            page_name = "not_found"

        # close connection to db
        self.controller.DB_mod.Close()
        

        return self.controller.Router_mod.GET(page_name)
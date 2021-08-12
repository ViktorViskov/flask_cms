# 
# This modul for processing users request
# 

# needed libs
from flask.templating import render_template_string
from flask import make_response, redirect

class POST_mod:

    # constructor
    def __init__(self, controller) -> None:
        self.controller = controller

    # process request
    def Process(self, path):

        # make action

        # not found redirect to page not found
        if path == 'not_found':
            page_to_print = make_response(redirect("not_found"))
        
        # login page
        elif path == 'login':
            page_to_print = self.login()

        # path not found
        else:
            # show page not found
            page_to_print = self.controller.Router_mod.GET("not_found")
        
        return page_to_print

    # method for login
    def login(self):
            # user input
            login = self.controller.request.form['user_name']
            password = self.controller.request.form['password']

            # search user in database
            user = self.controller.DB_mod.IO("SELECT * FROM admins_credentions WHERE user_name = '%s' AND password = '%s'" % (login, password))

            # if user is found set cookies
            if len(user) == 1:

                # create response
                response_to_client = make_response(redirect("/admin_panel"))
                response_to_client.set_cookie('user_name' , login)
                response_to_client.set_cookie('password' , password)

                # return to client
                page_to_print = response_to_client
                
            
            # show error page
            else:
                # show page login or password not correct
                page_info = self.controller.DB_mod.IO("SELECT * FROM pages WHERE path = 'auth_fail'")
                page_to_print = self.controller.Render_mod.Page(page_info)
            
            # response
            return page_to_print
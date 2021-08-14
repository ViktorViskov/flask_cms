# 
# This modul for define all web site routes
# 

# libs
from flask import make_response, redirect

class Router_mod:
    

    # constuctor
    def __init__(self, controller) -> None:
        # set link to controller
        self.controller = controller

        # static routes for get requests
        self.static_routes_get = {
            '/':'/',
            'login':'login',
            'admin':'admin',
            

            }

        # static pages
        self.static_pages = {
            'admin':['admin','Admin panel','static_cookies','./src/admin_panel/admin_panel.html','', ''],
            'login':['login','Login page','static','./src/admin_panel/admin_login.html','', ''],
        }

    # for GET requests
    def GET(self, path):

        # check for static path
        if path in self.static_routes_get:
            page = self.static_routes_get[path]

            # check for static page
            if page in self.static_pages:
                page_info = [[]]
                page_info[0] = self.static_pages[page]

            # load from db
            else:
                page_info = self.controller.DB_mod.IO("SELECT * FROM pages WHERE path = '%s'" %page)


        # show page from db
        else:
            # load page
            page = self.controller.DB_mod.IO("SELECT * FROM get WHERE path = '%s'" %path)

            # if is not pressent load error page
            if len(page) != 1:
                page_info = self.controller.DB_mod.IO("SELECT * FROM pages WHERE path = 'not_found'")

            # show page
            else:
                # check for static page
                if page in self.static_pages:
                    page_info = [[]]
                    page_info[0] = self.static_pages[page]

                # load from db
                else:
                    page_info = self.controller.DB_mod.IO("SELECT * FROM pages WHERE path = '%s'" %page[0][1])

        # print page
        page_to_print = self.controller.Render_mod.Page(page_info)

        # return page
        return page_to_print

    # for POST requests
    def POST(self, path):

            # 
            # check cookies
            # 

            # load from client
            user_name = self.controller.request.cookies.get('user_name')
            password = self.controller.request.cookies.get('password')

            # check
            user = self.controller.DB_mod.IO("SELECT * FROM admins_credentions WHERE user_name = '%s' AND password = '%s'" % (user_name, password))

            # correct cookies
            if len(user) == 1 or path == 'login':

                # load page
                action = self.controller.DB_mod.IO("SELECT * FROM post WHERE path = '%s'" %path)

                # if is not pressent load error page
                if len(action) != 1:
                    page_to_print = self.controller.POST_mod.Process("not_found")
                
                # make action
                else:
                    page_to_print = self.controller.POST_mod.Process(action[0][1])

                # show page
                return page_to_print


            # cookies wrong
            else:
                return make_response(redirect("admin"))
                # page_path = self.controller.DB_mod.IO("SELECT file_path FROM pages WHERE path = 'not_auth'")[0][0]
                # page_content += self.Content_From_File(page_path)





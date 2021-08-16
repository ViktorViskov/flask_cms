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
            'nav_menu':'nav_menu',
            'show_page':'show_page',
            'hide_page':'hide_page',
            'sql_edith':'sql_edith',
            'page_create':'page_create',
            'page_delete':'page_delete',

            }

        # static routes for get requests
        self.static_routes_post = {
            'login':{
                'action':'login',
                'cookies':False
                },
            'create_nav_menu_item':{
                'action':'create_nav_menu_item',
                'cookies':True
                },
            'delete_nav_menu_item':{
                'action':'delete_nav_menu_item',
                'cookies':True
                },
            'show_page':{
                'action':'show_page',
                'cookies':True
                },
            'hide_page':{
                'action':'hide_page',
                'cookies':True
                },
            'sql_create':{
                'action':'sql_create',
                'cookies':True
                },
            'sql_delete':{
                'action':'sql_delete',
                'cookies':True
                },
            'page_create':{
                'action':'page_create',
                'cookies':True
                },
            'page_delete':{
                'action':'page_delete',
                'cookies':True
                },
            }

        # static sql requests
        self.static_sql = {
            'Get items':'SELECT * FROM get',
            'Nav items':'SELECT * FROM nav_menu',
            'Sql all':'SELECT * FROM sql_requests',
            'Sql visible':'SELECT name FROM sql_requests WHERE NOT EXISTS (SELECT sql_name FROM pages WHERE sql_requests.name = sql_name)',
            'Sql hidden':'SELECT name FROM sql_requests WHERE EXISTS (SELECT sql_name FROM pages WHERE sql_requests.name = sql_name)',
            'Pages all':'SELECT * FROM pages',
            'Pages visible':'SELECT pages.path FROM pages WHERE EXISTS (SELECT page FROM get WHERE pages.path = page)',
            'Pages hidden': 'SELECT pages.path FROM pages WHERE NOT EXISTS (SELECT page FROM get WHERE pages.path = page)',
        }

        # static pages
        self.static_pages = {
            '/':['Main','Main page','static','./src/pages/main.html','', ''],
            'admin':['admin','Admin panel','static_cookies','./static/pages/panel.html','', ''],
            'login':['login','Login page','static','./static/pages/login.html','', ''],
            'auth_fail':['auth_fail','Login or password not correct','static','./static/pages/auth_fail.html','', ''],
            'nav_menu':['nav_menu','Edith navigation menu','dynamic_cookies','./static/pages/nav_menu_edith.html','./static/pages/nav_menu_edith_block.html', 'Nav items'],
            'show_page':['show_page','Menu for enabling','dynamic_cookies','./static/pages/show_page.html','./static/pages/show_page_block.html', 'Pages hidden'],
            'hide_page':['hide_page','Menu for disabling pages','dynamic_cookies','./static/pages/hide_page.html','./static/pages/hide_page_block.html', 'Get items'],
            'sql_edith':['sql_edith','Menu sql edithor','dynamic_cookies','./static/pages/sql_edith.html','./static/pages/sql_edith_block.html', 'Sql visible'],
            'page_create':['page_create','Menu sql edithor','dynamic_cookies','./static/pages/page_create.html','./static/pages/page_create_block.html', 'Sql all'],
            'page_delete':['page_delete','Menu sql edithor','dynamic_cookies','./static/pages/page_delete.html','./static/pages/page_delete_block.html', 'Pages hidden'],
            
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

            # if is not pressent return not found string
            if len(page) != 1:
                return "Page not found"

            # show page
            else:
                # check for static page
                if page[0][0] in self.static_pages:
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

            # check for path is available
            if path in self.static_routes_post:

                # load action
                action = self.static_routes_post[path]['action']

                # cookies
                need_cookies = self.static_routes_post[path]['cookies']

                # check for cookies and user is auth
                if need_cookies:
                    # exec script
                    if self.controller.user_is_auth:
                        page_to_print = self.controller.POST_mod.Process(action)

                    # redirect
                    else:
                        page_to_print = make_response(redirect("login"))

                # exec action
                else:
                    page_to_print = self.controller.POST_mod.Process(action)

            # redirect to page not foound
            else:
                page_to_print = make_response(redirect("not_found"))

            # return page
            return page_to_print





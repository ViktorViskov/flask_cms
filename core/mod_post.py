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
    def Process(self, action):

        # make action
       
        # login page
        if action == 'login':
            page_to_print = self.login()

        # create nav menu item 
        elif action == 'create_nav_menu_item':
            page_to_print = self.create_nav_menu_item()

        # delete nav menu item 
        elif action == 'delete_nav_menu_item':
            page_to_print = self.delete_nav_menu_item()

        # create get_request item 
        elif action == 'show_page':
            page_to_print = self.create_get_request_item()

        # delete get_request item 
        elif action == 'hide_page':
            page_to_print = self.delete_get_request_item()
        
        # create sql_request item 
        elif action == 'sql_create':
            page_to_print = self.create_sql_request_item()

        # delete sql_request item 
        elif action == 'sql_delete':
            page_to_print = self.delete_sql_request_item()

        # create page file
        elif action == 'page_create':
            page_to_print = self.create_page()

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

        # check user credentions
        user_credentions_correct = True if self.controller.user_config['user_name'].strip() == login.strip() and self.controller.user_config['user_password'].strip() == password.strip() else False

        # if user is found set cookies
        if user_credentions_correct:

            # create response
            response_to_client = make_response(redirect("/admin"))
            response_to_client.set_cookie('user_name' , login)
            response_to_client.set_cookie('password' , password)

            # return to client
            page_to_print = response_to_client
            
        
        # show error page
        else:
            # show page login or password not correct
            page_info = [[]]
            page_info[0] = self.controller.Router_mod.static_pages['auth_fail']
            page_to_print = self.controller.Render_mod.Page(page_info)
        
        # response
        return page_to_print

    # metod for create nav menu item
    def create_nav_menu_item(self):
        # user input
        page_name = self.controller.request.form['name']
        page_href = self.controller.request.form['href']

        # make request to db
        self.controller.DB_mod.IO("INSERT INTO nav_menu VALUES ('%s','%s')" % (page_name, page_href), True)

        # redirect to nav menu edith
        return make_response(redirect("/nav_menu"))

    # metod for delete nav menu item
    def delete_nav_menu_item(self):
        # user input
        page_name = self.controller.request.form['name']

        # make request to db
        self.controller.DB_mod.IO("DELETE FROM nav_menu WHERE title = '%s'" % (page_name), True)

        # redirect to nav menu edith
        return make_response(redirect("/nav_menu"))

    # metod for create get request item
    def create_get_request_item(self):
        # user input
        path = self.controller.request.form['path']
        page = self.controller.request.form['page']

        # make request to db
        self.controller.DB_mod.IO("INSERT INTO get VALUES ('%s','%s')" % (path, page), True)

        # redirect to nav menu edith
        return make_response(redirect("/show_page"))

    # metod for delete get request item
    def delete_get_request_item(self):
        # user input
        page_path = self.controller.request.form['path']

        # make request to db
        self.controller.DB_mod.IO("DELETE FROM get WHERE path = '%s'" % (page_path), True)

        # redirect to nav menu edith
        return make_response(redirect("/hide_page"))

    # metod for create sql request item
    def create_sql_request_item(self):
        # user input
        name = self.controller.request.form['name']
        sql_request = self.controller.request.form['sql_request']

        # make request to db
        self.controller.DB_mod.IO("INSERT INTO sql_requests VALUES ('%s','%s')" % (name, sql_request), True)

        # redirect to nav menu edith
        return make_response(redirect("/sql_edith"))

    # metod for delete sql request item
    def delete_sql_request_item(self):
        # user input
        name = self.controller.request.form['name']

        # make request to db
        self.controller.DB_mod.IO("DELETE FROM sql_requests WHERE name = '%s'" % (name), True)

        # redirect to nav menu edith
        return make_response(redirect("/sql_edith"))
    
    # metod for delete sql request item
    def create_page(self):
        # user input
        page_path = self.controller.request.form['page_path']
        page_title = self.controller.request.form['page_title']
        page_type = self.controller.request.form['page_type']
        file_name = self.controller.request.form['file_name']
        file_content = self.controller.request.form['file_content']
        sql_name = self.controller.request.form['sql_name']
        sql_name = "'%s'" % sql_name if bool(sql_name) else 'null'
        path_to_file = "./src/pages/%s.html" % file_name

        # write to file
        created_file = open(path_to_file, "w");
        created_file.write(file_content)
        created_file.close()

        # create page in db
        self.controller.DB_mod.IO("INSERT INTO pages VALUES ('%s','%s','%s','%s',null,%s)" % (page_path, page_title, page_type, path_to_file,sql_name) ,True)

        # add to get table
        self.controller.DB_mod.IO("INSERT INTO get VALUES ('%s','%s')" % (page_path, page_path) ,True)
        
        # add to nav menu
        self.controller.DB_mod.IO("INSERT INTO nav_menu VALUES ('%s','%s')" % (page_path, page_path) ,True)

        # redirect to nav menu edith
        return make_response(redirect("/create_page"))
# 
# This modul for define all web site routes
# 

class Router_mod:
    

    # constuctor
    def __init__(self, controller) -> None:
        self.controller = controller

    # for GET requests
    def GET(self, path):

        # open connection to db
        self.controller.DB_mod.Open()

        # load page info
        page = self.controller.DB_mod.IO("SELECT * FROM pages WHERE path = '%s'" %path)

        # if is not pressent load error page
        if len(page) != 1:
            page = self.controller.DB_mod.IO("SELECT * FROM pages WHERE path = 'not_found'")

        # handler activate
        # here must be code for handler

        # load rendered page
        rendered_page = self.controller.Render_mod.Page(page)

        # close connection to db
        self.controller.DB_mod.Close()

        # show page
        return rendered_page

    # for POST requests
    def POST(self, path):
        return "From routes POST"



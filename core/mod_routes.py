# 
# This modul for define all web site routes
# 

class Router_mod:
    

    # constuctor
    def __init__(self, controller) -> None:
        self.controller = controller

    # for GET requests
    def GET(self, path):

        # load page
        page = self.controller.DB_mod.IO("SELECT * FROM get WHERE path = '%s'" %path)

        # if is not pressent load error page
        if len(page) != 1:
            page_to_print = self.controller.Render_mod.Page(self.controller.DB_mod.IO("SELECT * FROM pages WHERE path = 'not_found'"))
        
        # show page
        else:
            page_to_print = self.controller.Render_mod.Page(self.controller.DB_mod.IO("SELECT * FROM pages WHERE path = '%s'" %page[0][1]))

        # return page
        return page_to_print

    # for POST requests
    def POST(self, path):

        # make action
        rendered_page = self.controller.POST_mod.Process(path)
        
        # show page
        return rendered_page



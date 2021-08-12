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
            page_info = self.controller.DB_mod.IO("SELECT * FROM pages WHERE path = 'not_found'")
            page_to_print = self.controller.Render_mod.Page(page_info)
        
        # show page
        else:
            page_info = self.controller.DB_mod.IO("SELECT * FROM pages WHERE path = '%s'" %page[0][1])
            page_to_print = self.controller.Render_mod.Page(page_info)


        # return page
        return page_to_print

    # for POST requests
    def POST(self, path):

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



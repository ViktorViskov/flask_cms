# 
# This modul for define all web site routes
# 

class Router_mod:
    

    # constuctor
    def __init__(self, controller) -> None:
        self.controller = controller

    # for GET requests
    def GET(self, path):

        # load pages list
        pages = self.controller.DB_mod.IO("SELECT * FROM get_requests WHERE path = '%s'" %path)
        
        result = ";".join(",".join(str(item) for item in page) for page in pages)
        
        return result
        return "From routes GET"

    # for POST requests
    def POST(self, path):
        return "From routes POST"



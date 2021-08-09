# 
# Class controller. Here is all web app modules
# 

# import libs

# import modules
import core.mod_db
import core.mod_flask
import core.mod_routes
import core.mod_render
import core.mod_post


class Controller:
    
    
    # init modules
    def __init__(self) -> None:
        # 1 level init
        self.DB_mod = core.mod_db.Mod_db("127.0.0.1", "root", "dbnmjr031193", "flask_test")
        self.Router_mod = core.mod_routes.Router_mod(self)
        self.Render_mod = core.mod_render.Render_mod(self)
        self.POST_mod = core.mod_post.POST_mod(self)

        # 2 level init
        self.Flask_mod = core.mod_flask.Flask_mod(self,"Test application", "0.0.0.0", 5000, True)

        # example
        # self.DB_mod.IO("insert into test values (45, 'Some name')", True)
        # print (self.DB_mod.IO("Select * from test"))
        # example
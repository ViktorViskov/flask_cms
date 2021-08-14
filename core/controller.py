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
        # load config files
        db_config = self.config_processing(open("./configs/db.cfg","r").readlines())
        user_config = self.config_processing(open("./configs/user.cfg","r").readlines())
        main_config = self.config_processing(open("./configs/main.cfg","r").readlines())       

        # 1 level init
        self.DB_mod = core.mod_db.Mod_db(db_config['db_address'], db_config['db_user_name'], db_config['db_user_password'], db_config['db_name'])
        self.Router_mod = core.mod_routes.Router_mod(self)
        self.Render_mod = core.mod_render.Render_mod(self)
        self.POST_mod = core.mod_post.POST_mod(self)

        # 2 level init
        self.Flask_mod = core.mod_flask.Flask_mod(self,"Test application", "0.0.0.0", 5000, True)

        # example
        # self.DB_mod.IO("insert into test values (45, 'Some name')", True)
        # print (self.DB_mod.IO("Select * from test"))
        # example

    def config_processing(self, config_file_lines):

        # variable for result
        result = {}

        # processing
        for item in config_file_lines:
            splittet_string = item.split("=")
            result[splittet_string[0]] = splittet_string[1]

        # return result
        return result
# 
# This modul for creating pages
# 

class Render_mod:

    # constructor
    def __init__(self, controller) -> None:
        self.controller = controller
        self.page_root = open("./src/templates/root_page/index.html", "r").read()
        pass

    # method for building page
    def Page(self, page):

        # converting data
        path = page[0][0]
        title = page[0][1]
        type = page[0][2]
        file_path = page[0][3]
        item_path = page[0][4]
        sql_name = page[0][5]

        # init page
        page_to_print = self.page_root

        # replace parameters
        page_to_print = page_to_print.replace("!!LANG!!", "en")
        page_to_print = page_to_print.replace("!!TITLE!!", title)

        # nav bar 
        page_content = self.Nav_Menu()

        # static content
        if (type == 'static'):
            page_content += self.Content_From_File(file_path)

        # dynamic item
        elif (type == 'dynamic'):
            page_content += self.List_Content(file_path, item_path, sql_name)

        # cookies
        elif (type == 'cookies'):

            # check cookies

            # create page

            # cookies wrong
            page_content += self.Content_From_File('./src/static_pages/not_auth.html')


        # type not available
        else:
            page_content += self.Content_From_File('./src/static_pages/content_type_wrong.html')

        # replace content
        page_to_print = page_to_print.replace("!!CONTENT!!", page_content)

        # return page
        return page_to_print

    # method for load content from file
    def Content_From_File(self, file_path):
        
        # variable for content
        content = ""

        # try to read file
        try:
            content += open(file_path,'r').read()

        # if file not exist show default file with error
        except:
            content = "%s <<< Path not valid" % file_path

        # return content
        return content

    # method for create list items content
    def List_Content(self, file_path, item_path, sql_name):
        # variables
        content = ""
        content_list = ""
        
        # main root item
        root_item = self.Content_From_File(file_path)

        # list item
        list_item = self.Content_From_File(item_path)

        # load sql request from database
        sql_request = self.controller.DB_mod.IO("SELECT sql_request FROM sql_requests where name = '%s'" % sql_name)[0][0]
        db_response = self.controller.DB_mod.IO(sql_request)

        # creating content list
        for record in db_response:
            # create new item
            new_item = list_item

            # replace values
            for i in range(len(record)):
                new_item = new_item.replace("!!%d!!" % i, str(record[i]))
            
            # add created item
            content_list += new_item
        
        # add list to content
        content += root_item.replace("!!ITEMS!!", content_list)

        # return ready page
        return content

    

    # method for create nav menu
    def Nav_Menu(self):

        # variables for content and items
        nav_items = ""

        # load templates
        template_root = open("./src/templates/blocks/nav_container.html", "r").read()
        template_item = open("./src/templates/blocks/nav_item.html", "r").read()

        # load nav items from database
        items = self.controller.DB_mod.IO("SELECT * FROM nav_menu")

        # creating items
        for item in items:
            nav_items += template_item.replace("!!HREF!!", item[2]).replace("!!NAME!!", item[1])

        # return nav menu
        return template_root.replace("!!NAV_ITEMS!!", nav_items)



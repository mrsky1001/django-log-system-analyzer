import json
from collections import namedtuple

from analyzer.src.modules.MenuFactory import MenuFactory, MenuItem
from analyzer.src.classes.PrintText import print_text, THEMES_MESSAGE


class Settings:
    def __init__(self, path_to_settings="analyzer/settings.json"):
        self.path = path_to_settings
        self.root = "analyzer/"
        self.root_resources = self.root + "src/resources/"
        self.root_classes = self.root + "src/classes/"
        self.root_modules = self.root + "src/modules/"
        self.path_to_rrd_database = "rrd_database/"
        self.path_to_exports = self.root_resources + "exports/"
        self.path_to_csv = self.path_to_exports + "csv/"
        self.path_to_correlation = self.path_to_exports + "correlation/"
        self.path_to_correlation_xls = self.path_to_correlation + "xls/"
        self.path_to_correlation_images = self.path_to_correlation + "images/"
        self.path_to_merges_params = self.path_to_correlation + "merges_params/"
        self.path_to_description_of_params = self.path_to_exports + "description_of_params/"
        self.path_to_params_rrd = self.path_to_exports + "params_rrd/"
        self.path_to_graphs = self.path_to_exports + "graphs/"
        self.path_to_localization = "analyzer/localization.json"
        self.local = ""
        self.lang = "eng"
        self.start_point = "1419000000"
        self.end_point = "now"
        self.type_command = "AVERAGE"
        self.height_graph = "800"
        self.width_graph = "1024"
        self.init()

    def init(self):
        print_text("Loading settings...")

        with open(self.path) as f:
            data = json.load(f)
            self.root = data["default"]["root"]
            self.root_resources = self.root + data["default"]["root_resources"]
            self.root_classes = self.root + data["default"]["root_classes"]
            self.root_modules = self.root + data["default"]["root_modules"]
            self.path_to_rrd_database = self.root_resources + data["default"]["path_to_rrd_database"]
            self.path_to_exports = self.root_resources + data["default"]["path_to_exports"]
            self.path_to_correlation = self.path_to_exports + data["default"]["path_to_correlation"]
            self.path_to_correlation_images = self.path_to_correlation + data["default"]["path_to_correlation_images"]
            self.path_to_correlation_xls = self.path_to_correlation + data["default"]["path_to_correlation_xls"]
            self.path_to_merges_params = self.path_to_correlation + data["default"]["path_to_merges_params"]
            self.path_to_csv = self.path_to_exports + data["default"]["path_to_csv"]
            self.path_to_description_of_params = self.path_to_exports + data["default"]["path_to_description_of_params"]
            self.path_to_params_rrd = self.path_to_exports + data["default"]["path_to_params_rrd"]
            self.path_to_graphs = self.path_to_exports + data["default"]["path_to_graphs"]
            self.path_to_localization = data["default"]["path_to_localization"]
            self.start_point = data["default"]["start_point"]
            self.lang = data["default"]["lang"]
            self.end_point = data["default"]["end_point"]
            self.type_command = data["default"]["type_command"]
            self.height_graph = data["default"]["height"]
            self.width_graph = data["default"]["width"]
            self.load_localization(self.lang)

    def load_localization(self, lang):
        print_text("Loading localization...")
        self.lang = lang

        with open(self.path_to_localization) as f:
            self.local = json.loads(json.dumps(json.load(f)[lang]),
                                    object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))

        print_text(self.local.localization + self.lang)

    def display_settings(self):
        print_text(self.local.main_settings, THEMES_MESSAGE.INFO)
        print_text("path = ", self.path)
        print_text("root = ", self.root)
        print_text("root_resources = ", self.root_resources)
        print_text("root_classes = ", self.root_classes)
        print_text("root_modules = ", self.root_modules)
        print_text("path_to_rrd_database = ", self.path_to_rrd_database)
        print_text("path_to_exports = ", self.path_to_exports)
        print_text("path_to_correlation = ", self.path_to_correlation)
        print_text("path_to_correlation_images = ", self.path_to_correlation_images)
        print_text("path_to_correlation_xls = ", self.path_to_correlation_xls)
        print_text("path_to_merges_params = ", self.path_to_merges_params)
        print_text("path_to_csv = ", self.path_to_csv)
        print_text("path_to_description_of_params = ", self.path_to_description_of_params)
        print_text("path_to_params_rrd = ", self.path_to_params_rrd)
        print_text("path_to_graphs = ", self.path_to_graphs)
        print_text("path_to_localization = ", self.path_to_localization)
        print_text("localization = ", self.lang)
        print_text("start_point = ", self.start_point)
        print_text("end_point = ", self.end_point)
        print_text("type_command = ", self.type_command)
        print_text("height_graph = ", self.height_graph)
        print_text("width_graph = ", self.width_graph)

    def get_list_settings(self):
        class Param: 
            def __init__(self, name, value):
                self.name = name
                self.value = value
        
        list_settings = []

        list_settings.append(Param("path: ", self.path))
        list_settings.append(Param("root: ", self.root))
        list_settings.append(Param("root_resources: ", self.root_resources))
        list_settings.append(Param("root_classes: ", self.root_classes))
        list_settings.append(Param("root_modules: ", self.root_modules))
        list_settings.append(Param("path_to_rrd_database: ", self.path_to_rrd_database))
        list_settings.append(Param("path_to_exports: ", self.path_to_exports))
        list_settings.append(Param("path_to_correlation: ", self.path_to_correlation))
        list_settings.append(Param("path_to_correlation_images: ", self.path_to_correlation_images))
        list_settings.append(Param("path_to_correlation_xls: ", self.path_to_correlation_xls))
        list_settings.append(Param("path_to_merges_params: ", self.path_to_merges_params))
        list_settings.append(Param("path_to_csv: ", self.path_to_csv))
        list_settings.append(Param("path_to_description_of_params: ", self.path_to_description_of_params))
        list_settings.append(Param("path_to_params_rrd: ", self.path_to_params_rrd))
        list_settings.append(Param("path_to_graphs: ", self.path_to_graphs))
        list_settings.append(Param("path_to_localization: ", self.path_to_localization))
        list_settings.append(Param("localization: ", self.lang))
        list_settings.append(Param("start_point: ", self.start_point))
        list_settings.append(Param("end_point: ", self.end_point))
        list_settings.append(Param("type_command: ", self.type_command))
        list_settings.append(Param("height_graph: ", self.height_graph))
        list_settings.append(Param("width_graph: ", self.width_graph))

        return list_settings
# def change_localization(self):
#     menu = MenuFactory(self.local.menu_change_locale, self,
#                        lambda: [MenuItem("Russian", lambda: self.load_localization("rus")),
#                                 MenuItem("English", lambda: self.load_localization("eng"))])
#
#     menu.display_menu()
#     print_text(self.lang)


settings = Settings()

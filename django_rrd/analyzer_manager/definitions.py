from analyzer.src.classes.PrintText import print_text
from analyzer.src.modules.MenuFactory import MenuItem, MenuFactory
from analyzer.src.modules.RRDFactory import rrd_factory
from analyzer.src.modules.Settings import settings
from analyzer_manager.models.PageFactory.PageFactory import page_factory


#
# def init_menu_rrd_factory(rrd_factory):
#     list_item_menu = []
#
#     list_item_menu.append(
#         MenuItem(settings.local.display_settings, settings.display_settings))
#
#     list_item_menu.append(MenuItem(settings.local.display_list_rrd_files,
#                                    rrd_factory.display_list_rrd_files))
#     list_item_menu.append(
#         MenuItem(settings.local.select_rrd_file, lambda: (rrd_factory.select_rrd_file(),
#                                                           rrd_factory.selected_rrd.display_menu(rrd_factory))))
#
#     list_item_menu.append(MenuItem(settings.local.display_menu_selected_rrd_file,
#                                    lambda: rrd_factory.selected_rrd.display_menu(rrd_factory)))
#
#     list_item_menu.append(MenuItem(settings.local.export_params_all_rdd_files_to_csv,
#                                    rrd_factory.export_params_all_rdd_files_to_csv))
#     list_item_menu.append(
#         MenuItem(settings.local.correlation_rrd_files, rrd_factory.correlation_rrd_files))
#
#     # list_item_menu.append(MenuItem(settings.local.change_localization, settings.change_localization))
#     #
#     list_item_menu.append(MenuItem(settings.local.exit, lambda: -1))
#
#     return list_item_menu


def render_main_menu(render, request):
    data = {"title": "Список RRD", "list_menu": page_factory.list_pages}
    return render(request, "left_sidebar.html", context=data)


def render_list_rrd(render, request):
    data = {
        "title": settings.local.list_rrds_table,
        "header": {
            "name": settings.local.name,
            "description": settings.local.description,
            "file": settings.local.file
        },
        "list_menu": page_factory.list_pages,
        "list_rrd": rrd_factory.list_rrd
    }
    return render(request, "list_rrd.html", context=data)

def render_settings(render, request):
    data = {
        "title": settings.local.main_settings,
        "header": {
            "name": settings.local.name,
            "description": settings.local.description,
        },
        "list_menu": page_factory.list_pages,
        "list_settings": settings.get_list_settings()
    }
    return render(request, "settings.html", context=data)

# def init_menu_selected_rrd(settings, selected_rrd, rrd_factory):
#     list_item_menu = []
#
#     list_item_menu.append(
#         MenuItem(settings.local.display_params, selected_rrd.display_params))
#
#     list_item_menu.append(
#         MenuItem(settings.local.select_rrd_file, rrd_factory.select_rrd_file))
#
#     list_item_menu.append(MenuItem(settings.local.plot_graph_by_one_param,
#                                    selected_rrd.generate_graph_with_all_params))
#     list_item_menu.append(
#         MenuItem(settings.local.plot_graph_by_all_param, selected_rrd.generate_graphs_on_all_params))
#
#     list_item_menu.append(MenuItem(settings.local.export_params_to_csv,
#                                    selected_rrd.csv_export))
#
#     list_item_menu.append(MenuItem(settings.local.back_to_main_menu, lambda: -1))
#
#     return list_item_menu

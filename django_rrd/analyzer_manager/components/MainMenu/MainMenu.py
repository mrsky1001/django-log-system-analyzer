from analyzer.src.classes.PrintText import print_text
from analyzer.src.modules.MenuFactory import MenuFactory, init_menu_rrd_factory
from analyzer.src.modules.RRDFactory import rrd_factory
from analyzer.src.modules.Settings import settings


def main_menu_component(render, request):
    menu_rrd_factory = MenuFactory(settings.local.main_menu, settings,
                                   lambda: init_menu_rrd_factory(settings, rrd_factory))
    print_text('----------------------------------------------------------')
    print_text(menu_rrd_factory)
    data = {"list_menu": menu_rrd_factory.list_item_menu, "message": "Welcome to Python"}
    return render(request, "index.html", context=data)

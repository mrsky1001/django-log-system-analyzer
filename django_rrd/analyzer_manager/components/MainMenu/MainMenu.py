from analyzer.src.modules.MenuFactory import MenuFactory, init_menu_rrd_factory
from analyzer.src.modules.RRDFactory import rrd_factory
from analyzer.src.modules.Settings import settings


def main_menu_component(render, request):
    menu_rrd_factory = MenuFactory(settings.local.main_menu, settings,
                                   lambda: init_menu_rrd_factory(settings, rrd_factory))
    return render(request, "MainMenu.html")

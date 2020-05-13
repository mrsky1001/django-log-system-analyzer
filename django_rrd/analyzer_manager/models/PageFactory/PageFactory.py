from analyzer.src.modules.RRDFactory import rrd_factory
from analyzer.src.modules.Settings import settings


class Page:
    def __init__(self, name='', title='', url='', template=''):
        self.name = name
        self.title = title
        self.url = url
        self.component = template


class PageFactory:
    def __init__(self, list_pages=None):
        if list_pages is None:
            list_pages = []

        self.list_pages = list_pages


page_factory = PageFactory([
    Page(name=settings.local.list_rrds_table,
         title=settings.local.list_rrds_table,
         url='/list-rrd',
         template='list_rrd.html'),

    Page(name=settings.local.main_settings,
         title=settings.local.main_settings,
         url='/settings',
         template='settings.html')
])

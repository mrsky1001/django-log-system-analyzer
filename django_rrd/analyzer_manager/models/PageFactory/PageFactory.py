from analyzer.src.modules.RRDFactory import rrd_factory
from analyzer.src.modules.Settings import settings


class Page:
    def __init__(self, name='', title='', content='', component=''):
        self.name = name
        self.title = title
        self.content = content
        self.component = component


class PageFactory:
    def __init__(self, list_pages=None):
        if list_pages is None:
            list_pages = []

        self.list_pages = list_pages


page_factory = PageFactory([
    Page(name=settings.local.list_rrds_table,
         title=settings.local.list_rrds_table,
         component='list_rrd.html'),

    Page(name=settings.local.main_settings,
         title=settings.local.main_settings,
         content=settings,
         component='settings.html')
])

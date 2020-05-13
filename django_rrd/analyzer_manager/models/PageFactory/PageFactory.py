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
    Page(name='list_rrd',
         title=settings.local.list_rrds_table,
         content={
             "list_rrd": rrd_factory.list_rrd,
             "header": {
                 "name": settings.local.name,
                 "description": settings.local.description,
                 "file": settings.local.file
             }
         },
         component='list_rrd.html'),
    Page(name='menu_selected_rrd',
         title=settings.local.menu_select_rrd_file,
         content='',
         component='empty.html'),
    Page(name='settings',
         title=settings.local.main_settings,
         content=settings,
         component='settings.html')
])

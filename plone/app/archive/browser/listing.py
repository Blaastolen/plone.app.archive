
from zope.component import getUtility
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from plone.app.archive.interfaces import IContentArchive


class ArchiveListingView(BrowserView):

    template =  ViewPageTemplateFile('listing.pt')
    item_template =  ViewPageTemplateFile('item.pt')

    def __init__(self, context, request):
        super(ArchiveListingView, self).__init__(context, request)
        self._archive = getUtility(IContentArchive)

    def __call__(self):
        item = self.request.get('item', None)
        if item is not None:
            try:
                item = int(item)
                item = self._archive._archive._items[item]
                self.item = item['item']
            except ValueError:
                item = None
            except KeyError:
                item = None
        if item is None:
            return self.template()
        else:
            return self.item_template()

    def archive(self):
        return self._archive.listArchivedContent()

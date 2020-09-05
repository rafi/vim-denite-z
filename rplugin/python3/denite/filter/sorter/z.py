# ============================================================================
# FILE: sorter/word.py
# AUTHOR: Rafael Bodill <justrafi at gmail.com>
# DESCRIPTION: Filter to order by predefined 'filter__order' key/value
# License: MIT license
# ============================================================================

from denite.base.filter import Base


class Filter(Base):

    def __init__(self, vim):
        super().__init__(vim)

        self.name = 'sorter/z'
        self.description = 'Sorter for Z source ordering'

    def filter(self, context):
        if len(context['input']) < 1:
            return context['candidates']

        return sorted(
            context['candidates'],
            key=lambda x: x['filter__order'],
            reverse=True)

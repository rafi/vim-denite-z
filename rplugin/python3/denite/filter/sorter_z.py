from .base import Base


class Filter(Base):

    def __init__(self, vim):
        super().__init__(vim)

        self.name = 'sorter_z'
        self.description = 'Sorter for Z source ordering'

    def filter(self, context):
        if len(context['input']) < 1:
            return context['candidates']

        return sorted(
            context['candidates'],
            key=lambda x: x['filter__order'],
            reverse=True)

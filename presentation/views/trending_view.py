import itertools

from presentation.views.view import View


class TrendingView(View):

    def __init__(self, display, global_color, repository):
        super(TrendingView, self).__init__(display, global_color)
        self.repository = repository

    def show(self):
        trending_topics = self.repository.data
        if trending_topics:
            # The list of trending topics is huge. We only display the first five.
            top_5 = itertools.islice(trending_topics, 5)
            names = map(lambda trending_topic: trending_topic.name, top_5)
            text = ", ".join(names)
            self._log(text)
            self.display.show_text(text, self.global_color)

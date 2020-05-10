from presentation.views.view import View


class TrendingView(View):

    def __init__(self, display, global_color, repository, text_formatter):
        super(TrendingView, self).__init__(display, global_color)
        self.repository = repository
        self.text_formatter = text_formatter

    def show(self):
        trending_topics = self.repository.data
        if trending_topics:
            # The list of trending topics is huge. We only display the first five.
            top_5 = trending_topics[:5]
            names = map(lambda trending_topic: self.text_formatter.format(trending_topic.name), top_5)
            text = ", ".join(names)
            self._log(text)
            self.display.show_text(text, self.global_color)

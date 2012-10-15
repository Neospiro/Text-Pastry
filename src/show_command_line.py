import sublime, sublime_plugin, parser

class TextPastryCommandLine(sublime_plugin.WindowCommand):

    def run(self, text):
        if not self.window.active_view(): return
        v = self.window.show_input_panel('Enter a list of items, separated by spaces', text, self.on_done, None, None)

    def on_done(self, text):
        parser = Parser()
        r = parser.parse(text)
        if r: self.window.active_view().run_command(r["command"], r["args"])
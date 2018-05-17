import os
import requests
from i3pystatus import IntervalModule
from i3pystatus.core.color import ColorRangeModule


class CsBook(IntervalModule, ColorRangeModule):
    """
    uname(1) like module.

    .. rubric:: Available formatters

    * `{sysname}` — operating system name
    * `{nodename}` — name of machine on network (implementation-defined)
    * `{release}` — operating system release
    * `{version}` — operating system version
    * `{machine}` — hardware identifier
    """

    settings = (
        ("color", "The text color")
    )

    visible = True

    format = ""
    interval = 1
    location_code = 'N6N1E4'
    start_color = "#FF0000"
    end_color = "#00FF00"
    color = start_color
    colors = []

    api_url = "https://coinsquare.io/api/v1/data/bookandsales/CAD/BTC/16"
    update_interval_fast = 1
    update_interval_slow = 10
    update_interval = 1
    update_tick = 0
    icon = ""

    current_book = ""
    on_leftclick = 'toggle_fast'
    on_rightclick = "toggle_visible"

    def toggle_visible(self):
        self.visible = not self.visible

    def toggle_fast(self):
        if self.update_interval == self.update_interval_fast:
            self.update_interval = self.update_interval_slow
        else:
            self.update_interval = self.update_interval_fast

    def init(self):
        self.colors = self.get_hex_color_range(
            self.start_color, self.end_color, int(500))
        self.current_book = self.icon + \
            " (" + str(self.update_interval) + ") " + self.getBook()
        self.output = {
            "full_text": self.current_book,
            "color": self.color
        }

    def run(self):
        self.update_tick += 1
        if self.update_tick % self.update_interval == 0:
            self.current_book = self.getBook()
            self.update_tick = 0

        if self.visible:
            self.output = {
                "full_text": self.icon + " (" + str(self.update_interval) + ") " + self.current_book,
                "color": self.color
            }
        else:
            self.output = {
                "full_text": self.icon,
                "color": self.color
            }

    def getBook(self):
        response = requests.get(url=self.api_url)
        data = response.json()

        bidPrice = int((int(data['book'][0]['amt']) * 10000) /
                       ((int(data['book'][0]['base']) / 100)))
        bidSize = int((int(data['book'][0]['amt']) / 100))

        askPrice = int((int(data['book'][16]['amt']) * 10000) /
                       ((int(data['book'][16]['base']) / 100)))
        askSize = int((int(data['book'][16]['amt']) / 100))

        spread = askPrice - bidPrice
        spreadPercentage = float(float(spread / bidPrice) * 100)
        spreadPercentage = str("{0:.2f}".format(spreadPercentage))

        if spread >= len(self.colors):
            self.color = self.colors[-1]
        else:
            self.color = self.colors[spread]

        status = "B:%d($%d) | A:%d($%d) | S:%d(%s%%)" % (
            bidPrice, bidSize, askPrice, askSize, spread, spreadPercentage)
        return status

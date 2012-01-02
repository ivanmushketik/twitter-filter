from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import Qt
from PyQt4.QtGui import QScrollArea, QWidget, QVBoxLayout
from twitterFilter.tweetWidget import Ui_TweetWidget

__author__ = 'proger'

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class TweetWidget(Ui_TweetWidget):
    def setupUi(self, Widget):
        super(TweetWidget, self).setupUi(Widget)
        Widget.setLayout(self.root_layout)

    def display_author_name(self, widget, author_name):
        widget.author_name.setText(_fromUtf8("Author: " + author_name))

    def display_publishing_date(self, widget, publishing_date):
        widget.publishing.setText(_fromUtf8("Date: " + str(publishing_date)))

class TweetsWidget(QScrollArea):
    def __init__(self):
        QScrollArea.__init__(self)

        self.setWidgetResizable(True)

        scroll_widget = QWidget()
        self.scroll_box_layout = QVBoxLayout(scroll_widget)
        self.setWidget(scroll_widget)

        self.scroll_box_layout.setSpacing(2)
        self.scroll_box_layout.setMargin(2)

        self.scroll_box_layout.setAlignment(Qt.AlignTop)
        self.scroll_box_layout.setSizeConstraint(QtGui.QLayout.SetMaximumSize)


    def add_tweet(self, tweet):
        new_tweet_widget = QtGui.QWidget()
        ui = TweetWidget()
        ui.setupUi(new_tweet_widget)

        ui.display_author_name(new_tweet_widget, tweet.author.name)
        ui.display_publishing_date(new_tweet_widget, tweet.created_at)
        ui.display_tweet_text(new_tweet_widget, tweet.text)

        self.scroll_box_layout.addWidget(new_tweet_widget)






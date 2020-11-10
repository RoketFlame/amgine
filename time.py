class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('durak.ui', self)

        self.button_create_flag.clicked.connect(self.run)

        self.buttonGroup.buttonClicked.connect(self.run2)
        self.buttonGroup_2.buttonClicked.connect(self.run2)
        self.buttonGroup_3.buttonClicked.connect(self.run2)
        self.color = {self.buttonGroup: 'Синий', self.buttonGroup_2: 'Синий',
                      self.buttonGroup_3: 'Синий'}

    def run(self):
        self.label_flag.setText('Цвета: {}, {}, {}'.format(*self.color))

    def run2(self, button):
        self.color[self.sender()] = button.text()
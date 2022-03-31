class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        super(Pen, self).draw()
        print('Draw with a pen\n')


class Pencil(Stationery):
    def draw(self):
        super(Pencil, self).draw()
        print('Draw with a pencil\n')


class Handle(Stationery):
    def draw(self):
        super(Handle, self).draw()
        print('Draw with a marker\n')


pen = Pen('ручка')
pencil = Pencil('карандаш')
handle = Handle('маркер')

pen.draw()
pencil.draw()
handle.draw()
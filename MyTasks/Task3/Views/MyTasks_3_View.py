from tkinter import *
from tkinter import ttk
from MyTasks.Task3.Controllers.My_Tasks_3Controller import ShopingListController

class MyTasks_3_View(Tk):
    def __init__(self):
        super().__init__()
        # Конфигурация окна
        self.title("Учет сотрудников")
        self.geometry('1000x600')

        # Добавить покупку
        self.add_frame = ttk.Frame(self, borderwidth=1, relief=SOLID, padding=[8, 10])
        self.add_frame.pack(anchor='center', fill=X, pady=10, padx=10)
        self.add_shop_title = ttk.Label(self.add_frame, text="Добавить покупку")
        self.add_shop_title.pack()

        # Название продукта
        self.product_shop = ttk.Label(self.add_frame, text="Введите Название продукта")
        self.product_shop.pack()
        self.product_shop_input = ttk.Entry(self.add_frame)
        self.product_shop_input.pack()

        # Количество продукта
        self.quantity_shop = ttk.Label(self.add_frame, text="Введите Количество продукта")
        self.quantity_shop.pack()
        self.quantity_shop_input = ttk.Entry(self.add_frame)
        self.quantity_shop_input.pack()

        # Кнопка
        self.add_shop_button = ttk.Button(self.add_frame, text="Добавить покупку")
        self.add_shop_button["command"] = self.add_shop
        self.add_shop_button.pack()

        # Изменить статус покупки
        self.bought_frame = ttk.Frame(self, borderwidth=1, relief=SOLID, padding=[8, 10])
        self.bought_frame.pack(anchor='center', fill=X, pady=10, padx=10)
        self.title_bought = ttk.Label(self.bought_frame, text='Введите id покупки и её статус')
        self.title_bought.pack()
        self.id_input = ttk.Entry(self.bought_frame)
        self.id_input.pack()
        self.bought_input = ttk.Entry(self.bought_frame)
        self.bought_input.pack()
        self.bought_button = ttk.Button(self.bought_frame, text='Изменить статус покупки')
        self.bought_button["command"] = self.update_bought
        self.bought_button.pack()

        # Кнопка обновления таблицы
        self.button_update = ttk.Button(self.add_frame, text='Обновить таблицу', command=self.table)
        self.button_update.pack()

    #############################ТАБЛИЦА##############################
        columns = ('id', 'product', 'quantity', 'bought')
        self.tree = ttk.Treeview(self, columns=columns, show='headings')
        self.tree.pack(fill=BOTH, expand=1)
        self.table()  # Обновить таблицу покупок
        # Событие при выборе строки в таблице
        self.tree.bind("<<TreeviewSelect>>", self.item_select)

    # Метод который будет запускает окно для изменения статуса покупки при выборе строки из таблицы
    def item_select(self, event):
        self.item = self.tree.selection()[0]  # Получить строку
        self.shop = self.tree.item(self.item, "values")[0]  # Из строки получаем id покупки
        self.id_input.delete(0, 'end')
        self.id_input.insert(0, self.shop)
        # window_update_grade = UpdateRatindView(self.shop)

    def table(self):
        # Очистить таблицу
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Получить список покупок из БД
        shops = ShopingListController.get()
        list_shops = []
        for shop in shops:
            list_shops.append(
                (shop.id,
                 shop.product,
                 shop.quantity,
                 shop.bought)
            )

        # Заголовки для таблицы
        self.tree.heading('product', text='Название продукта')
        self.tree.heading('quantity', text='Количество продукта')
        self.tree.heading('bought', text='Статус покупки')
        # Добавить данные в таблицу
        for shop in list_shops:
            self.tree.insert('', END, values=staff)

    def update_bought(self):
        self.id = self.id_input.get()  # id сотрудника
        self.bought = self.bought_input.get()  # новое описание
        if not self.id or not self.bought:  # проверка на пустые поля
            self.title_bought['text'] = 'Введите id сотрудника и зарплату'
        elif not self.id.isdigit():  # Проверка на целое число
            self.title_bought['text'] = 'id сотрудника и зарплата должны быть числами'
        try:
            self.bought
        except ValueError:
            self.title_bought['text'] = 'id сотрудника и зарплата должны быть числами'
            return
        else:
            ShopingListController.bought_update(
                id=self.id,
                bought=self.bought
            )
        self.id_input.delete(0, 'end')
        self.bought_input.delete(0, 'end')
        self.table()  # Обновить таблицу сотрудников
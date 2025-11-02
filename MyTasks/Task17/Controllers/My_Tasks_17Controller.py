from MyTasks.Task17.Models.MyTasks_17 import MyTasks_17


class My_Tasks_17Controller:
    obj = MyTasks_17()

    # Добавление трека
    @classmethod
    def add(cls, title, artist, album, year, genre):
        cls.obj.music = {
            "title": title,
            "artist": artist,
            "album": album,
            "year": year,
            "genre": genre
        }

    # Прокси-метод
    @classmethod
    def get(cls):
        return cls.obj.music

    # Поиск по исполнителю
    @classmethod
    def find_by_artist(cls, artist):
        result = []
        for dict in cls.get():
            if dict["artist"] == artist:
                result.append(dict)
        return result

    # Поиск по жанру
    @classmethod
    def tracks_by_genre(cls, genre):
        result = []
        for dict in cls.get():
            if dict["genre"] == genre:
                result.append(dict)
        return result

    # Поиск по году
    @classmethod
    def albums_by_year(cls, year):
        result = []
        for dict in cls.get():
            if dict["year"] == year:
                result.append(dict)
        return result


if __name__ == "__main__":
    print("Все треки:", My_Tasks_17Controller.get())
    My_Tasks_17Controller.add("Stairway to Heaven", "Led Zeppelin", "Led Zeppelin IV", 1971, "рок")
    print("После добавления:", My_Tasks_17Controller.get())
    print("Треки Queen:", My_Tasks_17Controller.find_by_artist("Queen"))
    print("Треки жанра рок:", My_Tasks_17Controller.tracks_by_genre("рок"))
    print("Треки 1975 года:", My_Tasks_17Controller.albums_by_year(1975))
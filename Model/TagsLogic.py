
import csv
import Model.Tag


class TagsLogic:

    _tags = []

    def read_tags(self, path: str) -> list:
        """
        Funkcja wczytująca dane tagów z bazy danych (pliku .csv)
        :param path: ścieżka do pliku
        :return: lista filmów
        """
        with open(path, 'r', encoding='utf-8') as file:
            csv_reader = csv.reader(file, delimiter=',')

            for row in csv_reader:
                tag = Model.Tag.Tag(row[0], row[1], row[2], row[3])
                self._tags.append(tag.__dict__)

        self._tags.pop(0)
        return self._tags

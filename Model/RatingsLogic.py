
import csv
import Model.Rating


class RatingsLogic:

    _ratings = []

    def read_ratings(self, path: str) -> list:
        """
        Funkcja wczytująca dane ocen z bazy danych (pliku .csv)
        :param path: ścieżka do pliku
        :return: lista filmów
        """
        with open(path, 'r', encoding='utf-8') as file:
            csv_reader = csv.reader(file, delimiter=',')

            for row in csv_reader:
                rating = Model.Rating.Rating(row[0], row[1], row[2], row[3])
                self._ratings.append(rating.__dict__)

        self._ratings.pop(0)
        return self._ratings

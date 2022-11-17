
import csv
import Model.Movie


class MoviesLogic:

    _movies = []

    def read_movies(self, path: str, item_count: int) -> list:
        """
        Funkcja wczytująca dane filmów z bazy danych (pliku .csv)
        :param path: ścieżka do pliku
        :param item_count:
        :return: lista filmów
        """
        with open(path, 'r', encoding='utf-8') as file:
            csv_reader = csv.reader(file, delimiter=',')

            for row in csv_reader:
                movie = Model.Movie.Movie(row[0], row[1], row[2])
                self._movies.append(movie.__dict__)

        self._movies.pop(0)
        return self._movies[0: int(item_count)]

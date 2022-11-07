
import magazine.utils


class Product:
    def __str__(self):
        magazine.utils.print_text(self, "product")


product = Product
product.__str__(product)

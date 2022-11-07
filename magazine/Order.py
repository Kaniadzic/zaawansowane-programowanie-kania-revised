
import magazine.utils as utils


class Order:
    def __str__(self):
        utils.print_text(self, "order")


order = Order
order.__str__(order)

class Flower:

    def __init__(self, color, s_length, price, lifetime, freshness):
        self.color = color
        self.s_length = s_length
        self.price = price
        self.lifetime = lifetime
        self.freshness = freshness

    def __str__(self):
        return f'str - Flower color: {self.color}, price: {self.price} byn'

    def __repr__(self):
        return f'repr - Flower color: {self.color}, price: {self.price} byn'


class Rose(Flower):
    pass


class Tulip(Flower):
    pass


class Lily(Flower):
    pass


rose1 = Rose("red", 50, 10, 7, 90)
tulip1 = Tulip("yellow", 40, 7, 5, 80)
lily1 = Lily("white", 60, 15, 9, 85)


class Bouquet:

    def __init__(self, flowers):
        self.flowers = flowers

    def __ge__(self, obj, min_lifetime):
        return self.min_lifetime >= obj.min_lifetime

    def total_price(self):
        total_price = 0
        for flower in self.flowers:
            total_price += flower.price
        return total_price

    def avg_lifetime(self):
        total_lifetime = 0
        for flower in self.flowers:
            total_lifetime += flower.lifetime
        return int(total_lifetime / len(self.flowers))

    def sort_by_freshness(self):
        self.flowers.sort(key=lambda flower: flower.freshness)

    def sort_by_color(self):
        self.flowers.sort(key=lambda flower: flower.color)

    def sort_by_s_length(self):
        self.flowers.sort(key=lambda flower: flower.s_length)

    def find_flower_by_lifetime(self, min_lifetime):
        result = []
        for flower in self.flowers:
            if flower.lifetime >= min_lifetime:
                result.append(flower)
        return result


bouquet = Bouquet([rose1, tulip1, lily1])

print(bouquet.find_flower_by_lifetime(7))
print(bouquet.avg_lifetime())
print(bouquet.total_price())

bouquet.sort_by_color()
print(bouquet.flowers)

bouquet.sort_by_s_length()
print(bouquet.flowers)

bouquet.sort_by_freshness()
print(bouquet.flowers)

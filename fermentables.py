class Fermentable:
    def _init_(self, name="Fermentable", supplier=None, max_prop=1, usage="Mash", is_fermentable=True):
        # TODO: raise an ValueError exception when usage is not in ["Mash", "Steep", "Boil", "Whirpool", "Primary", "Secondary", "Tertiary", "Bottling"]
        pass
    # TODO: create __str__ and other printing methods

class Grain(Fermentable):
    def _init_(self):
        super().__init__()


class MaltExtract(Fermentable):
    pass


class DryMaltExtract(MaltExtract):
    pass


class LiquidMaltExtract(MaltExtract):
    pass


class Sugar(Fermentable):
    pass


class Adjunct(Fermentable):
    pass


class Fruit(Fermentable):
    pass


class Juice(Fermentable):
    pass


class Honey(Fermentable):
    pass


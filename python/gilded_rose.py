"""
this module contains GlideRose and Item class
"""
# -*- coding: utf-8 -*-

from constants import SULFURAS_HAND_OD_RAGNAROS, AGED_BRIE, BACKSTAGE_PASS, CONJURED

class GildedRose(object):
    """this contains all the functions required to manage the items and there quality
       this holds list of items
    """

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        """ this will update the quality of different types of item
        """

        for item in self.items:
            if item == SULFURAS_HAND_OD_RAGNAROS:
                continue
            if item.name == AGED_BRIE:
                self._update_aged_brie(item)

            elif item.name.startswith(BACKSTAGE_PASS):
                self._update_backstage_pass(item)

            elif item.name.lower.startswith(CONJURED):
                self._update_conjured_item(item)

            else:
                self._update_standard_item(item)

    def _dicrease_quality(self, item, amount = 1):
        """should be used to dicrement the quality
           dicrements the quantity default by 1 unit if amount not provided

        Args:
            item (item): item
            amount (int, optional): this is the amount by which the quality should be dicremented.
            Defaults to 1.
        """
        item.quality = max(item.quality - amount)

    def _increase_quality(self, item, amount = 1):
        """should be used to derecement the quality
           increment the quantity default by 1 unit if amount not provided

        Args:
            item (item): item
            amount (int, optional): this is the amount by which the quality should be incremented.\
                                    Defaults to 1.
        """
        item.quality = min(50, item.quality + amount)

    def _update_aged_brie(self, item):
        """this is for updating for aged_bire items
           this will increment the 
        """
        amount = 1
        #since the aged_brie's quality increases as older it gets
        #incrementing it if the sell_in is <=0
        if item.sell_in <= 0:
            amount +=1
        self._increase_quality(item, amount=amount)

    def _update_backstage_pass(self, item):
        """this will update the quality for backstage_pass
           a. quality drops to 0 if the pass expires
           b. increase by 2 if 10 or fewer days left
           c. increase by 3 if 5 or fewer days left
        """
        if item.sell_in <=0:
            item.quality = 0
            return
        amount = 1
        if item.sell_in <=5:
            amount +=1
        elif item.sell_in <= 10:
            amount +=1
        self._increase_quality(item, amount=amount)

    def _update_standard_item(self, item, amount = 1):
        """this can be used to dicrement the quality of a standard item
           this dicrease the quality by 1 if any sell_in dates are remaining 
           else, it will decremen ty 2 units
        """
        if item.sell_in <=0:
            amount +=1
        self._dicrease_quality(item, amount)

    def _update_conjured_item(self, item):
        """ this can be used to update the quality for conjured items
            this will updte quality by 2 units and if the sell_in date is 0 or fewer days
            this will resuce the qulaity by 2 times
        """
        degrade = 2
        if item.sell_in <= 0:
            degrade *=2
        self._dicrease_quality(item, degrade)


class Item:
    """ this represents an item, one can use this to create an item object
    """

    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

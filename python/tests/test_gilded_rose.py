# -*- coding: utf-8 -*-
import unittest

from python.gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("foo", items[0].name)


    def test_conjured_item(self):
        items = [Item("conjured", 1, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("conjured", items[0].name)
        self.assertEquals(1, items[0].sell_in)
        self.assertEquals(8, items[0].quality)

    def test_conjured_item_with_no_sellin_days(self):
        items = [Item("conjured", 0, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("conjured", items[0].name)
        self.assertEquals(0, items[0].sell_in)
        self.assertEquals(6, items[0].quality)


    def test_backstage_pass_item_less_than_5days(self):
        items = [Item("Backstage passes at 1", 1, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("Backstage passes at 1", items[0].name)
        self.assertEquals(1, items[0].sell_in)
        self.assertEquals(12, items[0].quality)

    def test_backstage_pass_item_less_than_10days(self):
        items = [Item("Backstage passes at 1", 9, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("Backstage passes at 1", items[0].name)
        self.assertEquals(9, items[0].sell_in)
        self.assertEquals(13, items[0].quality)


    def test_aged_brie_item(self):
        items = [Item("Aged Brie", 1, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("Aged Brie", items[0].name)
        self.assertEquals(1, items[0].sell_in)
        self.assertEquals(11, items[0].quality)

    def test_aged_brie_item(self):
        items = [Item("Aged Brie", 1, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("Aged Brie", items[0].name)
        self.assertEquals(1, items[0].sell_in)
        self.assertEquals(11, items[0].quality)

    def test_sulfuras_item(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 1, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("Sulfuras, Hand of Ragnaros", items[0].name)
        self.assertEquals(1, items[0].sell_in)
        self.assertEquals(10, items[0].quality)

    def test_sulfuras_item(self):
        items = [Item("random", 1, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("random", items[0].name)
        self.assertEquals(1, items[0].sell_in)
        self.assertEquals(9, items[0].quality)


    def test_for_multiple_items(self):
        items = [Item("random", 1, 10), Item("Sulfuras, Hand of Ragnaros", 1, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("random", items[0].name)
        self.assertEquals(1, items[0].sell_in)
        self.assertEquals(9, items[0].quality)

        self.assertEqual("Sulfuras, Hand of Ragnaros", items[1].name)
        self.assertEquals(1, items[1].sell_in)
        self.assertEquals(10, items[1].quality)

    def test_where_quality_more_than_50_for_backstage(self):
        items = [Item("Backstage passes at 1", 5, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("Backstage passes at 1", items[0].name)
        self.assertEquals(5, items[0].sell_in)
        self.assertEquals(50, items[0].quality)



if __name__ == '__main__':
    unittest.main()

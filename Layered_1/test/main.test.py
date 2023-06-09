import sys
import os
import unittest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from layers import ApplicationLayer,DataLayer,PresentationLayer


class TestApplicationLayer(unittest.TestCase):
  def setUp(self):
    self.app_layer = ApplicationLayer(DataLayer())

  def test_loads_cache(self):
    self.assertEqual(self.app_layer.is_init, False)
    self.assertEqual(self.app_layer.names_cache, None)

    self.app_layer.get_item_value('')

    self.assertEqual(self.app_layer.is_init, True)
    self.assertGreater(len(self.app_layer.names_cache), 0)

  def test_returns_values(self):
    self.app_layer.get_item_value('')

    self.assertNotEqual(self.app_layer.get_item_value(self.app_layer.names_cache[0]), None)

  def test_returns_none_values(self):
    self.assertEqual(self.app_layer.get_item_value(''), None)

class TestDataLayer(unittest.TestCase):
  def setUp(self):
    self.dataLayer = DataLayer()

  def test_loads_db(self):
    self.assertGreater(len(self.dataLayer.items), 0)

  def test_returns_keys(self):
    self.assertGreater(len(self.dataLayer.get_items_keys()), 0)

  def test_returns_values(self):
    self.assertNotEqual(self.dataLayer.get_item_value(self.dataLayer.get_items_keys()[0]), None)

  def test_returns_none_values(self):
    self.assertEqual(self.dataLayer.get_item_value('---'), None)
    self.assertEqual(self.dataLayer.get_item_value(''), None)
    self.assertEqual(self.dataLayer.get_item_value(None), None)


if __name__ == "__main__":
  unittest.main()
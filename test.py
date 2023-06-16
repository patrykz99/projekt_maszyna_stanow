import unittest
from unittest.mock import patch
from homepage_gui import GUI

class GUITest(unittest.TestCase):
    def setUp(self):
        self.gui = GUI()

    def tearDown(self):
        self.gui.ticket_machine.destroy()

    def test_menu(self):
        self.gui.menu()
        # Assert that the main menu is displayed
        self.assertEqual(len(self.gui.ticket_machine.winfo_children()), 3)

    @patch('builtins.input', side_effect=[0.50, 1.50])
    def test_sum_monety(self, mock_input):
        result = self.gui.sum_monety(2.50)
        self.assertEqual(result[0], 2.50)  # Check the total sum
        self.assertEqual(result[1], '0.00')  # Check the change
        self.assertTrue(result[2])  # Check if the purchase is complete

    def test_cancel_purchase(self):
        with patch('homepage_gui.GUI.clear_window') as mock_clear_window:
            self.gui.cancel_purchase()
            # Assert that the cancel message is displayed
            self.assertEqual(len(self.gui.ticket_machine.winfo_children()), 1)
            # Assert that the clear_window method is called
            mock_clear_window.assert_called_once()

    @patch('homepage_gui.GUI.print_ticket')
    def test_select_bilet(self, mock_print_ticket):
        self.gui.select_bilet('normalny', 3)
        # Assert that the ticket information is displayed
        self.assertEqual(len(self.gui.ticket_machine.winfo_children()), 4)
        # Assert that the print_ticket method is called
        mock_print_ticket.assert_called_once()

    @patch('homepage_gui.GUI.print_receipt')
    def test_paragon(self, mock_print_receipt):
        self.gui.paragon()
        # Assert that the receipt question is displayed
        self.assertEqual(len(self.gui.ticket_machine.winfo_children()), 2)
        # Assert that the print_receipt method is called when 'Tak' is clicked
        self.gui.button_yes.invoke()
        mock_print_receipt.assert_called_once()

    @patch('homepage_gui.GUI.menu')
    def test_print_receipt(self, mock_menu):
        self.gui.print_receipt()
        # Assert that the receipt printed message is displayed
        self.assertEqual(len(self.gui.ticket_machine.winfo_children()), 1)
        # Assert that the menu method is called after 3 seconds
        self.gui.ticket_machine.after.assert_called_once_with(3000, mock_menu)

    @patch('homepage_gui.GUI.menu')
    def test_no_receipt(self, mock_menu):
        self.gui.no_receipt()
        # Assert that the no receipt message is displayed
        self.assertEqual(len(self.gui.ticket_machine.winfo_children()), 1)
        # Assert that the menu method is called after 3 seconds
        self.gui.ticket_machine.after.assert_called_once_with(3000, mock_menu)

if __name__ == "__main__":
    unittest.main()

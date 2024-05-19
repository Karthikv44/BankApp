import unittest
from unittest.mock import patch, Mock
from datetime import date
import pyodbc

from DAO import IBankRepository  # Replace 'your_module' with the actual module name

class TestIBankRepository(unittest.TestCase):

    @patch('pyodbc.connect')
    def test_Get_transactions(self, mock_connect):
        # Mock the database connection and cursor
        mock_conn = Mock()
        mock_cursor = Mock()
        mock_connect.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor
        
        # Define a mock result set
        mock_cursor.fetchall.return_value = [
            Mock(TransactionID=1, AccountNumber=1001, TransactionDate=date(2024, 5, 1), Amount=100.0, TransactionType='Deposit'),
            Mock(TransactionID=2, AccountNumber=1002, TransactionDate=date(2024, 5, 10), Amount=50.0, TransactionType='Withdrawal')
        ]
        
        # Create an instance of BankRepository
        repo = IBankRepository('mock_connection_string')
        
        # Call the get_transactions method
        transactions = repo.Get_transactions(123456789, date(2024, 5, 1), date(2024, 5, 15))
        
        # Assert the results using assertTrue
        self.assertTrue(len(transactions) == 2)
        self.assertTrue(transactions[0]['TransactionID'] == 1)
        self.assertTrue(transactions[0]['Amount'] == 100.0)
        self.assertTrue(transactions[1]['TransactionType'] == 'Withdrawal')

    @patch('pyodbc.connect')
    def test_insert_formatted_date(self, mock_connect):
        mock_conn = Mock()
        mock_cursor = Mock()
        mock_connect.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor
        
        # Mock the get_formatted_current_date method
        mock_cursor.fetchone.return_value = Mock(CurrentDate='2024-05-15')
        
        repo = IBankRepository('mock_connection_string')
        
        # Call the insert_formatted_date method
        repo.insert_formatted_date('mock_connection_string')
        
        # Verify the insert query was executed with correct parameters
        mock_cursor.execute.assert_called_with(
            "INSERT INTO ExampleTable (FormattedDate) VALUES (?);", '2024-05-15'
        )
        mock_conn.commit.assert_called_once()
        
        # Assert using assertTrue that the method was called with correct parameters
        self.assertTrue(mock_cursor.execute.call_args[0][0] == "INSERT INTO ExampleTable (FormattedDate) VALUES (?);")
        self.assertTrue(mock_cursor.execute.call_args[0][1] == '2024-05-15')
        self.assertTrue(mock_conn.commit.called)

if __name__ == '__main__':
    unittest.main()

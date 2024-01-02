import unittest
from unittest.mock import MagicMock, patch
from external_api import get_data_from_api


URL = 'http://example.com/api'


class TestExternalApi(unittest.TestCase):
    @patch('external_api.requests')
    def test_get_data_from_api_success(self, mock_requests):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'key': 'value',
        }

        mock_requests.get.return_value = mock_response
        result = get_data_from_api(URL)

        self.assertEqual(result, mock_response.json.return_value)

    @patch('external_api.requests')
    def test_get_data_from_api_failure(self, mock_requests):
        mock_response = MagicMock()
        mock_response.status_code = 404
        mock_response.json.return_value = None
        mock_requests.get.return_value = mock_response
        result = get_data_from_api(URL)
        self.assertIsNone(result)

import unittest
import logging

logger = logging.getLogger(__name__)

class TestLoggerFormat(unittest.TestCase):
  def test_logger_format(self):
    logger.debug("The API call end successfully", extra={
      "url": "https://example.com/",
      "payload": "{}",
      "method": "GET"
    })

    pass

if __name__ == '__main__':
    unittest.main()
import unittest
import tempfile

import sheets


class Example(sheets.Row):
    name = sheets.StringColumn()
    birthday = sheets.DateColumn(format='%d.%m.%Y')
    age = sheets.IntegerColumn()

    class Dialect:
        has_header_row = True


class TestSheets(unittest.TestCase):
    def test_sheets(self):
        with open('input.csv', newline='') as input_:
            input_content = input_.read()
            input_.seek(0)
            reader = Example.reader(input_)
            rows = list(reader)

        self.assertEqual(2, len(rows))
        for row in rows:
            self.assertIsInstance(row, Example)

        with tempfile.TemporaryFile(mode='w+', newline='') as output:
            writer = Example.writer(output)
            writer.writerows(rows)
            output.seek(0)
            output_content = output.read()

        self.assertEqual(input_content, output_content)

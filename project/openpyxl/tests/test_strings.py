# Copyright (c) 2010-2014 openpyxl

# Python stdlib imports
import os.path

# package imports
from openpyxl.workbook import Workbook
from openpyxl.reader.strings import read_string_table

from openpyxl.tests.helper import compare_xml


def test_create_string_table():
    from openpyxl.writer.strings import create_string_table

    wb = Workbook()
    ws = wb.create_sheet()
    ws.cell('B12').value = 'hello'
    ws.cell('B13').value = 'world'
    ws.cell('D28').value = 'hello'
    table = create_string_table(wb)
    assert table == ['hello', 'world']


def test_read_string_table(datadir):
    datadir.join('reader').chdir()
    src = 'sharedStrings.xml'
    with open(src) as content:
        assert read_string_table(content.read()) == [
            'This is cell A1 in Sheet 1', 'This is cell G5']


def test_empty_string(datadir):
    datadir.join('reader').chdir()
    src = 'sharedStrings-emptystring.xml'
    with open(src) as content:
        assert read_string_table(content.read()) == ['Testing empty cell', '']


def test_formatted_string_table(datadir):
    datadir.join('reader').chdir()
    src = 'shared-strings-rich.xml'
    with open(src) as content:
        assert read_string_table(content.read()) == [
            'Welcome', 'to the best shop in town', "     let's play "]


def test_write_string_table(datadir):
    from openpyxl.writer.strings import write_string_table

    datadir.join("reader").chdir()
    table = ['This is cell A1 in Sheet 1', 'This is cell G5']
    content = write_string_table(table)
    with open('sharedStrings.xml') as expected:
        diff = compare_xml(content, expected.read())
        assert diff is None, diff

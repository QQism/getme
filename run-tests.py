#!/usr/bin/env python

import unittest

from jinja2 import Environment, PackageLoader, Template
from faker import Faker
from random import randint


from getme import Getme

class GetmeTestCase(unittest.TestCase):

    def setUp(self):
        env = Environment(loader=PackageLoader('test', 'templates'))
        self.page = env.get_template('page.html')
        self.f = Faker()


    def tearDown(self):
        pass

    def test_get_string(self):
        template = """
        <div>
        <span name='single-string'><getme/></span>
        </div>
        """
        processor =  Getme(template)

        name = self.f.name()
        page = self.page.render({'single_string': name})

        extracted_name = processor.extract(page)
        self.assertTrue(name == extracted_name)

    def test_single_list(self):
        template = """
        <ul name='single-list'>
        <li><getme/></li>
        </ul>
        """

        processor =  Getme(template)

        names = [self.f.name() for i in range(5)]
        page = self.page.render({'single_list': names})

        extracted_names = processor.extract(page)
        self.assertTrue(names == extracted_names)

    def test_odd_even_list(self):
        template = """
        <ul name='single-list'>
        <li class='odd'><getme/></li>
        </ul>
        <span><getme/></span>
        """

        processor =  Getme(template)

        odd_even = ['odd', 'even'] * 4
        page = self.page.render({'odd_even_list': odd_even})

        odd = processor.extract(page)
        self.assertFalse('even' in odd)

    def test_objects(self):
        template =  """
        <table>
            <tbody>
                <getme group='person'>
                    <tr>
                        <td><getme/></td>
                    </tr>
                </getme>
            </tbody>
        </table>
        """

        processor =  Getme(template)

        people = [self.generate_person() for i in range(3)]

        page = self.page.render({'people': people})

        result = processor.extract(page)

        expected_result = [{'person': [attr for key, attr in person.items()]} for person in people]

        self.assertTrue(len(result) == len(expected_result))


        size = len(result)

        for index in range(size):
            self.assertTrue(set(result[index]) == set(expected_result[index]))


    def generate_person(self):
        return {
            'first-name': self.f.first_name(),
            'last-name' : self.f.last_name(),
            'year'      : randint(1900, 1999),
            'state'     : self.f.state()
        }


if __name__ == '__main__':
    unittest.main()

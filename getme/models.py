# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup

class Getme(object):
    TAG = 'getme'

    def __init__(self, template):
        """
        create an instructions array from the template
        """
        self.template = template

        self.template = BeautifulSoup(template)
        self.instructions = []

        for getme in self.template.find_all(self.TAG):
            if 'group' in getme.attrs:
                self.handle_group(getme)
            else:
                self.handle_single(getme)

    def handle_single(self, getme):
        parent_nodes = getme.find_parents()
        parent_nodes.pop() # pop out the last, which is *not* a Tag object
        parent_nodes.reverse()
        self.instructions.append(parent_nodes)

    def handle_group(self, getme):
        pass

    def extract(self, document):
        """
        Extract content from document, followed by instructions
        """
        soup = BeautifulSoup(document)
        soup = self.clean_up(soup)

        total_contents = []
        for instruction in self.instructions:
            contents = self.call_childnode(soup, instruction, 0)
            if contents:
                total_contents.append(self.dearray(contents))

        return self.dearray(total_contents)

    def call_childnode(self, node, instruction, level):
        if len(instruction) == level:
            return node.text.strip(' \t\r\n') # remove nonsense chars
        else:
            instruction_node = instruction[level]
            level += 1
            if instruction_node.name == self.TAG and 'group' in instruction_node.attrs:
                group_name = instruction_node.attrs['group']
                instruction_node = instruction[level]
                level+=1
                contents = self.traverse_instruction(node,
                                                     instruction_node,
                                                     instruction,
                                                     level, group_name)
            else:
                contents = self.traverse_instruction(node,
                                                     instruction_node,
                                                     instruction,
                                                     level)
            return self.dearray(contents)

    def traverse_instruction(self, node, instruction_node, instruction, level, group=None):
        if group:
            return [{group: self.call_childnode(childnode, instruction, level)}
                for childnode in node.find_all(instruction_node.name,
                                               attrs=instruction_node.attrs)]
        else:
            return [self.call_childnode(childnode, instruction, level)
                for childnode in node.find_all(instruction_node.name,
                                               attrs=instruction_node.attrs)]


    def clean_up(self, soup):
        """get rid of trivial content"""
        [x.extract() for x in soup.find_all('script')] # remove all script tags
        return soup

    def dearray(self, elements):
        """ return the only element, *not* array """
        if isinstance(elements, list) and len(elements) == 1:
            return self.dearray(elements[0])
        return elements

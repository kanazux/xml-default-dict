#!/usr/bin/env python
# -*- cod utf-8 -*-
#
# Author Silvio AS a.k.a kanazuchi <contato@kanazuchi.com>
# Save defauldict to a xml file
#


from collections import defaultdict


class save_file():

    def __init__(self, dict_obj, old_key=""):
        self.d_o = dict_obj
        self.key = old_key
        self.text = ""
        self.cont = 0
        self.delimiter = "    "

    def return_xml_string(self, _dict_obj):
        self.cont = self.cont + 1
        if isinstance(_dict_obj, (defaultdict)):
            g_k = _dict_obj.keys()
            get_set = list(set([type(x) for x in g_k if x not in ["@prolog", "@attrs"]]))
            if len(get_set) == 1 and get_set[0] == int:
                pass
            for i in g_k:
                if i not in ["@prolog", "@attrs"]:
                    _delimiter = self.delimiter * self.cont
                    self.text = self.text + "{}<{}>\n".format(_delimiter, i)
                    if isinstance(_dict_obj[i], (defaultdict)):
                        self.return_xml_string(_dict_obj[i])
                        self.cont = self.cont - 1
                        _delimiter = self.delimiter * self.cont
                        self.text = self.text + "{}</{}>\n".format(_delimiter, i)
                    else:
                        self.cont = self.cont + 1
                        _delimiter = self.delimiter * self.cont
                        self.text = self.text + "{}{}\n".format(_delimiter, _dict_obj[i])
                        self.cont = self.cont - 1
                        _delimiter = self.delimiter * self.cont
                        self.text = self.text + "{}</{}>\n".format(_delimiter, i)

    def run(self):
        if isinstance(self.d_o, (defaultdict)):
            g_k = [x for x in self.d_o.keys()]
            if "@prolog" in g_k:
                self.text = self.text + self.d_o["@prolog"] + "\n"
            for i in g_k:
                if i not in ["@prolog", "@attrs"]:
                    self.text = self.text + "<{}>\n".format(i)
                    self.return_xml_string(self.d_o[i])
                    self.text = self.text + "</{}>\n".format(i)
        return self.text.rstrip('\n')

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
        self.tmp_delimiter = ""
        self.tmp_tag = ""
        self.cntrl_tag = False

    def process_list(self, set_list, _dict_obj, _dict_tag_name=None):
        for i in set_list:
            if i not in ["@prolog", "@attrs"]:
                _delimiter = self.delimiter * self.cont
                if _dict_tag_name is not None:
                    if _dict_tag_name == self.tmp_tag:
                        if len(_delimiter) > len(self.tmp_delimiter):
                            self.cont = self.cont - 1
                            _delimiter = self.delimiter * self.cont
                            self.tmp_delimiter = _delimiter
                        if self.cntrl_tag:
                            self.text = self.text + "{}<{}>\n".format(_delimiter, _dict_tag_name)
                    else:
                        self.text = self.text + "{}<{}>\n".format(_delimiter, _dict_tag_name)
                else:
                    self.text = self.text + "{}<{}>\n".format(_delimiter, i)
                self.cntrl_tag = False
                if isinstance(_dict_obj[i], (defaultdict)):
                    self.return_xml_string(_dict_obj[i], i)
                    if _dict_tag_name is not None:
                        self.text = self.text + "{}</{}>\n".format(_delimiter, _dict_tag_name)
                    else:
                        if self.tmp_tag != i:
                            self.text = self.text + "{}</{}>\n".format(_delimiter, i)
                    self.cntrl_tag = True
                else:
                    self.cont = self.cont + 1
                    _delimiter = self.delimiter * self.cont
                    self.text = self.text + "{}{}\n".format(_delimiter, _dict_obj[i])
                    self.cont = self.cont - 1
                    _delimiter = self.delimiter * self.cont
                    self.text = self.text + "{}</{}>\n".format(_delimiter, i)
                    self.cntrl_tag = True
            self.tmp_delimiter = _delimiter
            self.tmp_tag = _dict_tag_name

    def return_xml_string(self, _dict_obj, _tmp_name=""):
        self.cont = self.cont + 1
        self.tmp_cont = self.cont
        if isinstance(_dict_obj, (defaultdict)):
            g_k = _dict_obj.keys()
            get_set = list(set([type(x) for x in g_k if x not in ["@prolog", "@attrs"]]))
            self.tmp_tag = _tmp_name
            if len(get_set) == 1 and get_set[0] == int:
                self.process_list(g_k, _dict_obj, _tmp_name)
            else:
                self.process_list(g_k, _dict_obj)

    def run(self):
        if isinstance(self.d_o, (defaultdict)):
            g_k = [x for x in self.d_o.keys()]
            if "@prolog" in g_k:
                self.text = self.text + self.d_o["@prolog"] + "\n"
            for i in g_k:
                if i not in ["@prolog", "@attrs"]:
                    self.text = self.text + "<{}>\n".format(i)
                    self.return_xml_string(self.d_o[i], i)
                    self.text = self.text + "</{}>\n".format(i)
        return self.text.rstrip('\n')

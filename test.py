#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re


if __name__ == '__main__':

  test = "versuch {} regex".format("mit")
  print(test)
  regex = re.findall('(?<=versuch\s).*(?=\sregex)',test)
  print(regex)

# -*- coding: utf-8 -*-

# etree - модуль, который используется как реализация ElementTree
import lxml.etree as etree

# Doc, DocResponse классы для формирования XML-ответа
from doc import Doc
from util import make_url

from handler import PageHandler
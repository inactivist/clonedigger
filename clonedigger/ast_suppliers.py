from __future__ import absolute_import
from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from future import standard_library
standard_library.install_aliases()
from builtins import *
#    Copyright 2008 Peter Bulychev
#        http://clonedigger.sourceforge.net
#
#    This file is part of Clone Digger.
#
#    Clone Digger is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    Clone Digger is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with Clone Digger.  If not, see <http://www.gnu.org/licenses/>.

# Abstract Syntax Tree suppliers
abstract_syntax_tree_suppliers = {}

from . import python_compiler
abstract_syntax_tree_suppliers['python'] = python_compiler.PythonCompilerSourceFile

from . import java_antlr
abstract_syntax_tree_suppliers['java'] = java_antlr.JavaANTLRSourceFile

from . import lua_antlr
abstract_syntax_tree_suppliers['lua'] = lua_antlr.LuaANTLRSourceFile

from . import js_antlr
abstract_syntax_tree_suppliers['javascript'] = js_antlr.JsANTLRSourceFile
abstract_syntax_tree_suppliers['js'] = js_antlr.JsANTLRSourceFile

# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_code')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_code')
    _code = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_code', [dirname(__file__)])
        except ImportError:
            import _code
            return _code
        try:
            _mod = imp.load_module('_code', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _code = swig_import_helper()
    del swig_import_helper
else:
    import _code
del _swig_python_version_info

try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr(self, class_type, name):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    raise AttributeError("'%s' object has no attribute '%s'" % (class_type.__name__, name))


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except __builtin__.Exception:
    class _object:
        pass
    _newclass = 0

class SwigPyIterator(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SwigPyIterator, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SwigPyIterator, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _code.delete_SwigPyIterator
    __del__ = lambda self: None

    def value(self):
        return _code.SwigPyIterator_value(self)

    def incr(self, n=1):
        return _code.SwigPyIterator_incr(self, n)

    def decr(self, n=1):
        return _code.SwigPyIterator_decr(self, n)

    def distance(self, x):
        return _code.SwigPyIterator_distance(self, x)

    def equal(self, x):
        return _code.SwigPyIterator_equal(self, x)

    def copy(self):
        return _code.SwigPyIterator_copy(self)

    def next(self):
        return _code.SwigPyIterator_next(self)

    def __next__(self):
        return _code.SwigPyIterator___next__(self)

    def previous(self):
        return _code.SwigPyIterator_previous(self)

    def advance(self, n):
        return _code.SwigPyIterator_advance(self, n)

    def __eq__(self, x):
        return _code.SwigPyIterator___eq__(self, x)

    def __ne__(self, x):
        return _code.SwigPyIterator___ne__(self, x)

    def __iadd__(self, n):
        return _code.SwigPyIterator___iadd__(self, n)

    def __isub__(self, n):
        return _code.SwigPyIterator___isub__(self, n)

    def __add__(self, n):
        return _code.SwigPyIterator___add__(self, n)

    def __sub__(self, *args):
        return _code.SwigPyIterator___sub__(self, *args)
    def __iter__(self):
        return self
SwigPyIterator_swigregister = _code.SwigPyIterator_swigregister
SwigPyIterator_swigregister(SwigPyIterator)

class VecDouble(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, VecDouble, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, VecDouble, name)
    __repr__ = _swig_repr

    def iterator(self):
        return _code.VecDouble_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _code.VecDouble___nonzero__(self)

    def __bool__(self):
        return _code.VecDouble___bool__(self)

    def __len__(self):
        return _code.VecDouble___len__(self)

    def __getslice__(self, i, j):
        return _code.VecDouble___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _code.VecDouble___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _code.VecDouble___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _code.VecDouble___delitem__(self, *args)

    def __getitem__(self, *args):
        return _code.VecDouble___getitem__(self, *args)

    def __setitem__(self, *args):
        return _code.VecDouble___setitem__(self, *args)

    def pop(self):
        return _code.VecDouble_pop(self)

    def append(self, x):
        return _code.VecDouble_append(self, x)

    def empty(self):
        return _code.VecDouble_empty(self)

    def size(self):
        return _code.VecDouble_size(self)

    def swap(self, v):
        return _code.VecDouble_swap(self, v)

    def begin(self):
        return _code.VecDouble_begin(self)

    def end(self):
        return _code.VecDouble_end(self)

    def rbegin(self):
        return _code.VecDouble_rbegin(self)

    def rend(self):
        return _code.VecDouble_rend(self)

    def clear(self):
        return _code.VecDouble_clear(self)

    def get_allocator(self):
        return _code.VecDouble_get_allocator(self)

    def pop_back(self):
        return _code.VecDouble_pop_back(self)

    def erase(self, *args):
        return _code.VecDouble_erase(self, *args)

    def __init__(self, *args):
        this = _code.new_VecDouble(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def push_back(self, x):
        return _code.VecDouble_push_back(self, x)

    def front(self):
        return _code.VecDouble_front(self)

    def back(self):
        return _code.VecDouble_back(self)

    def assign(self, n, x):
        return _code.VecDouble_assign(self, n, x)

    def resize(self, *args):
        return _code.VecDouble_resize(self, *args)

    def insert(self, *args):
        return _code.VecDouble_insert(self, *args)

    def reserve(self, n):
        return _code.VecDouble_reserve(self, n)

    def capacity(self):
        return _code.VecDouble_capacity(self)
    __swig_destroy__ = _code.delete_VecDouble
    __del__ = lambda self: None
VecDouble_swigregister = _code.VecDouble_swigregister
VecDouble_swigregister(VecDouble)

class VecVecdouble(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, VecVecdouble, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, VecVecdouble, name)
    __repr__ = _swig_repr

    def iterator(self):
        return _code.VecVecdouble_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _code.VecVecdouble___nonzero__(self)

    def __bool__(self):
        return _code.VecVecdouble___bool__(self)

    def __len__(self):
        return _code.VecVecdouble___len__(self)

    def __getslice__(self, i, j):
        return _code.VecVecdouble___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _code.VecVecdouble___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _code.VecVecdouble___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _code.VecVecdouble___delitem__(self, *args)

    def __getitem__(self, *args):
        return _code.VecVecdouble___getitem__(self, *args)

    def __setitem__(self, *args):
        return _code.VecVecdouble___setitem__(self, *args)

    def pop(self):
        return _code.VecVecdouble_pop(self)

    def append(self, x):
        return _code.VecVecdouble_append(self, x)

    def empty(self):
        return _code.VecVecdouble_empty(self)

    def size(self):
        return _code.VecVecdouble_size(self)

    def swap(self, v):
        return _code.VecVecdouble_swap(self, v)

    def begin(self):
        return _code.VecVecdouble_begin(self)

    def end(self):
        return _code.VecVecdouble_end(self)

    def rbegin(self):
        return _code.VecVecdouble_rbegin(self)

    def rend(self):
        return _code.VecVecdouble_rend(self)

    def clear(self):
        return _code.VecVecdouble_clear(self)

    def get_allocator(self):
        return _code.VecVecdouble_get_allocator(self)

    def pop_back(self):
        return _code.VecVecdouble_pop_back(self)

    def erase(self, *args):
        return _code.VecVecdouble_erase(self, *args)

    def __init__(self, *args):
        this = _code.new_VecVecdouble(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def push_back(self, x):
        return _code.VecVecdouble_push_back(self, x)

    def front(self):
        return _code.VecVecdouble_front(self)

    def back(self):
        return _code.VecVecdouble_back(self)

    def assign(self, n, x):
        return _code.VecVecdouble_assign(self, n, x)

    def resize(self, *args):
        return _code.VecVecdouble_resize(self, *args)

    def insert(self, *args):
        return _code.VecVecdouble_insert(self, *args)

    def reserve(self, n):
        return _code.VecVecdouble_reserve(self, n)

    def capacity(self):
        return _code.VecVecdouble_capacity(self)
    __swig_destroy__ = _code.delete_VecVecdouble
    __del__ = lambda self: None
VecVecdouble_swigregister = _code.VecVecdouble_swigregister
VecVecdouble_swigregister(VecVecdouble)


def average(i_matrix):
    return _code.average(i_matrix)
average = _code.average
# This file is compatible with both classic and new-style classes.



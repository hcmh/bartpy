# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
import _fft_swig

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "thisown":
            self.this.own(value)
        elif name == "this":
            set(self, name, value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)



def fftmod(N, dims, flags, dst, src):
    return _fft_swig.fftmod(N, dims, flags, dst, src)

def ifftmod(N, dims, flags, dst, src):
    return _fft_swig.ifftmod(N, dims, flags, dst, src)

def fftscale(N, dims, flags, dst, src):
    return _fft_swig.fftscale(N, dims, flags, dst, src)

def fftshift(N, dims, flags, dst, src):
    return _fft_swig.fftshift(N, dims, flags, dst, src)

def ifftshift(N, dims, flags, dst, src):
    return _fft_swig.ifftshift(N, dims, flags, dst, src)

def fft(dimensions, flags, src):
    return _fft_swig.fft(dimensions, flags, src)

def ifft(dimensions, flags, src):
    return _fft_swig.ifft(dimensions, flags, src)

def fftc(D, dimensions, flags, dst, src):
    return _fft_swig.fftc(D, dimensions, flags, dst, src)

def ifftc(D, dimensions, flags, dst, src):
    return _fft_swig.ifftc(D, dimensions, flags, dst, src)

def fftu(D, dimensions, flags, dst, src):
    return _fft_swig.fftu(D, dimensions, flags, dst, src)

def ifftu(D, dimensions, flags, dst, src):
    return _fft_swig.ifftu(D, dimensions, flags, dst, src)

def fftuc(D, dimensions, flags, dst, src):
    return _fft_swig.fftuc(D, dimensions, flags, dst, src)

def ifftuc(D, dimensions, flags, dst, src):
    return _fft_swig.ifftuc(D, dimensions, flags, dst, src)



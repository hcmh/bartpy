# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _linop
else:
    import _linop

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


class long_arr(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, nelements):
        _linop.long_arr_swiginit(self, _linop.new_long_arr(nelements))
    __swig_destroy__ = _linop.delete_long_arr

    def __getitem__(self, index):
        return _linop.long_arr___getitem__(self, index)

    def __setitem__(self, index, value):
        return _linop.long_arr___setitem__(self, index, value)

    def cast(self):
        return _linop.long_arr_cast(self)

    @staticmethod
    def frompointer(t):
        return _linop.long_arr_frompointer(t)

# Register long_arr in _linop:
_linop.long_arr_swigregister(long_arr)

def long_arr_frompointer(t):
    return _linop.long_arr_frompointer(t)

class floatp(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self):
        _linop.floatp_swiginit(self, _linop.new_floatp())
    __swig_destroy__ = _linop.delete_floatp

    def assign(self, value):
        return _linop.floatp_assign(self, value)

    def value(self):
        return _linop.floatp_value(self)

    def cast(self):
        return _linop.floatp_cast(self)

    @staticmethod
    def frompointer(t):
        return _linop.floatp_frompointer(t)

# Register floatp in _linop:
_linop.floatp_swigregister(floatp)

def floatp_frompointer(t):
    return _linop.floatp_frompointer(t)

class complexp(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self):
        _linop.complexp_swiginit(self, _linop.new_complexp())
    __swig_destroy__ = _linop.delete_complexp

    def assign(self, value):
        return _linop.complexp_assign(self, value)

    def value(self):
        return _linop.complexp_value(self)

    def cast(self):
        return _linop.complexp_cast(self)

    @staticmethod
    def frompointer(t):
        return _linop.complexp_frompointer(t)

# Register complexp in _linop:
_linop.complexp_swigregister(complexp)

def complexp_frompointer(t):
    return _linop.complexp_frompointer(t)


def create_complex_array(re, im, n):
    return _linop.create_complex_array(re, im, n)

def linop_create(ON, odims, IN, idims, data, forward, adjoint, normal, norm_inv, arg10):
    return _linop.linop_create(ON, odims, IN, idims, data, forward, adjoint, normal, norm_inv, arg10)

def linop_create2(ON, odims, ostr, IN, idims, istrs, data, forward, adjoint, normal, norm_inv, arg12):
    return _linop.linop_create2(ON, odims, ostr, IN, idims, istrs, data, forward, adjoint, normal, norm_inv, arg12)

def linop_get_data(ptr):
    return _linop.linop_get_data(ptr)

def linop_free(op):
    return _linop.linop_free(op)

def linop_forward(op, DN, ddims, dst, SN, sdims, src):
    return _linop.linop_forward(op, DN, ddims, dst, SN, sdims, src)

def linop_adjoint(op, DN, ddims, dst, SN, sdims, src):
    return _linop.linop_adjoint(op, DN, ddims, dst, SN, sdims, src)

def linop_normal(op, N, dims, dst, src):
    return _linop.linop_normal(op, N, dims, dst, src)

def linop_pseudo_inv(op, _lambda, DN, ddims, dst, SN, sdims, src):
    return _linop.linop_pseudo_inv(op, _lambda, DN, ddims, dst, SN, sdims, src)

def linop_forward_unchecked(op, dst, src):
    return _linop.linop_forward_unchecked(op, dst, src)

def linop_adjoint_unchecked(op, dst, src):
    return _linop.linop_adjoint_unchecked(op, dst, src)

def linop_normal_unchecked(op, dst, src):
    return _linop.linop_normal_unchecked(op, dst, src)

def linop_norm_inv_unchecked(op, _lambda, dst, src):
    return _linop.linop_norm_inv_unchecked(op, _lambda, dst, src)

def linop_chain(a, b):
    return _linop.linop_chain(a, b)

def linop_chainN(N, x):
    return _linop.linop_chainN(N, x)

def linop_chain_FF(a, b):
    return _linop.linop_chain_FF(a, b)

def linop_stack(D, E, a, b):
    return _linop.linop_stack(D, E, a, b)

def linop_domain(x):
    return _linop.linop_domain(x)

def linop_codomain(x):
    return _linop.linop_codomain(x)

def linop_clone(x):
    return _linop.linop_clone(x)

def linop_loop(D, dims, op):
    return _linop.linop_loop(D, dims, op)

def linop_copy_wrapper(D, istrs, ostrs, op):
    return _linop.linop_copy_wrapper(D, istrs, ostrs, op)

def linop_null_create2(NO, odims, ostrs, NI, idims, istrs):
    return _linop.linop_null_create2(NO, odims, ostrs, NI, idims, istrs)

def linop_null_create(NO, odims, NI, idims):
    return _linop.linop_null_create(NO, odims, NI, idims)

def linop_plus(a, b):
    return _linop.linop_plus(a, b)

def linop_plus_FF(a, b):
    return _linop.linop_plus_FF(a, b)

def linop_grad_create(N, dims, d, flags):
    return _linop.linop_grad_create(N, dims, d, flags)

def linop_cdiag_create(N, dims, flags, diag):
    return _linop.linop_cdiag_create(N, dims, flags, diag)

def linop_rdiag_create(N, dims, flags, diag):
    return _linop.linop_rdiag_create(N, dims, flags, diag)

def linop_identity_create(N, dims):
    return _linop.linop_identity_create(N, dims)

def linop_resize_create(N, out_dims, in_dims):
    return _linop.linop_resize_create(N, out_dims, in_dims)

def linop_resize_center_create(N, out_dims, in_dims):
    return _linop.linop_resize_center_create(N, out_dims, in_dims)

def linop_expand_create(N, out_dims, in_dims):
    return _linop.linop_expand_create(N, out_dims, in_dims)

def linop_reshape_create(A, out_dims, B, in_dims):
    return _linop.linop_reshape_create(A, out_dims, B, in_dims)

def linop_extract_create(N, pos, out_dims, in_dims):
    return _linop.linop_extract_create(N, pos, out_dims, in_dims)

def linop_transpose_create(N, a, b, dims):
    return _linop.linop_transpose_create(N, a, b, dims)

def linop_fft_create(N, dims, flags):
    return _linop.linop_fft_create(N, dims, flags)

def linop_ifft_create(N, dims, flags):
    return _linop.linop_ifft_create(N, dims, flags)

def linop_fftc_create(N, dims, flags):
    return _linop.linop_fftc_create(N, dims, flags)

def linop_ifftc_create(N, dims, flags):
    return _linop.linop_ifftc_create(N, dims, flags)

def linop_fft_create_measure(N, dims, flags):
    return _linop.linop_fft_create_measure(N, dims, flags)

def linop_cdf97_create(N, dims, flag):
    return _linop.linop_cdf97_create(N, dims, flag)
CONV_SYMMETRIC = _linop.CONV_SYMMETRIC
CONV_CAUSAL = _linop.CONV_CAUSAL
CONV_ANTICAUSAL = _linop.CONV_ANTICAUSAL
CONV_CYCLIC = _linop.CONV_CYCLIC
CONV_TRUNCATED = _linop.CONV_TRUNCATED
CONV_VALID = _linop.CONV_VALID
CONV_EXTENDED = _linop.CONV_EXTENDED

def linop_conv_create(N, flags, ctype, cmode, odims, idims1, idims2, src2):
    return _linop.linop_conv_create(N, flags, ctype, cmode, odims, idims1, idims2, src2)

def linop_matrix_create(N, out_dims, in_dims, matrix_dims, matrix):
    return _linop.linop_matrix_create(N, out_dims, in_dims, matrix_dims, matrix)

def linop_matrix_chain(a, b):
    return _linop.linop_matrix_chain(a, b)



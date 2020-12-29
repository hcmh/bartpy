# bart-swig

![BART-logo](BART-logo.png)

Python bindings for [BART](https://github.com/mrirecon/bart), autogenerated with [SWIG](http://swig.org/).

## Examples

```
import numpy as np
from matplotlib import pyplot as plt

from bartpy.simu.phantom import phantom
from bartpy.num.fft import ifft

# generate BART logo phantom in K-Space
logo_ksp = phantom([256, 256], ksp=True, ptype="bart")
logo_recon = ifft(logo_ksp)

plt.imshow(abs(logo_recon))
```

## Python Interface

### Requirements

[BART](https://github.com/mrirecon/bart)

NumPy


### Installation

Ensure that the environment variable `TOOLBOX_PATH` is set to your BART installation.

From this directory, run `python setup.py install`

### Current Coverage

#### `bartpy.simu.phantom`

- `phantom(dims, ksp=False, d3=False, ptype="shepp")`
    - Generates a numerical phantom in K-Space or the Image Domain.

#### `bartpy.num.fft`
- `fft(src, flags=0, unitary=False, centered=True)`
- `ifft(src, flags=0, unitary=False, centered=True)`

#### `bartpy.utils.cfl`
- `readcfl(name)`
- `writecfl(name)`

## Building With SWIG

To build with [SWIG](http://swig.org/), install SWIG and run `swig_setup.sh` from the `swig` subdirectory. 

At the moment, you may need to change file paths within the `.i` interface files. Additionally, when the resulting `{MODULE}_swig.py` files are generated, you will have to replace the if/else block on line 12 with `import _{MODULE}_swig.py`. Everything else should be correctly autogenerated.

## Next steps

These are my current tasks:

- [ ] Bug fixes
- [ ] Automatic documentation with Sphinx 
- [ ] Cleaning up package/module structure
- [ ] Further code coverage
    - [ ]
    - [ ]
    - [ ] 
- [ ] Simple tutorials

### Known Bugs
- There is an issue where the Python interpreter will hang after executing some functions with numpy data (e.g., calling `phantom` on a numpy array of dimensions). This is either GIL related or has to do with the way that I parse dimensions from the dimension array in the SWIG bindings. I suspect it's the latter, because the issue does not persist when `fft` is called on a numpy array. 
- Data not quite parsed correctly - see FFT recon of BART logo
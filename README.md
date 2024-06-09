# exploring-bosonic-qiskit-qec
Exploring Bosonic Error Correction with Bosonic Qiskit

This repository contains the code used for a school project. The codebase was developed to implement and validate the concepts discussed, as well as to serve as an educational introduction to Bosonic Error Correction.

---

Bosonic Qiskit is a C2QA project extending the functionality of Qiskit to simulate hybrid qumode-qubit systems. 
For additional information about installation, usage and a set of tutorials, visit the [official Github repository](https://github.com/C2QA/bosonic-qiskit). 
Here you can also download the c2qa package needed to program with Bosonic Qiskit.

A significant portion of the code in this repository is based on the work from [bosonic-qiskit](https://github.com/C2QA/bosonic-qiskit).

---
> Download c2qa from the [official Github repository](https://github.com/C2QA/bosonic-qiskit).

To use the `c2qa` package in your project, you need to ensure that it is located in the `root directory` of your project.
If `c2qa` is not in the root directory or another directory listed in `sys.path`, Python won't be able to find it.

However, you can manually add the directory containing `c2qa` to `sys.path` using the following code:

```python
import os
import sys
module_path = os.path.abspath(os.path.join("../.."))
if module_path not in sys.path:
    sys.path.append(module_path)
```

This code adds the parent directory of the parent directory of the current file to `sys.path`, allowing Python to import `c2qa` even if it's not in the current directory. <br>
To check `sys.path`, you can print it:

```python
print(sys.path)
```

---

### Dependencies
- Bosonic Qiskit 11.2
- Qiskit 1.1.0
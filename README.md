> [!TIP]
> This repository is the development version of the published book that can be found at https://doi.org/10.59490/tb.88.
>
> Cite as: Hensbergen, A., & Verhulst, N. (2024). _Linear Algebra_. TU Delft OPEN Books. https://doi.org/10.59490/tb.88

# Linear Algebra - Interactive Textbook

[![Creative Commons License](https://i.creativecommons.org/l/by/4.0/88x31.png)](http://creativecommons.org/licenses/by/4.0/)

An interactive, open-access linear algebra textbook designed for engineering students at the bachelor level. This book combines traditional mathematical rigor with modern interactive elements to create an engaging learning experience.

## 📖 Read the Book

The complete interactive textbook is available at: [https://interactivetextbooks.tudelft.nl/linear-algebra/](https://interactivetextbooks.tudelft.nl/linear-algebra/)

## 🎯 About This Textbook

This textbook is suited for a standard linear algebra course for engineering students. No prior knowledge is expected beyond basic algebra skills typically taught in secondary education.

### Key Features

- **Interactive Learning**: Embedded applets provide hands-on experience with linear algebra concepts
- **Geometric Perspective**: Main concepts are introduced from a geometrical viewpoint
- **Individualized Feedback**: Comprehensive selection of exercises with personalized feedback
- **Modern Design**: Built using Jupyter Book for an engaging digital experience
- **Open Access**: Freely available under Creative Commons Attribution 4.0 license

### Topics Covered

The book covers the following chapters:

1. **Vectors, Lines and Planes** - Introduction to basic geometric concepts
2. **Systems of Equations** - Linear systems, combinations, and solution sets
3. **Matrix Operations** - Linear transformations, inverse matrices, and LU decomposition
4. **Subspaces and Basis** - Vector spaces, basis, dimension, and change of basis
5. **Determinants** - Geometric interpretation and computational methods
6. **Eigenvalues and Eigenvectors** - Characteristic polynomials and diagonalization
7. **Orthogonality** - Gram-Schmidt process, least squares, and orthogonal bases
8. **Symmetric Matrices** - including quadratic forms and singular value decomposition
9. **Dynamical Systems** - Discrete systems, Markov chains, the power method and systems of differential equations

## 🛠️ Building the Book

This repository contains the source files for building the interactive textbook using Jupyter Book.

### Prerequisites

- Python 3.7+
- Jupyter Book
- Required packages (see `requirements.txt`)

### Installation

```bash
# Clone the repository
git clone https://github.com/TUDelft-PRIME-Books/Linear-Algebra.git
cd Linear-Algebra

# Install dependencies
pip install -r requirements.txt
```

### Building

Build the book using Jupyter Book:

```bash
# Build the book
jupyter-book build .
```

The built book will be available in the `_build/html/` directory. You can then open `_build/html/index.html` in your browser to view the book locally.

## 📁 Repository Structure

```
├── _config.yml          # Jupyter Book configuration
├── _toc.yml             # Table of contents
├── index.md             # Main page
├── Introduction.md      # Book introduction
├── Chapter1/            # Vectors, lines and planes
├── Chapter2/            # Systems of equations
├── Chapter3/            # Matrix operations
├── Chapter4/            # Subspaces and basis
├── Chapter5/            # Determinants
├── Chapter6/            # Eigenvalues and eigenvectors
├── Chapter7/            # Orthogonality
├── Chapter8/            # Symmetric matrices
├── Chapter9/            # Dynamical systems
├── Appendices/          # Additional material
├── Colophon/            # Acknowledgements
├── _static/             # Static assets (CSS, images)
└── _ext/                # Custom Sphinx extensions
```

## 👥 Authors and Contributors

This book was created by a team of lecturers from the **Delft Institute of Applied Mathematics** at **TU Delft University of Technology**.

### Principal Authors
- [Drs. A.T. (André) Hensbergen](https://www.tudelft.nl/ewi/over-de-faculteit/afdelingen/applied-mathematics/people/drs-at-andre-hensbergen)
- [Dr. N.D. (Nikolaas) Verhulst](https://www.linkedin.com/in/nikolaas-verhulst-0aa912130/)

### Contributing Authors
- [Dr. D. (Dani) Balagué Guardia](https://www.tudelft.nl/ewi/over-de-faculteit/afdelingen/applied-mathematics/people/dr-d-dani-balague-guardia)
- [Dr. F.J. (Fokko) van de Bult](https://www.tudelft.nl/ewi/over-de-faculteit/afdelingen/applied-mathematics/people/dr-fj-fokko-van-de-bult)
- [Dr.ir. D. (Dennis) den Ouden-van der Horst](https://www.linkedin.com/in/dennis-den-ouden-614b5813/)
- [Dr. T.W.C. (Tom) Vroegrijk](https://www.linkedin.com/in/tomvroegrijk/)

## 🤝 Contributing

We welcome contributions to improve this textbook! Please feel free to:

- Report issues or suggest improvements
- Submit pull requests for corrections or enhancements
- Provide feedback on the interactive elements

## 📄 License

This work is licensed under a [Creative Commons Attribution 4.0 International License](http://creativecommons.org/licenses/by/4.0/).

You are free to:
- **Share** — copy and redistribute the material in any medium or format
- **Adapt** — remix, transform, and build upon the material for any purpose, even commercially

## 💰 Funding

This project was funded by a grant from the [NPO (Nationaal Programma Onderwijs)](https://www.nponderwijs.nl/). The team collaborated closely with [PRIME (PRogramme of Innovation in Mathematics Education)](https://www.tudelft.nl/ewi/over-de-faculteit/afdelingen/applied-mathematics/studeren/prime).

## 📧 Contact

For questions about this textbook, please contact the Delft Institute of Applied Mathematics at TU Delft.

---

**TU Delft** | **Faculty of Electrical Engineering, Mathematics and Computer Science** | **Delft Institute of Applied Mathematics**


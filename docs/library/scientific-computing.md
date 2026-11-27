---
title: "Scientific Computing – Awesome List with 91 resources"
description: "91 curated Scientific Computing resources: Solving complex scientific problems using computers."
---

# Scientific Computing

Solving complex scientific problems using computers.

!!! info "Source"
    91 resources imported from [nschloe/awesome-scientific-computing](https://github.com/nschloe/awesome-scientific-computing), dedicated to the public domain ([CC0 / Unlicense](https://creativecommons.org/publicdomain/zero/1.0/)). Thanks to its maintainers and contributors. Part of the [KEEBOX Library](index.md) · Category: **Miscellaneous**.

<!-- kb-about:start -->

## About this list

**Scientific Computing** — solving complex scientific problems using computers. This page brings together 91 links about Scientific Computing, grouped into 9 sections. The largest sections are **Meshing**, **Other libraries and tools**, **Finite Elements**, a good place to start if you are exploring the topic for the first time. It belongs to the **Miscellaneous** category of the KEEBOX Library; see the related lists at the end of the page for neighbouring topics.

### What you'll find

- **Basic linear algebra** — 7 links
- **Multi-purpose toolkits** — 5 links
- **Finite Elements** — 11 links
- **Meshing** — 21 links
- **Data formats** — 4 links
- **Sparse linear solvers** — 3 links
- **Visualization** — 10 links
- **Other libraries and tools** — 21 links
- **Community** — 9 links

<!-- kb-about:end -->

## Basic linear algebra

- [BLAS](https://netlib.org/blas/) - Standard building blocks for performing basic vector and matrix operations.
- [OpenBLAS](https://www.openblas.net) - Optimized BLAS library based on GotoBLAS2.
- [BLIS](https://github.com/flame/blis) - High-performance BLAS-like dense linear algebra libraries.
- [LAPACK](https://netlib.org/lapack/) - Routines for solving systems of linear equations, linear least-squares, eigenvalue problems, etc.
- [Eigen](https://libeigen.gitlab.io/) - C++ template library for linear algebra.
- [Ginkgo](https://ginkgo-project.github.io/) - High-performance manycore linear algebra library, focus on sparse systems.
- [blaze](https://bitbucket.org/blaze-lib/blaze) - High-performance C++ math library for dense and sparse arithmetic.

## Multi-purpose toolkits

- [PETSc](https://petsc.org/release/) - Parallel solution of scientific applications modeled by PDEs.
- [DUNE Numerics](https://www.dune-project.org) - Toolbox for solving PDEs with grid-based methods.
- [SciPy](https://scipy.org) - Python modules for statistics, optimization, integration, linear algebra, etc.
- [NumPy](https://numpy.org/) - Fundamental package needed for scientific computing with Python.
- [DifferentialEquations.jl](https://docs.sciml.ai/DiffEqDocs/stable/) - Toolbox for solving different types of differential equations numerically. (Julia, MIT, [GitHub](https://github.com/SciML/DifferentialEquations.jl))

## Finite Elements

- [FEniCS](https://fenicsproject.org) - Computing platform for solving PDEs in Python and C++.
- [libMesh](https://libmesh.github.io) - Framework for the numerical simulation of PDEs using unstructured discretizations.
- [deal.II](https://dealii.org) - Software library supporting the creation of finite element codes.
- [Netgen/NGSolve](https://ngsolve.org) - High performance multiphysics finite element software.
- [Firedrake](https://www.firedrakeproject.org) - Automated system for the solution of PDEs using the finite element method.
- [MOOSE](https://mooseframework.inl.gov/) - Multiphysics Object Oriented Simulation Environment.
- [MFEM](https://mfem.org) - Free, lightweight, scalable C++ library for finite element methods.
- [SfePy](https://sfepy.org) - Simple Finite Elements in Python.
- [FreeFEM](https://freefem.org) - High level multiphysics-multimesh finite element language.
- [libceed](https://libceed.readthedocs.io/en/latest/index.html) - Code for Efficient Extensible Discretizations.
- [scikit-fem](https://github.com/kinnala/scikit-fem) - Simple finite element assemblers.

## Meshing

### Triangular and tetrahedral meshing

- [Gmsh](https://gmsh.info) - Three-dimensional finite element mesh generator with pre- and post-processing facilities.
- [pygmsh](https://github.com/nschloe/pygmsh) - Python interface for Gmsh.
- [MeshPy](https://mathema.tician.de/software/meshpy/) - Quality triangular and tetrahedral mesh generation.
- [CGAL](https://www.cgal.org) - Algorithms for computational geometry.
- [pygalmesh](https://github.com/meshpro/pygalmesh) - Python interface for CGAL's 3D meshing capabilities.
- [TetGen](https://www.wias-berlin.de/software/index.jsp?id=TetGen) - Quality tetrahedral mesh generator and 3D Delaunay triangulator.
- [Triangle](https://www.cs.cmu.edu/~quake/triangle.html) - Two-dimensional quality mesh generator and Delaunay triangulator.
- [distmesh](https://persson.berkeley.edu/distmesh/) - Simple generator for unstructured triangular and tetrahedral meshes.
- [trimesh](https://trimesh.org) - Loading and using triangular meshes with an emphasis on watertight surfaces.
- [dmsh](https://github.com/meshpro/dmsh) - Simple generator for unstructured triangular meshes, inspired by distmesh.
- [TetWild](https://arxiv.org/abs/1908.03581) - Generate tetrahedral meshes for triangular surface meshes.
- [TriWild](https://cims.nyu.edu/gcl/papers/2019-TriWild.pdf) - Robust triangulation with curve constraints.
- [fTetWild](https://arxiv.org/abs/1908.03581) - Same as TetWild, but faster.
- [SeismicMesh](https://github.com/krober10nd/SeismicMesh) - Parallel 2D/3D triangle/tetrahedral mesh generation with sliver removal.

### Quadrilateral and hexahedral meshing

- [QuadriFlow](https://stanford.edu/~jingweih/papers/quadriflow/) - Scalable and robust quadrangulation from triangulation.

### Mesh tools

- [meshio](https://github.com/nschloe/meshio) - I/O for various mesh formats, file conversion.
- [MOAB](https://sigma.mcs.anl.gov/moab-library/) - Representing and evaluating mesh data.
- [optimesh](https://github.com/meshpro/optimesh) - Triangular mesh smoothing.
- [pmp-library](https://www.pmp-library.org/) - Polygon mesh processing library.
- [Mmg](https://www.mmgtools.org/) - Robust, open-source & multidisciplinary software for remeshing.
- [meshplex](https://github.com/meshpro/meshplex) - Fast tools for simplex meshes.

## Data formats

- [NetCDF](https://www.unidata.ucar.edu/software/netcdf) - Software libraries and data formats for array-oriented scientific data.
- [HDF5](https://www.hdfgroup.org/solutions/hdf5/) - Data model, library, and file format for storing and managing data.
- [XDMF](https://xdmf.org/) - eXtensible Data Model and Format for data from High Performance Computing codes.
- [Zarr](https://zarr.readthedocs.io/en/stable/) - Format for the storage of chunked, compressed, N-dimensional arrays.

## Sparse linear solvers

- [SuperLU](https://portal.nersc.gov/project/sparse/superlu/) - Direct solution of large, sparse, nonsymmetric systems of linear equations.
- [PyAMG](https://pyamg.readthedocs.io/en/latest/) - Algebraic Multigrid Solvers in Python.
- [hypre](https://computing.llnl.gov/projects/hypre-scalable-linear-solvers-multigrid-methods) - Library of high-performance preconditioners and solvers.

## Visualization

- [ParaView](https://www.paraview.org) - Multi-platform data analysis and visualization application based on VTK.
- [VTK](https://vtk.org/) - Process images and create 3D computer graphics.
- [Mayavi](https://docs.enthought.com/mayavi/mayavi/) - 3D scientific data visualization and plotting in Python.
- [Polyscope](https://polyscope.run/) - Viewer and user interface for 3D geometry processing.
- [PyVista](https://docs.pyvista.org/) - 3D plotting and mesh analysis through a streamlined interface for VTK.
- [vedo](https://vedo.embl.es) - Library for scientific analysis and visualization of 3D objects based on VTK.
- [yt](https://yt-project.org/) - Toolkit for analysis and visualization of volumetric data.
- [F3D](https://f3d.app/) - Cross-platform, fast, and minimalist 3D viewer with scientific visualization tools.
- [TTK](https://topology-tool-kit.github.io/) - Topological data analysis and visualization.
- [morphologica](https://github.com/ABRG-Models/morphologica) - Header-only, modern OpenGL code to visualize numerical simulations at runtime. (C++, Apache 2.0, GitHub)

## Other libraries and tools

- [FFTW](http://www.fftw.org) - Discrete Fourier transforms in one or more dimensions, of arbitrary input size, real and complex.
- [Qhull](http://www.qhull.org) - Convex hull, Delaunay triangulation, Voronoi diagram, halfspace intersection about a point, etc.
- [GSL](https://www.gnu.org/software/gsl/) - Random number generators, special functions, and least-squares fitting etc.
- [OpenFOAM](https://www.openfoam.com) - Free, open source CFD (computational fluid dynamics) software.
- [quadpy](https://github.com/sigma-py/quadpy) - Numerical integration (quadrature, cubature) in Python.
- [FiPy](https://www.ctcms.nist.gov/fipy/) - Finite-volume PDE solver.
- [accupy](https://github.com/sigma-py/accupy) - Accurate sums and dot products for Python.
- [SLEPc](https://slepc.upv.es) - Scalable Library for Eigenvalue Problem Computations.
- [Chebfun](https://www.chebfun.org/) - Computing with functions to about 15-digit accuracy.
- [pyMOR](https://pymor.org/) - Model Order Reduction with Python.
- [cvxpy](https://www.cvxpy.org/) - Modeling language for convex optimization problems.
- [PyWavelets](https://pywavelets.readthedocs.io/en/latest/) - Wavelet transforms in Python.
- [NFFT](https://www-user.tu-chemnitz.de/~potts/nfft/) - Nonequispaced fast Fourier transform.
- [preCICE](https://precice.org/) - Coupling library for partitioned multi-physics simulations (FSI, CHT, and more).
- [orthopy](https://github.com/sigma-py/orthopy) - Compute orthogonal polynomials efficiently.
- [pyGAM](https://pygam.readthedocs.io/en/latest/) - Generalized Additive Models in Python.
- [Dedalus](https://dedalus-project.org/) - Solve partial differential equations with spectral methods.
- [PyGMO](https://esa.github.io/pygmo/) - Massively parallel optimization.
- [shenfun](https://shenfun.readthedocs.io/en/latest/) - High-performance Python library for the spectral Galerkin method.
- [PyDMD](https://github.com/mathLab/PyDMD) - Dynamic Mode Decomposition (DMD) in Python.
- [HPDDM](https://github.com/hpddm/hpddm) - High-performance unified framework for domain decomposition methods.

## Community

- [SciComp StackExchange](https://scicomp.stackexchange.com/) - Computational Science on the StackExchange network.
- [Wolfgang Bangerth's video class](https://www.math.colostate.edu/~bangerth/videos.html) - MATH 676: Finite element methods in scientific computing.
- [Nick Higham's blog](https://nhigham.com/) - Mostly on MATLAB, general computing advice.
- [Nick Trefethen's Video Lectures](https://people.maths.ox.ac.uk/trefethen/videos.html) - 36 video lectures on approximation theory/practice and scientific computing.
- [John D. Cook's blog](https://www.johndcook.com/blog/) - Feats of scientific computing.
- [Jack Dongarra's software list](https://netlib.org/utk/people/JackDongarra/la-sw.html) - List of freely available software for the solution of linear algebra problems.
- [NA Digest](https://netlib.org/na-digest-html/) - Collection of articles on topics related to numerical analysis and those who practice it.
- [Gabriel Peyré on Bluesky](https://bsky.app/profile/gabrielpeyre.bsky.social) - One post a day on computational mathematics.
- [Discord: Numerical Software](https://discord.com/invite/hnTJ5MRX2Y) - Discord messaging server on numerical software.

<!-- kb-related:start -->

## Related lists

More lists in the **Miscellaneous** category of the [KEEBOX Library](index.md):

- [Scientific Writing](scientific-writing.md)
- [Scriptable](scriptable.md)
- [Site Reliability Engineering](site-reliability-engineering.md)
- [Software Architecture](software-architecture.md)
- [Readme](readme.md)
- [Research Tools](research-tools.md)
- [REST](rest.md)
- [SAP Commerce](sap-commerce.md)

<!-- kb-related:end -->

#!/bin/bash
export BLISLAB_DIR=.
echo "BLISLAB_DIR = $BLISLAB_DIR"

# Compiler Options (intel, gnu, or clang)
export BLISLAB_COMPILER=clang
echo "BLISLAB_COMPILER = $BLISLAB_COMPILER"

# Whether use BLAS or not?
export BLISLAB_USE_BLAS=true
echo "BLISLAB_USE_BLAS = $BLISLAB_USE_BLAS"

# Optimization Level (O0, O1, O2, O3)
export COMPILER_OPT_LEVEL=O3
echo "COMPILER_OPT_LEVEL = $COMPILER_OPT_LEVEL"

# BLAS installation prefix. Homebrew OpenBLAS installs headers in include/ and
# libraries in lib/ beneath this directory.
export BLAS_DIR=/opt/homebrew/opt/openblas
echo "BLAS_DIR = $BLAS_DIR"

# Parallel Options
export KMP_AFFINITY=compact,verbose
export OMP_NUM_THREADS=1
export BLISLAB_IC_NT=1

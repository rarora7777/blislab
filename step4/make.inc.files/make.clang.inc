CC  = clang
CXX = clang++

ARCH = ar
ARCHFLAGS = cr
RANLIB = ranlib

OMPFLAGS = -Xpreprocessor -fopenmp -I/opt/homebrew/opt/libomp/include
OMPLIBS = -L/opt/homebrew/opt/libomp/lib -lomp

ifeq ($(BLISLAB_USE_BLAS),true)
CFLAGS = -$(COMPILER_OPT_LEVEL) -march=native -fPIC $(OMPFLAGS) -DUSE_BLAS
LDLIBS = $(LIBBLISLAB) -L$(BLAS_DIR)/lib -lopenblas $(OMPLIBS) -lpthread -lm
else
CFLAGS = -$(COMPILER_OPT_LEVEL) -march=native -fPIC $(OMPFLAGS)
LDLIBS = $(LIBBLISLAB) $(OMPLIBS) -lpthread -lm
endif

LIBBLISLAB = $(BLISLAB_DIR)/lib/libblislab.a
SHAREDLIBBLISLAB = $(BLISLAB_DIR)/lib/libblislab.so

LDFLAGS = -I$(BLISLAB_DIR)/include -I$(BLISLAB_DIR)/kernels -I$(BLAS_DIR)/include

OS_NAME = $(shell uname -s)
ifeq ($(OS_NAME),Linux)
LDLIBS += -lrt
endif

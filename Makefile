# Build an executable, standalone version of tweet.py using PyInstaller


# These settings may change based on your system:
# -----------------------------------------------------------------------------
# The python interpreter
PY = python

# Executable file extension
# POSIX: BINARY_EXT =
# Windows: BINARY_EXT = .exe
BINARY_EXT = .exe

# The PyInstaller directory
PYINST = pyinstaller-1.5-rc1
# -----------------------------------------------------------------------------


# PyInstaller scripts
CONFIGURE = $(PYINST)/Configure.py
CONFIGDAT = $(PYINST)/config.dat
MAKESPEC = $(PYINST)/Makespec.py
BUILDER = $(PYINST)/Build.py

# BASENAME is the name of the python script
BASENAME = tweet
SOURCE = $(BASENAME).py
SPECFILE = $(BASENAME).spec

# compiled binary path
BINARY = dist/$(BASENAME)$(BINARY_EXT)

# output files created during build
OUTFILES = build dist warn$(BASENAME).txt $(SPECFILE) *.log

build: $(BINARY)

$(BINARY): $(SPECFILE) $(CONFIGDAT)
	$(PY) "$(BUILDER)" "$(SPECFILE)"

$(CONFIGDAT):
	$(PY) "$(CONFIGURE)"

$(SPECFILE): $(SOURCE) $(CONFIGDAT)
	$(PY) "$(MAKESPEC)" --onefile "$@"

clean:
	rm -rfv $(OUTFILES)

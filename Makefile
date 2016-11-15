current_dir := $(shell pwd)
starlink_dir := $(current_dir)/pycupid/star

unexport STARLINK
unexport INSTALL
export STARCONF_DEFAULT_PREFIX := $(starlink_dir)
export STARCONF_DEFAULT_STARLINK := $(starlink_dir)
export PATH := $(starlink_dir)/bin:$(starlink_dir)/buildsupport/bin:$(PATH)
export FC := gfortran
export F77 := gfortran

all: buildcupid

.PHONY: buildcupid
buildcupid: $(starlink_dir)/bin/cupid

.PHONY: buildsupport
buildsupport: $(starlink_dir)/buildsupport

.PHONY: updatestarlink
updatestarlink: 
	git submodule update --init
	
$(starlink_dir)/buildsupport: updatestarlink
	cd ./starlink && ./bootstrap --buildsupport

$(starlink_dir)/bin/cupid: buildsupport
	cd ./starlink && ./bootstrap
	$(MAKE) -C ./starlink configure-deps
	cd ./starlink && ./configure -C --without-stardocs
	$(MAKE) -C ./starlink $(starlink_dir)/manifests/cupid

.PHONY: clean
clean:
	-rm -rf build/
	-rm -f *.so

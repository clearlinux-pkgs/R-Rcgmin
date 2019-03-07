#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-Rcgmin
Version  : 2013.2.21
Release  : 5
URL      : https://cran.r-project.org/src/contrib/Rcgmin_2013-2.21.tar.gz
Source0  : https://cran.r-project.org/src/contrib/Rcgmin_2013-2.21.tar.gz
Summary  : Conjugate Gradient Minimization of Nonlinear Functions
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-numDeriv
BuildRequires : R-numDeriv
BuildRequires : clr-R-helpers

%description
with box constraints incorporating the Dai/Yuan update. This
        implementation should be used in place of the "CG" algorithm
        of the optim() function.

%prep
%setup -q -c -n Rcgmin

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1530497792

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1530497792
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library Rcgmin
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library Rcgmin
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library Rcgmin
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library Rcgmin|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/Rcgmin/DESCRIPTION
/usr/lib64/R/library/Rcgmin/INDEX
/usr/lib64/R/library/Rcgmin/Meta/Rd.rds
/usr/lib64/R/library/Rcgmin/Meta/demo.rds
/usr/lib64/R/library/Rcgmin/Meta/features.rds
/usr/lib64/R/library/Rcgmin/Meta/hsearch.rds
/usr/lib64/R/library/Rcgmin/Meta/links.rds
/usr/lib64/R/library/Rcgmin/Meta/nsInfo.rds
/usr/lib64/R/library/Rcgmin/Meta/package.rds
/usr/lib64/R/library/Rcgmin/NAMESPACE
/usr/lib64/R/library/Rcgmin/NEWS
/usr/lib64/R/library/Rcgmin/R/Rcgmin
/usr/lib64/R/library/Rcgmin/R/Rcgmin.rdb
/usr/lib64/R/library/Rcgmin/R/Rcgmin.rdx
/usr/lib64/R/library/Rcgmin/demo/broydt_test.R
/usr/lib64/R/library/Rcgmin/demo/cyq_test.R
/usr/lib64/R/library/Rcgmin/demo/genrose_test.R
/usr/lib64/R/library/Rcgmin/help/AnIndex
/usr/lib64/R/library/Rcgmin/help/Rcgmin.rdb
/usr/lib64/R/library/Rcgmin/help/Rcgmin.rdx
/usr/lib64/R/library/Rcgmin/help/aliases.rds
/usr/lib64/R/library/Rcgmin/help/paths.rds
/usr/lib64/R/library/Rcgmin/html/00Index.html
/usr/lib64/R/library/Rcgmin/html/R.css

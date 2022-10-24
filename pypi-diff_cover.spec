#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x972401BDE60128CB (matt.bachmann@lola.com)
#
Name     : pypi-diff_cover
Version  : 7.0.1
Release  : 12
URL      : https://files.pythonhosted.org/packages/d1/4d/8557aab5641b8a524a83b3515f9a49128a4215d06712ebc4132f49d5b4d4/diff_cover-7.0.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/d1/4d/8557aab5641b8a524a83b3515f9a49128a4215d06712ebc4132f49d5b4d4/diff_cover-7.0.1.tar.gz
Source1  : https://files.pythonhosted.org/packages/d1/4d/8557aab5641b8a524a83b3515f9a49128a4215d06712ebc4132f49d5b4d4/diff_cover-7.0.1.tar.gz.asc
Summary  : Run coverage and linting reports on diffs
Group    : Development/Tools
License  : Apache-2.0
Requires: pypi-diff_cover-bin = %{version}-%{release}
Requires: pypi-diff_cover-license = %{version}-%{release}
Requires: pypi-diff_cover-python = %{version}-%{release}
Requires: pypi-diff_cover-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(poetry_core)

%description
diff-cover |pypi-version| |conda-version| |build-status|
========================================================================================

%package bin
Summary: bin components for the pypi-diff_cover package.
Group: Binaries
Requires: pypi-diff_cover-license = %{version}-%{release}

%description bin
bin components for the pypi-diff_cover package.


%package license
Summary: license components for the pypi-diff_cover package.
Group: Default

%description license
license components for the pypi-diff_cover package.


%package python
Summary: python components for the pypi-diff_cover package.
Group: Default
Requires: pypi-diff_cover-python3 = %{version}-%{release}

%description python
python components for the pypi-diff_cover package.


%package python3
Summary: python3 components for the pypi-diff_cover package.
Group: Default
Requires: python3-core
Provides: pypi(diff_cover)
Requires: pypi(chardet)
Requires: pypi(jinja2)
Requires: pypi(pluggy)
Requires: pypi(pygments)

%description python3
python3 components for the pypi-diff_cover package.


%prep
%setup -q -n diff_cover-7.0.1
cd %{_builddir}/diff_cover-7.0.1
pushd ..
cp -a diff_cover-7.0.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1663687457
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-diff_cover
cp %{_builddir}/diff_cover-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-diff_cover/598f87f072f66e2269dd6919292b2934dbb20492 || :
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/diff-cover
/usr/bin/diff-quality

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-diff_cover/598f87f072f66e2269dd6919292b2934dbb20492

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

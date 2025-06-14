#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v27
# autospec commit: 65cf152
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko.becker@kde.org)
#
Name     : kio-admin
Version  : 25.04.2
Release  : 27
URL      : https://download.kde.org/stable/release-service/25.04.2/src/kio-admin-25.04.2.tar.xz
Source0  : https://download.kde.org/stable/release-service/25.04.2/src/kio-admin-25.04.2.tar.xz
Source1  : https://download.kde.org/stable/release-service/25.04.2/src/kio-admin-25.04.2.tar.xz.sig
Source2  : BB463350D6EF31EF.pkey
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause CC0-1.0 FSFAP GPL-2.0 GPL-3.0
Requires: kio-admin-data = %{version}-%{release}
Requires: kio-admin-lib = %{version}-%{release}
Requires: kio-admin-license = %{version}-%{release}
Requires: kio-admin-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : gnupg
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
<!--
SPDX-License-Identifier: CC0-1.0
-->
# Requirements
- Must be installed to /usr! Polkit and DBus hardcode /usr as source for policies and system services
- KIO 5.98 (master at the time of writing)

%package data
Summary: data components for the kio-admin package.
Group: Data

%description data
data components for the kio-admin package.


%package lib
Summary: lib components for the kio-admin package.
Group: Libraries
Requires: kio-admin-data = %{version}-%{release}
Requires: kio-admin-license = %{version}-%{release}

%description lib
lib components for the kio-admin package.


%package license
Summary: license components for the kio-admin package.
Group: Default

%description license
license components for the kio-admin package.


%package locales
Summary: locales components for the kio-admin package.
Group: Default

%description locales
locales components for the kio-admin package.


%prep
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) BB463350D6EF31EF' gpg.status
%setup -q -n kio-admin-25.04.2
cd %{_builddir}/kio-admin-25.04.2
pushd ..
cp -a kio-admin-25.04.2 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1749520164
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake .. -DQT_MAJOR_VERSION=6  -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
pushd ../buildavx2/
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake .. -DQT_MAJOR_VERSION=6  -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1749520164
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kio-admin
cp %{_builddir}/kio-admin-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/kio-admin/3630f1ffcec0e075bf446b88c7b507b1287b571d || :
cp %{_builddir}/kio-admin-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/kio-admin/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0 || :
cp %{_builddir}/kio-admin-%{version}/LICENSES/FSFAP.txt %{buildroot}/usr/share/package-licenses/kio-admin/da20b47077b3106fb65720d6fef309f39043fa60 || :
cp %{_builddir}/kio-admin-%{version}/LICENSES/GPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/kio-admin/3cb34cfc72e87654683f2894299adf912d14b284 || :
cp %{_builddir}/kio-admin-%{version}/LICENSES/GPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/kio-admin/e3bdbf20d43fc066a1b40a64d57d4ae5a31f177f || :
cp %{_builddir}/kio-admin-%{version}/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/kio-admin/7d9831e05094ce723947d729c2a46a09d6e90275 || :
cp %{_builddir}/kio-admin-%{version}/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/kio-admin/7d9831e05094ce723947d729c2a46a09d6e90275 || :
export GOAMD64=v2
pushd ../buildavx2/
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
%find_lang kio5_admin
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/V3/usr/lib64/libexec/kf6/kio-admin-helper
/usr/lib64/libexec/kf6/kio-admin-helper

%files data
%defattr(-,root,root,-)
/usr/share/dbus-1/system-services/org.kde.kio.admin.service
/usr/share/dbus-1/system.d/org.kde.kio.admin.conf
/usr/share/metainfo/org.kde.kio.admin.metainfo.xml
/usr/share/polkit-1/actions/org.kde.kio.admin.policy

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/qt6/plugins/kf6/kfileitemaction/kio-admin.so
/V3/usr/lib64/qt6/plugins/kf6/kio/admin.so
/usr/lib64/qt6/plugins/kf6/kfileitemaction/kio-admin.so
/usr/lib64/qt6/plugins/kf6/kio/admin.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kio-admin/3630f1ffcec0e075bf446b88c7b507b1287b571d
/usr/share/package-licenses/kio-admin/3cb34cfc72e87654683f2894299adf912d14b284
/usr/share/package-licenses/kio-admin/7d9831e05094ce723947d729c2a46a09d6e90275
/usr/share/package-licenses/kio-admin/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0
/usr/share/package-licenses/kio-admin/da20b47077b3106fb65720d6fef309f39043fa60
/usr/share/package-licenses/kio-admin/e3bdbf20d43fc066a1b40a64d57d4ae5a31f177f

%files locales -f kio5_admin.lang
%defattr(-,root,root,-)


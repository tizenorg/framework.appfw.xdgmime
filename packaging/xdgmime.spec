Name:       xdgmime
Summary:    Pkg xdgmime
Version:    0.0.12
Release:    4
Group:      TO_BE/FILLED_IN
License:    TO_BE_FILLED
Source0:    xdgmime-%{version}.tar.gz
Requires(post): /sbin/ldconfig, /bin/chown, /bin/chmod
Requires(postun): /sbin/ldconfig
BuildRequires:  cmake

%description
Package xdgmime 

%package devel
Summary:    Pkg xdgmime (devel)
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
Package xdgmime (devel)

%prep
%setup -q -n %{name}-%{version}

%build
cmake . -DCMAKE_INSTALL_PREFIX=%{_prefix}

make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install
mkdir -p %{buildroot}/usr/share/license
install COPYING %{buildroot}/usr/share/license/%{name}

%post
chmod 644 /usr/lib/libxdgmime.so.1.1.0
/sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
/usr/lib/libxdgmime.so.*
/usr/share/license/%{name}
%manifest xdgmime.manifest

%files devel
%defattr(-,root,root,-)
/usr/include/xdgmime.h
/usr/lib/libxdgmime.so
/usr/lib/pkgconfig/xdgmime.pc


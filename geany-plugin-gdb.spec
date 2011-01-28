# Conditional build:
%bcond_without	nls	# do not use Native Language Support
%bcond_with	gnuld	# assume the C compiler uses GNU ld

Summary:	geany gdb plugin
Summary(pl.UTF-8):	wtyczka dla geany wspierająca gdb
Name:		geany-plugin-gdb
Version:	0.0.2
Release:	1
License:	GPL v2
Group:		Libraries
Source0:	http://plugins.geany.org/geanygdb/geanygdb-%{version}.tar.gz
# Source0-md5:	9e088888ac81c902fa5fe487e147efdf
URL:		http://plugins.geany.org/geanygdb/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	geany-devel >= 0.16
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel >= 2:2.8
BuildRequires:	intltool
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.198
Requires:	gdb
Requires:	geany >= 0.16
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a plugin to provide integrated debugging from Geany using the
GNU debugger (gdb).

%descriptaion -l pl.UTF-8
Ta wtyczka zapewnia zintegrowanie debugownia z Geany dzięki użyciu GNU
debugera (gdb).

%package static
Summary:	geany-plugin-gdb static library
Summary(pl.UTF-8):	Biblioteka statyczna geany-plugin-gdb
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{rel}

%description  static
geany-plugin-gdb static library.

%description static -l pl.UTF-8
Biblioteka statyczna geany-plugin-gdb.

%prep
%setup -q -n geanygdb-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__automake}
%{__autoconf}

%configure \
%{?with_gnuld: --with-gnu-ld} \
%{!?with_nls: --disable-nls}  \
	 --enable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang geanygdb

%clean
rm -rf $RPM_BUILD_ROOT

%files -f geanygdb.lang
%defattr(644,root,root,755)
%attr(755,root,root)%{_bindir}/*
%{_libdir}/geany/*.so
%{_libdir}/geany/*.la

%files static
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/geany/*.a

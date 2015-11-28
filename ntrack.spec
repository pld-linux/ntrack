#
# Conditional build:
%bcond_without	tests	# don't perform "make check"
#
%define		file_ver	%(echo %{version} | tr -d .)
Summary:	Network status tracking made easy for desktop applications
Summary(pl.UTF-8):	Łatwe śledzenie stanu sieci dla aplikacji użytkowych
Name:		ntrack
Version:	0.17
Release:	3
License:	LGPL v3+
Group:		Libraries
Source0:	http://launchpad.net/ntrack/main/%{file_ver}/+download/%{name}-%{file_ver}.tar.gz
# Source0-md5:	93de49925cee052544d66b8cc7fc067a
Patch0:		%{name}-am.patch
URL:		http://launchpad.net/ntrack
BuildRequires:	QtCore-devel >= 4
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	glib2-devel >= 2.0
BuildRequires:	libnl-devel >= 1:3.2.3
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	python-devel >= 2.3.5
BuildRequires:	python-pygobject-devel >= 2.0
BuildRequires:	qt4-build >= 4
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.600
BuildConflicts:	libnl1-devel
Requires:	libnl >= 1:3.2.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ntrack aims to be a lightweight and easy to use library for
application developers that want to get events on network online
status changes such as online, offline or route changes.

%description -l pl.UTF-8
Projekt ntrack ma na celu dostarczenie lekkiej i łatwej w użyciu
biblioteki dla programistów aplikacji chcących otrzymywać zdarzenia
przy zmianach stanu podłączenia do sieci, tzn. podłączenia, odłączenia
lub zmianach trasowania.

%package devel
Summary:	Header files for ntrack library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki ntrack
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-qt4 = %{version}-%{release}

%description devel
Header files for ntrack library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki ntrack.

%package static
Summary:	Static ntrack library
Summary(pl.UTF-8):	Statyczna biblioteka ntrack
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static ntrack library.

%description static -l pl.UTF-8
Statyczna biblioteka ntrack.

%package glib
Summary:	GLib 2 and GObject bindings for ntrack library
Summary(pl.UTF-8):	Wiązania GLib 2 i GObject do biblioteki ntrack
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description glib
GLib 2 and GObject bindings for ntrack library.

%description glib -l pl.UTF-8
Wiązania GLib 2 i GObject do biblioteki ntrack.

%package glib-devel
Summary:	GLib 2 and GObject bindings for ntrack library - header files
Summary(pl.UTF-8):	Wiązania GLib 2 i GObject do biblioteki ntrack - pliki nagłówkowe
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-glib = %{version}-%{release}

%description glib-devel
GLib 2 and GObject bindings for ntrack library - header files.

%description glib-devel -l pl.UTF-8
Wiązania GLib 2 i GObject do biblioteki ntrack - pliki nagłówkowe.

%package glib-static
Summary:	GLib 2 and GObject bindings for ntrack library - static libraries
Summary(pl.UTF-8):	Wiązania GLib 2 i GObject do biblioteki ntrack - biblioteki statyczne
Group:		Development/Libraries
Requires:	%{name}-glib-devel = %{version}-%{release}

%description glib-static
GLib 2 and GObject bindings for ntrack library - static libraries.

%description glib-static -l pl.UTF-8
Wiązania GLib 2 i GObject do biblioteki ntrack - biblioteki statyczne.

%package qt4
Summary:	Qt4 bindings for ntrack library
Summary(pl.UTF-8):	Wiązania Qt4 do biblioteki ntrack
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description qt4
Qt4 bindings for ntrack library.

%description qt4 -l pl.UTF-8
Wiązania Qt4 do biblioteki ntrack.

%package qt4-devel
Summary:	Qt4 bindings for ntrack library - header files
Summary(pl.UTF-8):	Wiązania Qt4 do biblioteki ntrack - pliki nagłówkowe
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-qt4 = %{version}-%{release}

%description qt4-devel
Qt4 bindings for ntrack library - header files.

%description qt4-devel -l pl.UTF-8
Wiązania Qt4 do biblioteki ntrack - pliki nagłówkowe.

%package qt4-static
Summary:	Qt4 bindings for ntrack library - static library
Summary(pl.UTF-8):	Wiązania Qt4 do biblioteki ntrack - biblioteka statyczna
Group:		Development/Libraries
Requires:	%{name}-qt4-devel = %{version}-%{release}

%description qt4-static
Qt4 bindings for ntrack library - static library.

%description qt4-static -l pl.UTF-8
Wiązania Qt4 do biblioteki ntrack - biblioteka statyczna.

%package -n python-ntrack
Summary:	Python bindings for ntrack library
Summary(pl.UTF-8):	Wiązania Pythona do biblioteki ntrack
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}

%description -n python-ntrack
Python bindings for ntrack library.

%description -n python-ntrack -l pl.UTF-8
Wiązania Pythona do biblioteki ntrack.

%prep
%setup -q -n %{name}-%{file_ver}
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
CFLAGS="%{rpmcflags} -std=c99 -D_GNU_SOURCE=1"
%configure

%{__make}

%{?with_tests:%{__make} -j1 check}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -j1 install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/lib*.la
# loadable modules
%{__rm} $RPM_BUILD_ROOT%{_libdir}/ntrack/modules/ntrack-*.{la,a} \
	$RPM_BUILD_ROOT%{py_sitedir}/pyntrack.{la,a}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	glib -p /sbin/ldconfig
%postun	glib -p /sbin/ldconfig

%post	qt4 -p /sbin/ldconfig
%postun	qt4 -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libntrack.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libntrack.so.0
%dir %{_libdir}/ntrack
%dir %{_libdir}/ntrack/modules
%attr(755,root,root) %{_libdir}/ntrack/modules/ntrack-libnl3_x.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libntrack.so
%dir %{_includedir}/ntrack
%{_includedir}/ntrack/common
%{_pkgconfigdir}/libntrack.pc

%files static
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libntrack.a

%files glib
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libntrack-glib.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libntrack-glib.so.2
%attr(755,root,root) %{_libdir}/libntrack-gobject.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libntrack-gobject.so.1

%files glib-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libntrack-glib.so
%attr(755,root,root) %{_libdir}/libntrack-gobject.so
%{_includedir}/ntrack/glib
%{_includedir}/ntrack/gobject
%{_pkgconfigdir}/libntrack-glib.pc
%{_pkgconfigdir}/libntrack-gobject.pc

%files glib-static
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libntrack-glib.a
%attr(755,root,root) %{_libdir}/libntrack-gobject.a

%files qt4
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libntrack-qt4.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libntrack-qt4.so.1

%files qt4-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libntrack-qt4.so
%{_pkgconfigdir}/libntrack-qt4.pc
%{_includedir}/ntrack/qt4

%files qt4-static
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libntrack-qt4.a

%files -n python-ntrack
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/pyntrack.so

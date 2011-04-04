#
%define		_realver	%(echo %{version} | tr -d .)

Summary:	Program
Summary(pl.UTF-8):	Program
Name:		ntrack
Version:	0.14
Release:	2
License:	GPL v3/LGPL v3
Group:		Development/Libraries
Source0:	http://launchpad.net/ntrack/main/014/+download/%{name}-%{_realver}.tar.gz
# Source0-md5:	d8af7c0f77c030d089bfa5ce0dd1057b
Patch0:		%{name}-link.patch
URL:		http://launchpad.net/ntrack
BuildRequires:	QtCore-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libnl-devel >= 1:3.0
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	python-pygobject-devel
BuildRequires:	qt4-build
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.600
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ntrack aims to be a lightweight and easy to use library for
application developers that want to get events on network online
status changes such as online, offline or route changes.

%description -l pl.UTF-8

%package qt4
Summary:	Qt4 bindings for ntrack library
Summary(pl.UTF-8):	Dowiązania qt4 dla  biblioteki ntrack
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description qt4
Qt4 bindings for ntrack library.

%description qt4 -l pl.UTF-8
Dowiązania qt4 dla biblioteki ntrack.

%package -n python-ntrack
Summary:	python bindings for ntrack library
Summary(pl.UTF-8):	Dowiązania python dla  biblioteki ntrack
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description -n python-ntrack
Python bindings for ntrack library.

%description -n python-ntrack -l pl.UTF-8
Dowiązania python dla biblioteki ntrack.

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

%prep
%setup -q -n %{name}-%{_realver}
%patch0 -p1

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -j1 install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig
%post	qt4	-p /sbin/ldconfig
%postun	qt4	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libntrack-glib.so.?
%attr(755,root,root) %{_libdir}/libntrack-glib.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libntrack-gobject.so.?
%attr(755,root,root) %{_libdir}/libntrack-gobject.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libntrack.so.?
%attr(755,root,root) %{_libdir}/libntrack.so.*.*.*
%dir %{_libdir}/ntrack
%dir %{_libdir}/ntrack/modules
%attr(755,root,root) %{_libdir}/ntrack/modules/ntrack-libnl3.so

%files qt4
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libntrack-qt4.so.?
%attr(755,root,root) %{_libdir}/libntrack-qt4.so.*.*.*

%files -n python-ntrack
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/pyntrack.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libntrack-glib.so
%attr(755,root,root) %{_libdir}/libntrack-gobject.so
%attr(755,root,root) %{_libdir}/libntrack-qt4.so
%attr(755,root,root) %{_libdir}/libntrack.so
%{_pkgconfigdir}/libntrack*.pc
%dir %{_includedir}/ntrack
%{_includedir}/ntrack/common
%{_includedir}/ntrack/glib
%{_includedir}/ntrack/gobject
%{_includedir}/ntrack/qt4

%files static
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libntrack-glib.a
%attr(755,root,root) %{_libdir}/libntrack-gobject.a
%attr(755,root,root) %{_libdir}/libntrack-qt4.a
%attr(755,root,root) %{_libdir}/libntrack.a
%attr(755,root,root) %{_libdir}/ntrack/modules/ntrack-libnl3.a
%attr(755,root,root) %{_libdir}/python2.7/site-packages/pyntrack.a

Summary:	Fake Xinerama library for exposing virtual screens to X11 client applications
Summary(pl.UTF-8):	Fałszywa biblioteka Xinerama udostępniająca ekrany wirtualne klientom X11
Name:		libfakeXinerama
Version:	0.1.0
Release:	1
License:	MIT
Group:		X11/Libraries
Source0:	http://xpra.org/src/libfakeXinerama-%{version}.tar.bz2
# Source0-md5:	e49caf9cb96cea1d1f5316062f2e334a
URL:		https://www.xpra.org/trac/wiki/FakeXinerama
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXinerama-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides a fake Xinerama library which can be used to
return pre-defined screen layout information to X11 client
applications which use the Xinerama extension.

%description -l pl.UTF-8
Ten pakiet udostępnia bibliotekę udającą bibliotekę Xinerama, która
może zwracać predefiniowaną informację o układzie ekranu do aplikacji
klienckich X11 wykorzystujących rozszerzenie Xinerama.

%prep
%setup -q

%build
%{__cc} %{rpmcflags} %{rpmcppflags} -fPIC -c fakeXinerama.c
%{__cc} -shared %{rpmldflags} %{rpmcflags} -o libfakeXinerama.so.1.0 fakeXinerama.o -Wl,-soname=libfakeXinerama.so.1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}

install -D libfakeXinerama.so.1.0 $RPM_BUILD_ROOT%{_libdir}
/sbin/ldconfig -n $RPM_BUILD_ROOT%{_libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc LICENSE README.TXT
%attr(755,root,root) %{_libdir}/libfakeXinerama.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libfakeXinerama.so.1

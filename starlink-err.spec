Summary:	MERS - Message and Error Reporting System
Summary(pl.UTF-8):   MERS - system komunikatów i raportowania błędów
Name:		starlink-err
Version:	1.8.218
Release:	1
License:	non-commercial use and distribution (see MERS_CONDITIONS)
Group:		Libraries
Source0:	ftp://ftp.starlink.rl.ac.uk/pub/ussc/store/mers/err.tar.Z
# Source0-md5:	1916d131656da30052c6ca5df3556c84
Patch0:		%{name}-make.patch
URL:		http://www.starlink.rl.ac.uk/static_www/soft_further_MERS.html
BuildRequires:	gcc-g77
BuildRequires:	starlink-pcs-devel
BuildRequires:	starlink-sae-devel
Requires:	starlink-sae
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		stardir		/usr/lib/star

%description
This package contains two Fortran subroutine libraries, MSG and ERR,
which can be used to provide informational text to the user from any
application program. The Message Reporting System, MSG, is used for
reporting non-error information and the Error Reporting System, ERR,
is used specifically for reporting error messages.

%description -l pl.UTF-8
Ten pakiet zawiera dwie biblioteki funkcji fortranowych - MSG i ERR,
które mogą być używane do dostarczania tekstu informacyjnego do
użytkownika z poziomu dowolnej aplikacji. MSG (Message Reporting
System - system raportowania komunikatów) służy do raportowania
informacji nie będących błędami, natomiast ERR (Error Reporting System
- system raportowania błędów) jest używany dla komunikatów błędów.

%package devel
Summary:	Header files for MERS libraries
Summary(pl.UTF-8):   Pliki nagłówkowe bibliotek MERS
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	starlink-pcs-devel

%description devel
Header files for MERS libraries.

%description devel -l pl.UTF-8
Pliki nagłówkowe bibliotek MERS.

%package static
Summary:	Static Starlink MERS libraries
Summary(pl.UTF-8):   Statyczne biblioteki Starlink MERS
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static Starlink MERS libraries.

%description static -l pl.UTF-8
Statyczne biblioteki Starlink MERS.

%prep
%setup -q -c
%patch0 -p1

%build
OPT="%{rpmcflags}" \
SYSTEM=ix86_Linux \
./mk build \
	STARLINK=%{stardir}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{stardir}/help

SYSTEM=ix86_Linux \
./mk install \
	STARLINK=%{stardir} \
	INSTALL=$RPM_BUILD_ROOT%{stardir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc MERS_CONDITIONS mers.news
%{stardir}/dates/*
%docdir %{stardir}/docs
%{stardir}/docs/sun*
%{stardir}/help/fac*
%attr(755,root,root) %{stardir}/share/*.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{stardir}/bin/err_dev
%attr(755,root,root) %{stardir}/bin/err_link*
%{stardir}/include/*

%files static
%defattr(644,root,root,755)
%{stardir}/lib/*.a

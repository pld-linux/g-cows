Summary:	G-Cows
Summary(pl):	G-Cows
Name:		g-cows
Version:	1.4
Release:	1
License:	GPL
Group:		Applications/Console
Source0:	http://www.g-cows.org/download/%{name}-%{version}.tar.gz
# Source0-md5:	1d0eef7bdf1a270531d59b9b99c5cda7
BuildRequires:	automake
BuildRequires:	autoconf
BuildRequires:	bison
BuildRequires:	flex
URL:		http://www.g-cows.org
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
G-Cows is a software project consisting in:
- definition of a scripting language designed for creation of web
  sites;
- interpreter for the scripting language (Cows);
- a makefile generator (Cows-mkgen);

%description -l pl
G-Cows jest projektem, w sklad ktorego wchodzi:
- jezyk skryptowy zaprojektowany do tworzenia stron internetowych;
- interpretator tego jezyka
- generator plikow makefile (Cows-mkgen);

%prep
%setup -q

%build
./bootstrap
CFLAGS="%{rpmcflags}"
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*

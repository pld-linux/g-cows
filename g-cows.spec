Summary:	G-Cows - simple scripting language for web content management
Summary(pl):	G-Cows - prosty jêzyk skryptowy do zarz±dzania tre¶ci± WWW
Name:		g-cows
Version:	1.4
Release:	1
License:	GPL
Group:		Applications/Console
Source0:	http://www.g-cows.org/download/%{name}-%{version}.tar.gz
# Source0-md5:	1d0eef7bdf1a270531d59b9b99c5cda7
URL:		http://www.g-cows.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	flex
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
G-Cows is a software project consisting in:
- definition of a scripting language designed for creation of web
  sites;
- interpreter for the scripting language (Cows);
- a makefile generator (Cows-mkgen);

%description -l pl
G-Cows jest projektem, w sk³ad którego wchodzi:
- jêzyk skryptowy zaprojektowany do tworzenia stron internetowych;
- interpreter tego jêzyka
- generator plików makefile (Cows-mkgen);

%prep
%setup -q

%build
./bootstrap
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

#
# Conditional build:
%bcond_with	tests	# do not perform "make test"
#
%define		pdir	IO
%define		pnam	All
Summary:	IO::All of it to Graham and Damian
Summary(pl.UTF-8):	IO::All - wszystkie IO dla Grahama i Damiana
Name:		perl-IO-All
Version:	0.86
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/IO/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	b257d3f742867825d018e74f5a5d549b
URL:		http://search.cpan.org/dist/IO-All/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-File-ReadBackwards
BuildRequires:	perl-IO-String
BuildRequires:	perl-MLDBM
BuildRequires:	perl-Spiffy >= 0.19
%endif
Requires:	perl-mixin
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
IO::All combines all of the best Perl IO modules into a single Spiffy
object oriented interface to greatly simplify your everyday Perl IO
idioms. It exports a single function called io, which returns a new
IO::All object. And that object can do it all!

The IO::All object is a proxy for IO::File, IO::Dir, IO::Socket,
IO::String, Tie::File and File::ReadBackwards. You can use most of the
methods found in these classes and in IO::Handle (which they all
inherit from). IO::All is easily subclassable. You can override any
methods and also add new methods of your own.

%description -l pl.UTF-8
IO::All łączy wszystkie najlepsze moduły Perla IO w pojedynczy
zorientowany obiektowo interfejs Spiffy, aby znacznie uprościć
codziennie używane idiomy IO. Eksportuje pojedynczą funkcję o nazwie
io, która zwraca nowy obiekt IO::All - i ten obiekt może robić to
wszystko!

Obiekt IO::All to proxy dla IO::File, IO::Dir, IO::Socket, IO::String,
Tie::File i File::ReadBackwards. Można używać większości z metod
obecnych w tych klasach oraz w IO::Handle (z którego one wszystkie
dziedziczą). IO::All może być łatwo użyty jako podklasa. Można
przykryć dowolne metody i dodać nowe, własne.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{perl_vendorlib}/IO/All.pod

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/IO/All.pm
%{perl_vendorlib}/IO/All
%{_mandir}/man3/IO::All*.3pm*

#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	IO
%define	pnam	All
Summary:	IO::All of it to Graham and Damian
Summary(pl):	IO::All - wszystkie IO dla Grahama i Damiana
Name:		perl-IO-All
Version:	0.16
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	f5d6418e461a24528331f246f55c50dc
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Spiffy >= 0.13
BuildRequires:	perl-File-ReadBackwards
%endif
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

%description -l pl
IO::All ³±czy wszystkie najlepsze modu³y Perla IO w pojedynczy
zorientowany obiektowo interfejs Spiffy, aby znacznie upro¶ciæ
codziennie u¿ywane idiomy IO. Eksportuje pojedyncz± funkcjê o nazwie
io, która zwraca nowy obiekt IO::All - i ten obiekt mo¿e robiæ to
wszystko!

Obiekt IO::All to proxy dla IO::File, IO::Dir, IO::Socket, IO::String,
Tie::File i File::ReadBackwards. Mo¿na u¿ywaæ wiêkszo¶ci z metod
obecnych w tych klasach oraz w IO::Handle (z którego one wszystkie
dziedzicz±). IO::All mo¿e byæ ³atwo u¿yty jako podklasa. Mo¿na
przykryæ dowolne metody i dodaæ nowe, w³asne.

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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/IO/All.pm
%{_mandir}/man3/*

#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%include	/usr/lib/rpm/macros.perl
%define	pdir	IO
%define	pnam	All
Summary:	IO::All of it to Graham and Damian
Name:		perl-IO-All
Version:	0.15
Release:	1
# Same as Perl
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	0335ed5c723b8e02c2d700719c8d3fa9
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

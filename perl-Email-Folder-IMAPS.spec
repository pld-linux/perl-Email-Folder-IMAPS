#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Email
%define		pnam	Folder-IMAPS
Summary:	Email::Folder::IMAP - Email::Folder Access to IMAP over SSL Folders
Summary(pl.UTF-8):	Email::Folder::IMAP - Dostęp do folderów IMAP przez SSL za pomocą Email::Folder
Name:		perl-Email-Folder-IMAPS
Version:	1.102
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	38c17bf7c8922a923112c309b98a2325
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Email-Folder-IMAP
BuildRequires:	perl-Email-FolderType-Net
BuildRequires:	perl-Net-IMAP-Simple-SSL
#BuildRequires:	perl-Test-More >= 0.47
BuildRequires:	perl-URI-imaps
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This software adds IMAPS functionality to Email::Folder. Its interface
is identical to the other Email::Folder::Reader subclasses.

%description -l pl.UTF-8
Ta klasa dodaje do Email::Folder wsparcie dla IMAPS. Interfejs jest
identyczny względem innych podklas Email::Folder::Reader.

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
%{perl_vendorlib}/Email/Folder/IMAPS*.pm
%{_mandir}/man3/*

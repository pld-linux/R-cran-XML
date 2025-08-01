%define		ver 3.99
%define		subver	0.18
%define		modulename	XML
Summary:	Tools for parsing and generating XML within R and S-Plus
Name:		R-cran-%{modulename}
Version:	3.99_0.18
Release:	1
License:	GPL
Group:		Applications/Databases
Source0:	http://cran.r-project.org/src/contrib/%{modulename}_%{ver}-%{subver}.tar.gz
# Source0-md5:	8c0fc2a49bb0aeaef88d5c820ad15f96
URL:		http://www.omegahat.org/RSXML
BuildRequires:	R >= 2.8.1
BuildRequires:	texlive-fonts-cmsuper
BuildRequires:	texlive-latex-ae
BuildRequires:	texlive-latex-bibtex
BuildRequires:	texlive-xetex
BuildRequires:	libxml2-devel
BuildRequires:	pkgconfig
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides many approaches for both reading and creating
XML (and HTML) documents (including DTDs), both local and accessible
via HTTP or FTP. It also offers access to an XPath "interpreter".

%prep
%setup -q -c

%build
R CMD build %{modulename}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/R/library/
R CMD INSTALL %{modulename} --library=$RPM_BUILD_ROOT%{_libdir}/R/library/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{modulename}/DESCRIPTION
%{_libdir}/R/library/%{modulename}

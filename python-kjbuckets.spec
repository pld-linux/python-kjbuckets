Summary:	Python extension with new Graph, Set and Mapping types
Summary(pl):	Rozszerzenie Pythona z typami Graph, Set i Mapping
Name:		python-kjbuckets
Version:	2.2
Release:	3
License:	distributable
Group:		Development/Languages/Python
Source0:	http://www.pythonpros.com/arw/kjbuckets/kjb.tar.gz
# Source0-md5:	d700e3782d5c8784dc41251f94b1d09a
Source1:	Makefile.pre.in
Source2:	python-kjb-Setup.in
URL:		http://www.pythonpros.com/arw/kjbuckets/
Icon:		linux-python-small.gif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Requires:	python >= 1.5

%description
Python extension with new Graph, Set and Mapping types.

%description -l pl
Rozszerzenie Pythona z nowymi typami Graph, Set i Mapping.

%prep
%setup -q -n kjb
cp -f %{SOURCE1} .
cp -f %{SOURCE2} Setup.in

%build
%{__make} -f Makefile.pre.in boot
%{__make} OPT="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/python1.5/site-packages
install -m 555 kjbucketsmodule.so $RPM_BUILD_ROOT%{_libdir}/python1.5/site-packages/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc kjbuckets.html
%{_libdir}/python1.5/site-packages/kjbucketsmodule.so

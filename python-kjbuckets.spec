Summary: Python extension with new Graph, Set and Mapping types
Name: python-kjbuckets
Version: 2.2 
Release: 3
Copyright: distributable
Packager: John Eikenbery <jae@ai.uga.edu>
Group: Development/Languages/Python
Source0: kjb.tar.gz
Source1: Makefile.pre.in
Source2: python-kjb-Setup.in
Icon: linux-python-small.gif 
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Requires: python >= 1.5

%description
Python extension with new Graph, Set and Mapping types

%prep
%setup -n kjb
cp $RPM_SOURCE_DIR/Makefile.pre.in .
cp $RPM_SOURCE_DIR/python-kjb-Setup.in Setup.in

%build
%{__make} -f Makefile.pre.in boot
%{__make} "OPT=$RPM_OPT_FLAGS"

%install
mkdir -p $RPM_BUILD_ROOT%{_libdir}/python1.5/site-packages/
install -m 555 kjbucketsmodule.so $RPM_BUILD_ROOT%{_libdir}/python1.5/site-packages/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc kjbuckets.html
%{_libdir}/python1.5/site-packages/kjbucketsmodule.so

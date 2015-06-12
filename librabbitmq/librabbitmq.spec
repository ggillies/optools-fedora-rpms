# spec file for librabbitmq
#
# Copyright (c) 2012-2014 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/3.0/
#
# Please, preserve the changelog entries
#

Name:      librabbitmq
Summary:   Client library for AMQP
Version:   0.5.2
Release:   1%{?dist}
License:   MIT
Group:     System Environment/Libraries
URL:       https://github.com/alanxz/rabbitmq-c

Source0:   https://github.com/alanxz/rabbitmq-c/releases/download/v%{version}/rabbitmq-c-%{version}.tar.gz

BuildRequires: libtool
BuildRequires: openssl-devel
# For tools
BuildRequires: popt-devel
# For man page
BuildRequires: xmlto


%description
This is a C-language AMQP client library for use with AMQP servers
speaking protocol versions 0-9-1.


%package devel
Summary:    Header files and development libraries for %{name}
Group:      Development/Libraries
Requires:   %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains the header files and development libraries
for %{name}.


%package tools
Summary:    Example tools built using the librabbitmq package
Group:      Development/Libraries
Requires:   %{name}%{?_isa} = %{version}

%description tools
This package contains example tools built using %{name}.

It provides:
amqp-consume        Consume messages from a queue on an AMQP server
amqp-declare-queue  Declare a queue on an AMQP server
amqp-delete-queue   Delete a queue from an AMQP server
amqp-get            Get a message from a queue on an AMQP server
amqp-publish        Publish a message on an AMQP server


%prep
%setup -q -n rabbitmq-c-%{version}

# Copy sources to be included in -devel docs.
cp -pr examples Examples


%build
autoreconf -i
%configure \
   --enable-tools \
   --enable-docs  \
   --with-ssl=openssl

# rpath removal
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

make %{_smp_mflags}


%install
make install  DESTDIR="%{buildroot}"

rm %{buildroot}%{_libdir}/%{name}.la


%check
: check .pc is usable
grep @ %{buildroot}%{_libdir}/pkgconfig/librabbitmq.pc && exit 1

: upstream tests
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}
make check


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE-MIT
%{_libdir}/%{name}.so.1*


%files devel
%doc AUTHORS THANKS TODO *.md
%doc Examples
%{_libdir}/%{name}.so
%{_includedir}/amqp*
%{_libdir}/pkgconfig/librabbitmq.pc

%files tools
%{_bindir}/amqp-*
%doc %{_mandir}/man1/amqp-*.1*
%doc %{_mandir}/man7/librabbitmq-tools.7*


%changelog
* Mon Sep 15 2014 Remi Collet <remi@fedoraproject.org> - 0.5.2-1
- update to 0.5.2

* Wed Aug 13 2014 Remi Collet <remi@fedoraproject.org> - 0.5.1-1
- update to 0.5.1
- fix license handling
- move all documentation in devel subpackage

* Tue Apr 15 2014 Remi Collet <remi@fedoraproject.org> - 0.5.0-2
- upstream patch for missing function

* Mon Feb 17 2014 Remi Collet <remi@fedoraproject.org> - 0.5.0-1
- update to 0.5.0
- open https://github.com/alanxz/rabbitmq-c/issues/169 (version is 0.5.1-pre)
- open https://github.com/alanxz/rabbitmq-c/issues/170 (amqp_get_server_properties)

* Mon Jan 13 2014 Remi Collet <remi@fedoraproject.org> - 0.4.1-4
- drop BR python-simplejson

* Tue Jan  7 2014 Remi Collet <remi@fedoraproject.org> - 0.4.1-3
- fix broken librabbitmq.pc, #1039555
- add check for usable librabbitmq.pc

* Thu Jan  2 2014 Remi Collet <remi@fedoraproject.org> - 0.4.1-2
- fix Source0 URL

* Sat Sep 28 2013 Remi Collet <remi@fedoraproject.org> - 0.4.1-1
- update to 0.4.1
- add ssl support

* Thu Aug  1 2013 Remi Collet <remi@fedoraproject.org> - 0.3.0-3
- cleanups

* Wed Mar 13 2013 Remi Collet <remi@fedoraproject.org> - 0.3.0-2
- remove tools from main package

* Wed Mar 13 2013 Remi Collet <remi@fedoraproject.org> - 0.3.0-1
- update to 0.3.0
- create sub-package for tools

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-0.2.git2059570
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Aug 01 2012 Remi Collet <remi@fedoraproject.org> - 0.2-0.1.git2059570
- update to latest snapshot (version 0.2, moved to github)
- License is now MIT

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-0.3.hgfb6fca832fd2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Mar 11 2012 Remi Collet <remi@fedoraproject.org> - 0.1-0.2.hgfb6fca832fd2
- add %%check (per review comment)

* Sat Mar 10 2012 Remi Collet <remi@fedoraproject.org> - 0.1-0.1.hgfb6fca832fd2
- Initial RPM


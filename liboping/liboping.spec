Name:           liboping
Version:        1.6.2
Release:        2%{?dist}
Summary:        C library to generate ICMP echo requests

License:        GPLv2
URL:            http://verplant.org/liboping/
Source0:        http://verplant.org/liboping/files/%{name}-%{version}.tar.bz2

BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
BuildRequires:  ncurses-devel
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
Liboping is a C library to generate ICMP echo requests, better known as
"ping packets". It is intended for use in network monitoring applications
or applications that would otherwise need to fork ping(1) frequently.


%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}

%description devel
This package contains files needed to develop and build software against
liboping, a %{summary}.


%prep
%setup -q


%build
%configure --disable-static
make -C src %{?_smp_mflags}
make -C bindings %{?_smp_mflags} perl/Makefile
cd bindings/perl
%{__perl} Makefile.PL INSTALLDIRS=vendor TOP_BUILDDIR=..
make %{?_smp_mflags}


%install
make -C src install DESTDIR=%{buildroot}
cd bindings/perl
make pure_install PERL_INSTALL_ROOT=%{buildroot}

find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} %{buildroot}/*


%check
LD_LIBRARY_PATH=../../src/.libs make -C bindings/perl test


%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig


%files
%{_bindir}/oping
%{_bindir}/noping
%{_libdir}/liboping.so.*
%{_mandir}/man8/oping.8*
%{_mandir}/man3/Net::Oping.3pm*
%{perl_vendorarch}/*
%exclude %{_libdir}/liboping.la
%doc AUTHORS ChangeLog COPYING README


%files devel
%{_includedir}/oping.h
%{_libdir}/liboping.so
%{_mandir}/man3/liboping.3*
%{_mandir}/man3/ping_construct.3*
%{_mandir}/man3/ping_get_error.3*
%{_mandir}/man3/ping_host_add.3*
%{_mandir}/man3/ping_iterator_get.3*
%{_mandir}/man3/ping_iterator_get_context.3*
%{_mandir}/man3/ping_iterator_get_info.3*
%{_mandir}/man3/ping_send.3*
%{_mandir}/man3/ping_setopt.3*


%changelog
* Thu Oct 24 2013 Lubomir Rintel <lkundrak@v3.sk> - 1.6.2-2
- Bulk sad and useless attempt at consistent SPEC file formatting

* Sat Aug 10 2013 Fabian Affolter <mail@fabian-affolter.ch> - 1.6.2-1
- Updated to latest upstream version 1.6.2

* Sat Aug 10 2013 Fabian Affolter <mail@fabian-affolter.ch> - 1.6.0-1
- Updated to latest upstream version 1.6.0
- Spec file updated

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 1.5.1-8
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 11 2012 Petr Pisar <ppisar@redhat.com> - 1.5.1-5
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jun 15 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.5.1-3
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Dec 04 2010 Lubomir Rintel <lkundrak@v3.sk> - 1.5.1-1
- Bump to later version

* Tue Jun 01 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.3.4-2
- Mass rebuild with perl-5.12.0

* Tue Mar 09 2010 Lubomir Rintel <lkundrak@v3.sk> - 1.3.4-1
- Initial packaging

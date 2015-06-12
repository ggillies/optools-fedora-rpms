Name:           nodejs-packaging
Version:        7
Release:        1%{?dist}
Summary:        RPM Macros and Utilities for Node.js Packaging
BuildArch:      noarch
License:        MIT
URL:            https://fedoraproject.org/wiki/Node.js/Packagers
Source0:        https://fedorahosted.org/released/%{name}/%{name}-fedora-%{version}.tar.xz
ExclusiveArch:  %{nodejs_arches} noarch

#nodejs-devel before 0.10.12 provided these macros and owned /usr/share/node
Requires:       nodejs(engine) >= 0.10.12
Requires:       redhat-rpm-config

%description
This package contains RPM macros and other utilities useful for packaging
Node.js modules and applications in RPM-based distributions.

%prep
%setup -qn %{name}-fedora-%{version}

%build
#nothing to do

%install
install -Dpm0644 macros.nodejs %{buildroot}%{_sysconfdir}/rpm/macros.nodejs
install -Dpm0644 nodejs.attr %{buildroot}%{_rpmconfigdir}/fileattrs/nodejs.attr
install -pm0755 nodejs.prov %{buildroot}%{_rpmconfigdir}/nodejs.prov
install -pm0755 nodejs.req %{buildroot}%{_rpmconfigdir}/nodejs.req
install -pm0755 nodejs-symlink-deps %{buildroot}%{_rpmconfigdir}/nodejs-symlink-deps
install -pm0755 nodejs-fixdep %{buildroot}%{_rpmconfigdir}/nodejs-fixdep
install -Dpm0644 multiver_modules %{buildroot}%{_datadir}/node/multiver_modules

%files
%{_sysconfdir}/rpm/macros.nodejs
%{_rpmconfigdir}/fileattrs/nodejs*.attr
%{_rpmconfigdir}/nodejs*
%{_datadir}/node/multiver_modules
%doc LICENSE

%changelog
* Sun May 25 2014 T.C. Hollingsworth <tchollingsworth@gmail.com> - 7-1
- nodejs-symlink-deps: fix regression preventing multiply versioned modules from
  being symlinked correctly

* Sat May 24 2014 T.C. Hollingsworth <tchollingsworth@gmail.com> - 6-1
- nodejs-fixdep: use real option parsing
- nodejs-fixdep: support modifying optionalDependencies and devDependencies
- req: support the caret operator
- nodejs-symlink-deps: add --force option
- nodejs-symlink-deps: add --build alias for --check
- nodejs-fixdep: support converting to caret dependencies
- nodejs-fixdep: support non-dictionary dependency properties
- multiver_modules: add nan

* Mon Jul 29 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 4-1
- handle cases where the symlink target exists gracefully

* Wed Jul 10 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 3-1
- dependencies and engines can be lists or strings too
- handle unversioned dependencies on multiply versioned modules correctly
  (RHBZ#982798)
- restrict to compatible arches

* Fri Jun 21 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 2-1
- move multiple version list to /usr/share/node
- bump nodejs Requires to 0.10.12
- add Requires: redhat-rpm-config

* Thu Jun 13 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1-1
- initial package

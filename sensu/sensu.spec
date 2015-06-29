# Generated from sensu-0.16.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name sensu
%global sensu_build_commit_ver b58f825

Name: %{gem_name}
Version: 0.16.0
Release: 2%{?dist}
Summary: A monitoring framework
Group: Development/Languages
License: MIT
URL: https://github.com/sensu/sensu
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# Got from https://github.com/sensu/sensu-build/tarball/%{sensu_build_commit_ver}
Source1: sensu-sensu-build-%{sensu_build_commit_ver}.tar.gz
Patch0: sensu-0.16.0-relax-gemspec-dependencies.patch
Patch1: sensu-sensu-build-fix-systemd-unit-binary-paths.patch
BuildRequires: ruby
BuildRequires: rubygems-devel
BuildRequires: systemd
Requires(pre): shadow-utils
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
%if 0%{?el7} > 0
Requires: rubygem(async_sinatra) >= 1.0.0
Requires: rubygem(em-redis-unified) = 0.5.0
Requires: rubygem(multi_json) = 1.10.1
Requires: rubygem(sensu-em) = 2.4.0
Requires: rubygem(sensu-extension) = 1.0.0
Requires: rubygem(sensu-extensions) = 1.0.0
Requires: rubygem(sensu-logger) = 1.0.0
Requires: rubygem(sensu-settings) = 1.2.0
Requires: rubygem(sensu-spawn) = 1.1.0
Requires: rubygem(sensu-transport) = 2.4.0
Requires: rubygem(sinatra) >= 1.3.5
Requires: rubygem(thin) >= 1.5.0
Requires: rubygem(uuidtools) >= 2.1.4
%endif
BuildArch: noarch

%description
A monitoring framework that aims to be simple, malleable, and scalable.


%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
gem unpack %{SOURCE0}

%setup -q -D -T -n  %{gem_name}-%{version}

gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

%patch0

tar -xzf %{SOURCE1}

cd sensu-sensu-build-%{sensu_build_commit_ver}
%patch1
cd ..

%build
# Create the gem as gem install only works on a gem file
gem build %{gem_name}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/


mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
        %{buildroot}%{_bindir}/

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

mkdir -p %{buildroot}%{_unitdir}
rm -f sensu-sensu-build-%{sensu_build_commit_ver}/sensu_configs/systemd/sensu-runsvdir.service
install -p -m 0644 sensu-sensu-build-%{sensu_build_commit_ver}/sensu_configs/systemd/*.service %{buildroot}%{_unitdir}/

mkdir -p %{buildroot}%{_sysconfdir}/sysconfig
install -p -m 0644 sensu-sensu-build-%{sensu_build_commit_ver}/sensu_configs/default/%{name} %{buildroot}%{_sysconfdir}/sysconfig

mkdir -p %{buildroot}%{_sysconfdir}/logrotate.d
install -p -m 0644 sensu-sensu-build-%{sensu_build_commit_ver}/sensu_configs/logrotate.d/%{name} %{buildroot}%{_sysconfdir}/logrotate.d

mkdir -p %{buildroot}%{_sysconfdir}/%{name}
cp -ar sensu-sensu-build-%{sensu_build_commit_ver}/sensu_configs/%{name}/* %{buildroot}%{_sysconfdir}/%{name}

mkdir -p %{buildroot}%{_localstatedir}/log/%{name}

%pre
getent group sensu >/dev/null || groupadd -r sensu
getent passwd sensu >/dev/null || \
    useradd -r -g sensu -d /etc/sensu -s /sbin/nologin \
    -c "Sensu monitoring software" sensu
exit 0

%post
%systemd_post sensu-server.service sensu-client.service sensu-api.service

%preun
%systemd_preun sensu-server.service sensu-client.service sensu-api.service

%postun
%systemd_postun sensu-server.service sensu-client.service sensu-api.service

%files
%dir %{gem_instdir}
%{_bindir}/sensu-server
%{_bindir}/sensu-client
%{_bindir}/sensu-api
%{gem_instdir}/bin
%{gem_libdir}
%{_unitdir}/*.service
%{_sysconfdir}/sysconfig/%{name}
%{_sysconfdir}/logrotate.d/%{name}
%attr(0770, sensu, sensu) %{_sysconfdir}/%{name}
%attr(0770, sensu, sensu) %{_localstatedir}/log/%{name}
%exclude %{gem_cache}
%{gem_spec}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/MIT-LICENSE.txt
%doc %{gem_instdir}/README.md

%files doc
%doc %{gem_docdir}
%{gem_instdir}/%{gem_name}.gemspec
%changelog
* Thu Jun 18 2015 Graeme Gillies <ggillies@redhat.com> - 0.16.0-2
- Corrected spec file macro so explicit dependencies for EL7 are included

* Fri Jan 23 2015 Graeme Gillies <ggillies@redhat.com> - 0.16.0-1
- Initial package

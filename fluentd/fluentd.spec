# Generated from fluentd-0.12.2.gem by gem2rpm -*- rpm-spec -*-
%global gem_name fluentd

Name: %{gem_name}
Version: 0.12.5
Release: 2%{?dist}
Summary: Fluentd event collector
Group: Development/Languages
License: ASL 2.0
URL: http://fluentd.org/
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1: fluentd.service
BuildRequires: ruby(release)
BuildRequires: rubygems-devel 
BuildRequires: ruby >= 1.9.3
BuildRequires: rubygem(test-unit)
BuildRequires: rubygem(rr)
BuildRequires: rubygem(test-unit-rr)
BuildRequires: rubygem(yajl-ruby)
BuildRequires: rubygem(msgpack)
BuildRequires: rubygem(sigdump)
BuildRequires: rubygem(cool.io)
BuildRequires: rubygem(tzinfo)
BuildRequires: rubygem(tzinfo-data)
BuildRequires: rubygem(http_parser.rb)
BuildRequires: rubygem(thread_safe)
BuildRequires: systemd

Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
Requires: rubygem-msgpack
Requires: rubygem-yajl-ruby
Requires: rubygem-cool.io
Requires: rubygem-http_parser.rb
Requires: rubygem-sigdump
Requires: rubygem-tzinfo
Requires: rubygem-tzinfo-data
Requires: rubygem-thread_safe
Requires: rubygem-string-scrub
BuildArch: noarch

%description
Fluentd is an open source data collector designed to scale and simplify log
management. It can collect, process and ship many kinds of data in near
real-time.


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

mkdir -p %{buildroot}%{_sysconfdir}/%{gem_name}
mv %{buildroot}%{gem_instdir}/fluent.conf %{buildroot}%{_sysconfdir}/%{gem_name}

mkdir -p %{buildroot}%{_unitdir}
install -p -m 0644 %{SOURCE1} %{buildroot}%{_unitdir}/

rm -f %{buildroot}%{gem_instdir}/{.gitignore,.travis.yml}

# Run the test suite
%check
pushd .%{gem_instdir}
# Tests disabled on EL due to outdated test-unit
%if 0%{?fedora} > 0
testrb2 -Ilib:test test/**/test_*.rb
%endif
popd

%files
%defattr(-, fluentd, fluentd, -)
%dir %{gem_instdir}
%{_bindir}/fluent-cat
%{_bindir}/fluent-debug
%{_bindir}/fluent-gem
%{_bindir}/fluentd
%{gem_instdir}/bin
%{gem_libdir}
%attr(644, root, root) /%{_unitdir}/fluentd.service
%exclude %{gem_cache}
%{gem_spec}
%dir %{_sysconfdir}/%{gem_name}
%config(noreplace) %{_sysconfdir}/%{gem_name}/fluent.conf
%doc %{gem_instdir}/AUTHORS
%doc %{gem_instdir}/CONTRIBUTING.md
%doc %{gem_instdir}/COPYING
%doc %{gem_instdir}/ChangeLog
%doc %{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md


%files doc
%doc %{gem_docdir}
%{gem_instdir}/Rakefile
%{gem_instdir}/test/
%{gem_instdir}/%{gem_name}.gemspec
%{gem_instdir}/example/*

%pre
getent group fluentd >/dev/null || groupadd -r fluentd
getent passwd fluentd >/dev/null || \
    useradd -r -g fluentd -d /etc/fluentd -s /sbin/nologin \
    -c "Fluentd data collection agent" fluentd
exit 0

%post
%systemd_post fluentd.service

%preun
%systemd_preun fluentd.service

%postun
%systemd_postun fluentd.service

%changelog
* Tue Jun 02 2015 Graeme Gillies <ggillies@redhat.com> - 0.12.5-2
- Fixed file ownership permissions for package

* Mon Feb 16 2015 Graeme Gillies <ggillies@redhat.com> - 0.12.5-1
- Upgraded to 0.12.5

* Mon Jan 05 2015 Graeme Gillies <ggillies@redhat.com> - 0.12.2-1
- Initial package

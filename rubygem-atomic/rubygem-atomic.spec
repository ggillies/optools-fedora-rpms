# Generated from atomic-1.1.8.gem by gem2rpm -*- rpm-spec -*-
%global gem_name atomic

Name: rubygem-%{gem_name}
Version: 1.1.16
Release: 3%{?dist}
Summary: An atomic reference implementation for JRuby, Rubinius, and MRI
Group: Development/Languages
License: ASL 2.0
URL: http://github.com/headius/ruby-atomic
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel 
BuildRequires: ruby-devel 
BuildRequires: rubygem(minitest)
%if 0%{?fedora} <= 20 || 0%{?el7}
Provides: rubygem(%{gem_name}) = %{version}
%endif

%description
An atomic reference implementation for JRuby, Rubinius, and MRI.


%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -c -T
%gem_install -n %{SOURCE0}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%if 0%{?fedora} > 0
mkdir -p %{buildroot}%{gem_extdir_mri}
cp -a .%{gem_extdir_mri}/{gem.build_complete,*.so} %{buildroot}%{gem_extdir_mri}/
%endif

%if 0%{?rhel} >= 7
mkdir -p %{buildroot}%{gem_extdir_mri}/lib/%{gem_name}
cp -pa .%{gem_instdir}/lib/%{gem_name}/* %{buildroot}%{gem_extdir_mri}/lib/%{gem_name}
%endif

# Prevent dangling symlink in -debuginfo (rhbz#878863).
rm -rf %{buildroot}%{gem_instdir}/ext/

# Remove useless shebangs.
sed -i -e '/^#!\/usr\/bin\/env/d' %{buildroot}%{gem_instdir}/examples/*.rb

%check
pushd .%{gem_instdir}
%if 0%{?rhel} >= 7
sed -i "s|require 'minitest/autorun'|require 'test/unit'|" ./test/test_atomic.rb
sed -i "s/MiniTest::Test/Test::Unit::TestCase/" ./test/test_atomic.rb
sed -i "s|assert_raises|assert_raise|" ./test/test_atomic.rb
%endif
ruby -Ilib -e 'Dir.glob "./test/test_*.rb", &method(:require)'
popd


%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.*
%doc %{gem_instdir}/LICENSE
%{gem_libdir}
%{gem_extdir_mri}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/%{gem_name}.gemspec
%{gem_instdir}/examples
%{gem_instdir}/test

%changelog
* Mon May 25 2015 Graeme Gillies <ggillies@redhat.com> - 1.1.16-3
- Added explicit provides for EL7 builds

* Thu Jan 15 2015 Vít Ondruch <vondruch@redhat.com> - 1.1.16-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.2

* Thu Dec 18 2014 Vít Ondruch <vondruch@redhat.com> - 1.1.16-1
- Update to atomic 1.1.16.

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Apr 10 2014 Josef Stribny <jstribny@redhat.com> - 1.1.9-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.1

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon May 13 2013 Vít Ondruch <vondruch@redhat.com> - 1.1.9-1
- Update to atomic 1.1.9.

* Mon May 06 2013 Vít Ondruch <vondruch@redhat.com> - 1.1.8-1
- Initial package

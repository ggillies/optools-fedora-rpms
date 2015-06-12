# Generated from fluent-plugin-add-0.0.3.gem by gem2rpm -*- rpm-spec -*-
%global gem_name fluent-plugin-add

Name: rubygem-%{gem_name}
Version: 0.0.3
Release: 1%{?dist}
Summary: Output filter plugin to add messages
Group: Development/Languages
License: MIT
URL: https://github.com/yu-yamada/fluent-plugin-add
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Patch0: rubygem-fluent-plugin-add-gemspec-include-deps.patch
BuildRequires: ruby(release)
BuildRequires: rubygems-devel 
BuildRequires: ruby
%if 0%{?fedora} > 0
BuildRequires: rubygem-minitest4
%else
BuildRequires: rubygem-minitest
%endif
BuildRequires: rubygem-bundler
BuildRequires: rubygem-rake
BuildRequires: fluentd
Requires: fluentd
BuildArch: noarch
%if 0%{?fedora} <= 20 || 0%{?el7}
Provides: rubygem(%{gem_name}) = %{version}
%endif

%description
Output filter plugin to add messages.


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

rm -f %{buildroot}%{gem_instdir}/.gitignore

# Run the test suite
%check
pushd .%{gem_instdir}
ruby -Ilib:test -e 'Dir.glob "./test/**/test_*.rb", &method(:require)'
popd

%files
%dir %{gem_instdir}
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}
%doc %{gem_instdir}/LICENSE.txt
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/Gemfile

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Rakefile
%{gem_instdir}/test
%{gem_instdir}/%{gem_name}.gemspec

%changelog
* Wed Feb 18 2015 Graeme Gillies <ggillies@redhat.com> - 0.0.3-1
- Initial package

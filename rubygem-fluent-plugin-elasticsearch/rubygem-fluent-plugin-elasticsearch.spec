# Generated from fluent-plugin-elasticsearch-0.7.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name fluent-plugin-elasticsearch

Name: rubygem-%{gem_name}
Version: 0.7.0
Release: 1%{?dist}
Summary: ElasticSearch output plugin for Fluent event collector
Group: Development/Languages
License: MIT
URL: https://github.com/uken/fluent-plugin-elasticsearch
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel 
BuildRequires: ruby 
BuildRequires: fluentd
BuildRequires: rubygem(test-unit)
BuildRequires: rubygem(patron)
BuildRequires: rubygem(elasticsearch)
BuildRequires: rubygem(multipart-post)
Requires: fluentd
Requires: rubygem(elasticsearch)
Requires: rubygem(patron)
BuildArch: noarch
%if 0%{?fedora} <= 20 || 0%{?el7}
Provides: rubygem(%{gem_name}) = %{version}
%endif

%description
ElasticSearch output plugin for Fluent event collector.


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

rm -f %{buildroot}%{gem_instdir}/{.gitignore,.travis.yml}


# Run the test suite
%check
pushd .%{gem_instdir}
# Disabled on EL due to missing dependencies
%if 0%{?fedora} > 0
testrb2 -Ilib test
%endif
popd

%files
%dir %{gem_instdir}
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/History.md
%doc %{gem_instdir}/LICENSE.txt
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/Rakefile
%doc %{gem_instdir}/Gemfile
%doc %{gem_instdir}/%{gem_name}.gemspec
%doc %{gem_instdir}/test

%changelog
* Tue Feb 17 2015 Graeme Gillies <ggillies@redhat.com> - 0.7.0-1
- Initial package

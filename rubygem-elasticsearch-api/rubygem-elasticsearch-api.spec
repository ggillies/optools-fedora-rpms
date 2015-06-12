# Generated from elasticsearch-api-1.0.4.gem by gem2rpm -*- rpm-spec -*-
%global gem_name elasticsearch-api

Name: rubygem-%{gem_name}
Version: 1.0.7
Release: 1%{?dist}
Summary: Ruby API for Elasticsearch
License: ASL 2.0
URL: https://github.com/elasticsearch/elasticsearch-ruby/tree/master/elasticsearch-api
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
%if 0%{?fedora} <= 20 || 0%{?el7}
Requires: ruby(release)
Requires: ruby(rubygems) 
Requires: rubygem(multi_json) 
%endif
BuildRequires: ruby(release)
BuildRequires: rubygems-devel 
BuildRequires: ruby 
BuildArch: noarch
%if 0%{?fedora} <= 20 || 0%{?el7}
Provides: rubygem(%{gem_name}) = %{version}
%endif

%description
Ruby API for Elasticsearch. See the `elasticsearch` gem for full integration.

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

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/test
%exclude %{gem_instdir}/.gitignore
%exclude %{gem_instdir}/Gemfile
%exclude %{gem_instdir}/Rakefile
%exclude %{gem_instdir}/%{gem_name}.gemspec
%exclude %{gem_instdir}/utils
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}
%doc %{gem_instdir}/LICENSE.txt

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md


%changelog
* Mon Mar 23 2015 Steve Traylen <steve.traylen@cern.ch> - 1.0.7-1
- Update source 1.0.7

* Fri Aug 08 2014 Steve Traylen <steve.traylen@cern.ch> - 1.0.4-2
- Use correct timestamped source files.

* Thu Jul 03 2014 Steve Traylen <steve.traylen@cern.ch> - 1.0.4-1
- Initial package

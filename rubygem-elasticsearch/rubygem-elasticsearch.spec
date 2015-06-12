# Generated from elasticsearch-1.0.4.gem by gem2rpm -*- rpm-spec -*-
%global gem_name elasticsearch

Name: rubygem-%{gem_name}
Version: 1.0.8
Release: 1%{?dist}
Summary: Ruby integration for Elasticsearch
Group: Development/Languages
License: ASL 2.0
URL: http://github.com/elasticsearch/elasticsearch-ruby
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
%if 0%{?fc19} || 0%{?fc20} || 0%{?el7}
Requires: ruby(release)
Requires: ruby(rubygems) 
Requires: rubygem(elasticsearch-transport)
Requires: rubygem(elasticsearch-api)
%endif
BuildRequires: ruby(release)
BuildRequires: rubygems-devel 
BuildRequires: ruby 
BuildArch: noarch
%if 0%{?fc19} || 0%{?fc20} || 0%{?el7}
Provides: rubygem(%{gem_name}) = %{version}
%endif

%description
Ruby integration for Elasticsearch (client, API, etc.).

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
%exclude %{gem_instdir}/.gitignore
%exclude %{gem_instdir}/test
%exclude %{gem_instdir}/Rakefile
%exclude %{gem_instdir}/Gemfile
%exclude %{gem_instdir}/%{gem_name}.gemspec
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}
%doc %{gem_instdir}/LICENSE.txt

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md

%changelog
* Mon Mar 23 2015 Steve Traylen  <steve.traylen@cern.ch> - 1.0.8-1
- New upstream

* Thu Aug 07 2014 Steve Traylen  <steve.traylen@cern.ch> - 1.0.4-2
- Use correct time stamp for src file.

* Thu Jul 03 2014 Steve Traylen  <steve.traylen@cern.ch> - 1.0.4-1
- Initial package

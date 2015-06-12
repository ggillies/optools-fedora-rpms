# Generated from elasticsearch-extensions-0.0.15.gem by gem2rpm -*- rpm-spec -*-
%global gem_name elasticsearch-extensions

Name: rubygem-%{gem_name}
Version: 0.0.15
Release: 2%{?dist}
Summary: Extensions for the Elasticsearch Rubygem
Group: Development/Languages
License: ASL 2.0
URL: https://github.com/elasticsearch/elasticsearch-ruby/tree/master/elasticsearch-extensions
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
%if 0%{?fedora} <= 20 || 0%{?el7}
Requires: ruby(release)
Requires: ruby(rubygems) 
Requires: rubygem(ansi) 
Requires: rubygem(ruby-prof) 
%endif
BuildRequires: ruby(release)
BuildRequires: rubygems-devel 
BuildRequires: ruby 
BuildArch: noarch
%if 0%{?fedora} <= 20 || 0%{?el7}
Provides: rubygem(%{gem_name}) = %{version}
%endif

%description
Extensions for the Elasticsearch Rubygem.


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
%exclude %{gem_instdir}/Gemfile
%exclude %{gem_instdir}/Rakefile
%exclude %{gem_instdir}/%{gem_name}.gemspec
%exclude %{gem_instdir}/test
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}
%doc %{gem_instdir}/LICENSE.txt

%files doc
%doc %{gem_instdir}/README.md
%doc %{gem_docdir}

%changelog
* Fri Aug 08 2014 Steve Traylen <steve.traylen@cern.ch> - 0.0.15-2
- Correct timestamp on SOURCE file.

* Thu Jul 03 2014 Steve Traylen <steve.traylen@cern.ch> - 0.0.15-1
- Initial package

# Generated from amqp-1.5.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name amqp

Name: rubygem-%{gem_name}
Version: 1.5.0
Release: 2%{?dist}
Summary: Widely used, feature-rich asynchronous RabbitMQ client with batteries included
Group: Development/Languages
License: Ruby
URL: http://rubyamqp.info
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel 
BuildRequires: ruby 
# BuildRequires: rubygem(rspec) 
# BuildRequires: rubygem(bundler) 
Requires: rubygem(eventmachine)
Requires: rubygem(amq-protocol)
BuildArch: noarch
%if 0%{?fedora} <= 20 || 0%{?el7}
Provides: rubygem(%{gem_name}) = %{version}
%endif

%description
Widely used, feature-rich asynchronous RabbitMQ client with batteries
included.


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

rm -f %{buildroot}%{gem_instdir}/{.gitignore,.rspec,.ruby-version,.travis.yml,.yardopts}


# Run the test suite
%check
pushd .%{gem_instdir}
# Disabled because the tests pull in a lot of dependencies, including rabbitmq
# rspec -Ilib spec
popd

%files
%dir %{gem_instdir}
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}
%doc %{gem_instdir}/Gemfile
%doc %{gem_instdir}/ChangeLog.md

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/docs/08Migration.textile
%doc %{gem_instdir}/docs/AMQP091ModelExplained.textile
%doc %{gem_instdir}/docs/Bindings.textile
%doc %{gem_instdir}/docs/Clustering.textile
%doc %{gem_instdir}/docs/ConnectingToTheBroker.textile
%doc %{gem_instdir}/docs/ConnectionEncryptionWithTLS.textile
%doc %{gem_instdir}/docs/DocumentationGuidesIndex.textile
%doc %{gem_instdir}/docs/Durability.textile
%doc %{gem_instdir}/docs/ErrorHandling.textile
%doc %{gem_instdir}/docs/Exchanges.textile
%doc %{gem_instdir}/docs/GettingStarted.textile
%doc %{gem_instdir}/docs/PatternsAndUseCases.textile
%doc %{gem_instdir}/docs/Queues.textile
%doc %{gem_instdir}/docs/RabbitMQVersions.textile
%doc %{gem_instdir}/docs/RunningTests.textile
%doc %{gem_instdir}/docs/TestingWithEventedSpec.textile
%doc %{gem_instdir}/docs/Troubleshooting.textile
%doc %{gem_instdir}/docs/VendorSpecificExtensions.textile
%doc %{gem_instdir}/docs/diagrams
%{gem_instdir}/spec
%{gem_instdir}/%{gem_name}.gemspec
%{gem_instdir}/examples
%{gem_instdir}/bin
%{gem_instdir}/Rakefile
%{gem_instdir}/repl

%changelog
* Thu Jun 18 2015 Graeme Gillies <ggillies@redhat.com> - 1.5.0-2
- Updated specfile to include missing runtime dependencies

* Tue Jan 27 2015 Graeme Gillies <ggillies@redhat.com> - 1.5.0-1
- Initial package

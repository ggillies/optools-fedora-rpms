%global gem_name shoulda-context

Name: rubygem-%{gem_name}
Version: 1.2.1
Release: 2%{?dist}
Summary: Context framework extracted from Shoulda
Group: Development/Languages
License: MIT
URL: https://github.com/thoughtbot/shoulda-context
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
%if 0%{?fedora} > 0
BuildRequires: rubygem(bundler)
BuildRequires: rubygem(jquery-rails)
BuildRequires: rubygem(minitest)
BuildRequires: rubygem(mocha)
BuildRequires: rubygem(rails)
BuildRequires: rubygem(sass-rails)
BuildRequires: rubygem(sqlite3)
BuildRequires: rubygem(test-unit)
%endif
BuildArch: noarch
%if 0%{?fedora} <= 20 || 0%{?el7}
Provides: rubygem(%{gem_name}) = %{version}
%endif

%description
Shoulda's contexts make it easy to write understandable and maintainable
tests for Test::Unit. It's fully compatible with your existing tests in
Test::Unit, and requires no retooling to use.

Refer to the shoulda gem if you want to know more about using shoulda
with Rails or RSpec.


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

# Fix wrong-file-end-of-line-encoding for rpmlint
sed -i 's/\r$//' MIT-LICENSE

# Remove /usr/bin/env from shebang so RPM doesn't consider this a dependency
sed -i 's|#!/usr/bin/env ruby|#!/usr/bin/ruby|' bin/convert_to_should_syntax

# Remove zero-length developer-only file
rm test/fake_rails_root/vendor/plugins/.keep
sed -i 's|"test/fake_rails_root/vendor/plugins/.keep",||' %{gem_name}.gemspec


%build
# Create the gem as gem install only works on a gem file
gem build %{gem_name}.gemspec

%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
        %{buildroot}%{_bindir}/

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

%check
%if 0%{?fedora} > 0
pushd .%{gem_instdir}
# Remove locks to be able to use system dependencies.
rm gemfiles/*.lock

# Relax mocha and test-unit dependencies.
sed -i '/dependency.*mocha/ s/0.9.10/0.9/' shoulda-context.gemspec
sed -i '/dependency.*test-unit/ s/2.1.0/2.1/' shoulda-context.gemspec

# Get rid of unnecessary dependencies.
sed -i '/dependency.*appraisal/d' shoulda-context.gemspec
sed -i '/dependency.*rails/d' shoulda-context.gemspec
sed -i '/dependency.*rake/d' shoulda-context.gemspec

# Use RoR available in build root.
sed -i '/gem "rails"/ s/, :github=>"rails\/rails", :branch=>"4-1-stable"//' gemfiles/rails_4_1.gemfile

BUNDLE_GEMFILE=gemfiles/test_unit.gemfile bundle exec ruby -Itest -e 'Dir.glob "./test/**/*_test.rb", &method(:require)'
BUNDLE_GEMFILE=gemfiles/minitest_5_x.gemfile bundle exec ruby -Itest -e 'Dir.glob "./test/**/*_test.rb", &method(:require)'
BUNDLE_GEMFILE=gemfiles/rails_4_1.gemfile bundle exec ruby -Itest -e 'Dir.glob "./test/**/*_test.rb", &method(:require)'
popd
%endif

%files
%dir %{gem_instdir}
%doc %{gem_instdir}/MIT-LICENSE
%exclude %{gem_instdir}/.*
%{_bindir}/convert_to_should_syntax
%{gem_instdir}/bin
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/CONTRIBUTING.md
%{gem_instdir}/Appraisals
%{gem_instdir}/Gemfile
%{gem_instdir}/gemfiles
%{gem_instdir}/init.rb
%{gem_instdir}/rails/init.rb
%{gem_instdir}/Rakefile
%{gem_instdir}/shoulda-context.gemspec
%{gem_instdir}/tasks
%{gem_instdir}/test

%changelog
* Mon May 25 2015 Graeme Gillies <ggillies@redhat.com> - 1.2.1-2
- Added explicit provides for EL7 builds
- Disabled tests and associated dependencies for EL7

* Wed Jul 02 2014 Vít Ondruch <vondruch@redhat.com> - 1.2.1-1
- Update to shoulda-context 1.2.1.

* Tue Nov 05 2013 Ken Dreyer <ktdreyer@ktdreyer.com> - 1.1.6-2
- Update to shoulda-context 1.1.6
- Clean up comments
- Remove unnecessary BR: on ruby
- Exclude developer-only files from binary packages

* Tue Aug 27 2013 Ken Dreyer <ktdreyer@ktdreyer.com> - 1.1.5-1
- Initial package

%global debug_package   %{nil}
%global provider        google
%global provider_sub    golang
%global provider_tld    org
%global repo            api
# google.golang.org/api
%global import_path     %{provider}.%{provider_sub}.%{provider_tld}/%{repo}
%global commit          fc402b0d6f2a46ba7dcf0a4606031f45fb82a728
%global shortcommit     %(c=%{commit}; echo ${c:0:7})
%global gg_name         golang-%{provider}-%{provider_sub}-%{repo}

%global gc_rev             e1c259484b495133836706f46319f5897f1e9bf6
%global gc_shortrev        %(r=%{gc_rev}; echo ${r:0:12})
%global gc_provider        google
%global gc_provider_sub    code
%global gc_provider_tld    com
%global gc_repo            google-api-go-client
# code.google.com/p/google-api-go-client
%global gc_import_path     %{gc_provider_sub}.%{gc_provider}.%{gc_provider_tld}/p/%{gc_repo}
%global gc_name            golang-%{gc_provider}%{gc_provider_sub}-%{gc_repo}

Name:           golang-googlecode-google-api-client
Version:        0
Release:        0.6.git%{shortcommit}%{?dist}
Summary:        Go libraries for "new style" Google APIs
License:        BSD
URL:            http://%{import_path}
Source0:        https://github.com/google/google-api-go-client/archive/%{commit}/google-api-go-client-%{shortcommit}.tar.gz
Source1:        https://%{gc_repo}.%{gc_provider}%{gc_provider_sub}.%{gc_provider_tld}/archive/%{gc_rev}.tar.gz
%if 0%{?fedora} >= 19 || 0%{?rhel} >= 7
BuildArch:      noarch
%else
ExclusiveArch:  %{ix86} x86_64 %{arm}
%endif

%description
%{summary}

%package -n %{gc_name}-devel
Requires:       golang >= 1.2.1-3
Requires:       golang(code.google.com/p/goauth2/oauth)
Summary:        Go libraries for "new style" Google APIs
Provides: golang(%{gc_import_path}/adexchangebuyer/v1) = %{version}-%{release}
Provides: golang(%{gc_import_path}/adexchangebuyer/v1.1) = %{version}-%{release}
Provides: golang(%{gc_import_path}/adexchangebuyer/v1.2) = %{version}-%{release}
Provides: golang(%{gc_import_path}/adexchangebuyer/v1.3) = %{version}-%{release}
Provides: golang(%{gc_import_path}/adexchangeseller/v1) = %{version}-%{release}
Provides: golang(%{gc_import_path}/adexchangeseller/v1.1) = %{version}-%{release}
Provides: golang(%{gc_import_path}/admin/directory_v1) = %{version}-%{release}
Provides: golang(%{gc_import_path}/admin/email_migration_v2) = %{version}-%{release}
Provides: golang(%{gc_import_path}/admin/reports_v1) = %{version}-%{release}
Provides: golang(%{gc_import_path}/adsense/v1.2) = %{version}-%{release}
Provides: golang(%{gc_import_path}/adsense/v1.3) = %{version}-%{release}
Provides: golang(%{gc_import_path}/adsense/v1.4) = %{version}-%{release}
Provides: golang(%{gc_import_path}/adsensehost/v4.1) = %{version}-%{release}
Provides: golang(%{gc_import_path}/analytics/v2.4) = %{version}-%{release}
Provides: golang(%{gc_import_path}/analytics/v3) = %{version}-%{release}
Provides: golang(%{gc_import_path}/androidpublisher/v1) = %{version}-%{release}
Provides: golang(%{gc_import_path}/androidpublisher/v1.1) = %{version}-%{release}
Provides: golang(%{gc_import_path}/androidpublisher/v2) = %{version}-%{release}
Provides: golang(%{gc_import_path}/appsactivity/v1) = %{version}-%{release}
Provides: golang(%{gc_import_path}/appstate/v1) = %{version}-%{release}
Provides: golang(%{gc_import_path}/audit/v1) = %{version}-%{release}
Provides: golang(%{gc_import_path}/autoscaler/v1beta2) = %{version}-%{release}
Provides: golang(%{gc_import_path}/bigquery/v2) = %{version}-%{release}
Provides: golang(%{gc_import_path}/blogger/v2) = %{version}-%{release}
Provides: golang(%{gc_import_path}/blogger/v3) = %{version}-%{release}
Provides: golang(%{gc_import_path}/books/v1) = %{version}-%{release}
Provides: golang(%{gc_import_path}/calendar/v3) = %{version}-%{release}
Provides: golang(%{gc_import_path}/civicinfo/us_v1) = %{version}-%{release}
Provides: golang(%{gc_import_path}/civicinfo/v1) = %{version}-%{release}
Provides: golang(%{gc_import_path}/cloudmonitoring/v2beta1) = %{version}-%{release}
Provides: golang(%{gc_import_path}/compute/v1) = %{version}-%{release}
Provides: golang(%{gc_import_path}/content/v2) = %{version}-%{release}
Provides: golang(%{gc_import_path}/coordinate/v1) = %{version}-%{release}
Provides: golang(%{gc_import_path}/customsearch/v1) = %{version}-%{release}
Provides: golang(%{gc_import_path}/datastore/v1beta1) = %{version}-%{release}
Provides: golang(%{gc_import_path}/datastore/v1beta2) = %{version}-%{release}
Provides: golang(%{gc_import_path}/dfareporting/v1) = %{version}-%{release}
Provides: golang(%{gc_import_path}/dfareporting/v1.1) = %{version}-%{release}
Provides: golang(%{gc_import_path}/dfareporting/v1.2) = %{version}-%{release}
Provides: golang(%{gc_import_path}/dfareporting/v1.3) = %{version}-%{release}
Provides: golang(%{gc_import_path}/discovery/v1) = %{version}-%{release}
Provides: golang(%{gc_import_path}/dns/v1beta1) = %{version}-%{release}
Provides: golang(%{gc_import_path}/doubleclickbidmanager/v1) = %{version}-%{release}
Provides: golang(%{gc_import_path}/doubleclicksearch/v2) = %{version}-%{release}
Provides: golang(%{gc_import_path}/drive/v1) = %{version}-%{release}
Provides: golang(%{gc_import_path}/drive/v2) = %{version}-%{release}
Provides: golang(%{gc_import_path}/freebase/v1) = %{version}-%{release}
Provides: golang(%{gc_import_path}/freebase/v1-sandbox) = %{version}-%{release}
Provides: golang(%{gc_import_path}/freebase/v1sandbox) = %{version}-%{release}
Provides: golang(%{gc_import_path}/games/v1) = %{version}-%{release}
Provides: golang(%{gc_import_path}/gamesmanagement/v1management) = %{version}-%{release}
Provides: golang(%{gc_import_path}/gan/v1beta1) = %{version}-%{release}
Provides: golang(%{gc_import_path}/genomics/v1beta) = %{version}-%{release}
Provides: golang(%{gc_import_path}/gmail/v1) = %{version}-%{release}
Provides: golang(%{gc_import_path}/google-api-go-generator) = %{version}-%{release}
Provides: golang(%{gc_import_path}/googleapi) = %{version}-%{release}
Provides: golang(%{gc_import_path}/googleapi/internal/uritemplates) = %{version}-%{release}
Provides: golang(%{gc_import_path}/googleapi/transport) = %{version}-%{release}
Provides: golang(%{gc_import_path}/groupsmigration/v1) = %{version}-%{release}
Provides: golang(%{gc_import_path}/groupssettings/v1) = %{version}-%{release}
Provides: golang(%{gc_import_path}/identitytoolkit/v3) = %{version}-%{release}
Provides: golang(%{gc_import_path}/licensing/v1) = %{version}-%{release}
Provides: golang(%{gc_import_path}/manager/v1beta2) = %{version}-%{release}
Provides: golang(%{gc_import_path}/mapsengine/exp2) = %{version}-%{release}
Provides: golang(%{gc_import_path}/mapsengine/v1) = %{version}-%{release}
Provides: golang(%{gc_import_path}/mirror/v1) = %{version}-%{release}
Provides: golang(%{gc_import_path}/oauth2/v1) = %{version}-%{release}
Provides: golang(%{gc_import_path}/oauth2/v2) = %{version}-%{release}
Provides: golang(%{gc_import_path}/orkut/v2) = %{version}-%{release}
Provides: golang(%{gc_import_path}/pagespeedonline/v1) = %{version}-%{release}
Provides: golang(%{gc_import_path}/plus/v1) = %{version}-%{release}
Provides: golang(%{gc_import_path}/plusdomains/v1) = %{version}-%{release}
Provides: golang(%{gc_import_path}/prediction/v1.2) = %{version}-%{release}
Provides: golang(%{gc_import_path}/prediction/v1.3) = %{version}-%{release}
Provides: golang(%{gc_import_path}/prediction/v1.4) = %{version}-%{release}
Provides: golang(%{gc_import_path}/prediction/v1.5) = %{version}-%{release}
Provides: golang(%{gc_import_path}/prediction/v1.6) = %{version}-%{release}
Provides: golang(%{gc_import_path}/pubsub/v1beta1) = %{version}-%{release}
Provides: golang(%{gc_import_path}/qpxexpress/v1) = %{version}-%{release}
Provides: golang(%{gc_import_path}/replicapool/v1beta1) = %{version}-%{release}
Provides: golang(%{gc_import_path}/reseller/v1) = %{version}-%{release}
Provides: golang(%{gc_import_path}/reseller/v1sandbox) = %{version}-%{release}
Provides: golang(%{gc_import_path}/resourceviews/v1beta1) = %{version}-%{release}
Provides: golang(%{gc_import_path}/siteverification/v1) = %{version}-%{release}
Provides: golang(%{gc_import_path}/spectrum/v1explorer) = %{version}-%{release}
Provides: golang(%{gc_import_path}/sqladmin/v1beta1) = %{version}-%{release}
Provides: golang(%{gc_import_path}/sqladmin/v1beta3) = %{version}-%{release}
Provides: golang(%{gc_import_path}/storage/v1) = %{version}-%{release}
Provides: golang(%{gc_import_path}/storage/v1beta1) = %{version}-%{release}
Provides: golang(%{gc_import_path}/storage/v1beta2) = %{version}-%{release}
Provides: golang(%{gc_import_path}/taskqueue/v1beta1) = %{version}-%{release}
Provides: golang(%{gc_import_path}/taskqueue/v1beta2) = %{version}-%{release}
Provides: golang(%{gc_import_path}/tasks/v1) = %{version}-%{release}
Provides: golang(%{gc_import_path}/translate/v2) = %{version}-%{release}
Provides: golang(%{gc_import_path}/urlshortener/v1) = %{version}-%{release}
Provides: golang(%{gc_import_path}/webfonts/v1) = %{version}-%{release}
Provides: golang(%{gc_import_path}/youtube/v3) = %{version}-%{release}
Provides: golang(%{gc_import_path}/youtubeanalytics/v1) = %{version}-%{release}
Provides: golang(%{gc_import_path}/youtubeanalytics/v1beta1) = %{version}-%{release}

%description -n %{gc_name}-devel
%{summary}

These are auto-generated Go libraries from the Google Discovery Services JSON
description files of the available "new style" Google APIs.

Announcement email:
http://groups.google.com/group/golang-nuts/browse_thread/thread/6c7281450be9a21e

Status: Relative to the other Google API clients, this library is labeled alpha.
Some advanced features may not work. Please file bugs if any problems are found.

Getting started documentation:
    http://code.google.com/p/google-api-go-client/wiki/GettingStarted 

%package -n %{gg_name}-devel
BuildRequires:       golang >= 1.2.1-3
BuildRequires:       golang(golang.org/x/net/context)
# cyclic dep, used in examples
#BuildRequires:       golang(golang.org/x/oauth2)
#BuildRequires:       golang(golang.org/x/oauth2/google)
Requires:       golang >= 1.2.1-3
Requires:       golang(golang.org/x/net/context)
Summary:        Go libraries for "new style" Google APIs
Provides:       golang(%{import_path}/adexchangebuyer/v1.1) = %{version}-%{release}
Provides:       golang(%{import_path}/adexchangebuyer/v1.2) = %{version}-%{release}
Provides:       golang(%{import_path}/adexchangebuyer/v1.3) = %{version}-%{release}
Provides:       golang(%{import_path}/adexchangebuyer/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/adexchangeseller/v1.1) = %{version}-%{release}
Provides:       golang(%{import_path}/adexchangeseller/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/adexchangeseller/v2.0) = %{version}-%{release}
Provides:       golang(%{import_path}/admin/directory_v1) = %{version}-%{release}
Provides:       golang(%{import_path}/admin/email_migration_v2) = %{version}-%{release}
Provides:       golang(%{import_path}/admin/reports_v1) = %{version}-%{release}
Provides:       golang(%{import_path}/adsensehost/v4.1) = %{version}-%{release}
Provides:       golang(%{import_path}/adsense/v1.2) = %{version}-%{release}
Provides:       golang(%{import_path}/adsense/v1.3) = %{version}-%{release}
Provides:       golang(%{import_path}/adsense/v1.4) = %{version}-%{release}
Provides:       golang(%{import_path}/analytics/v2.4) = %{version}-%{release}
Provides:       golang(%{import_path}/analytics/v3) = %{version}-%{release}
Provides:       golang(%{import_path}/androidpublisher/v1.1) = %{version}-%{release}
Provides:       golang(%{import_path}/androidpublisher/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/androidpublisher/v2) = %{version}-%{release}
Provides:       golang(%{import_path}/appsactivity/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/appstate/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/audit/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/autoscaler/v1beta2) = %{version}-%{release}
Provides:       golang(%{import_path}/bigquery/v2) = %{version}-%{release}
Provides:       golang(%{import_path}/blogger/v2) = %{version}-%{release}
Provides:       golang(%{import_path}/blogger/v3) = %{version}-%{release}
Provides:       golang(%{import_path}/books/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/calendar/v3) = %{version}-%{release}
Provides:       golang(%{import_path}/civicinfo/us_v1) = %{version}-%{release}
Provides:       golang(%{import_path}/civicinfo/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/civicinfo/v2) = %{version}-%{release}
Provides:       golang(%{import_path}/cloudlatencytest/v2) = %{version}-%{release}
Provides:       golang(%{import_path}/cloudmonitoring/v2beta1) = %{version}-%{release}
Provides:       golang(%{import_path}/compute/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/container/v1beta1) = %{version}-%{release}
Provides:       golang(%{import_path}/content/v2) = %{version}-%{release}
Provides:       golang(%{import_path}/coordinate/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/customsearch/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/dataflow/v1beta3) = %{version}-%{release}
Provides:       golang(%{import_path}/datastore/v1beta1) = %{version}-%{release}
Provides:       golang(%{import_path}/datastore/v1beta2) = %{version}-%{release}
Provides:       golang(%{import_path}/deploymentmanager/v2beta1) = %{version}-%{release}
Provides:       golang(%{import_path}/dfareporting/v1.1) = %{version}-%{release}
Provides:       golang(%{import_path}/dfareporting/v1.2) = %{version}-%{release}
Provides:       golang(%{import_path}/dfareporting/v1.3) = %{version}-%{release}
Provides:       golang(%{import_path}/dfareporting/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/dfareporting/v2.0) = %{version}-%{release}
Provides:       golang(%{import_path}/discovery/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/dns/v1beta1) = %{version}-%{release}
Provides:       golang(%{import_path}/doubleclickbidmanager/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/doubleclicksearch/v2) = %{version}-%{release}
Provides:       golang(%{import_path}/drive/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/drive/v2) = %{version}-%{release}
Provides:       golang(%{import_path}/examples) = %{version}-%{release}
Provides:       golang(%{import_path}/fitness/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/freebase/v1-sandbox) = %{version}-%{release}
Provides:       golang(%{import_path}/freebase/v1sandbox) = %{version}-%{release}
Provides:       golang(%{import_path}/freebase/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/gamesconfiguration/v1configuration) = %{version}-%{release}
Provides:       golang(%{import_path}/gamesmanagement/v1management) = %{version}-%{release}
Provides:       golang(%{import_path}/games/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/gan/v1beta1) = %{version}-%{release}
Provides:       golang(%{import_path}/genomics/v1beta2) = %{version}-%{release}
Provides:       golang(%{import_path}/genomics/v1beta) = %{version}-%{release}
Provides:       golang(%{import_path}/gmail/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-generator) = %{version}-%{release}
Provides:       golang(%{import_path}/googleapi/internal/uritemplates) = %{version}-%{release}
Provides:       golang(%{import_path}/googleapi/transport) = %{version}-%{release}
Provides:       golang(%{import_path}/googleapi) = %{version}-%{release}
Provides:       golang(%{import_path}/groupsmigration/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/groupssettings/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/identitytoolkit/v3) = %{version}-%{release}
Provides:       golang(%{import_path}/licensing/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/manager/v1beta2) = %{version}-%{release}
Provides:       golang(%{import_path}/mapsengine/exp2) = %{version}-%{release}
Provides:       golang(%{import_path}/mapsengine/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/mirror/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/oauth2/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/oauth2/v2) = %{version}-%{release}
Provides:       golang(%{import_path}/pagespeedonline/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/pagespeedonline/v2) = %{version}-%{release}
Provides:       golang(%{import_path}/plusdomains/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/plus/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/prediction/v1.2) = %{version}-%{release}
Provides:       golang(%{import_path}/prediction/v1.3) = %{version}-%{release}
Provides:       golang(%{import_path}/prediction/v1.4) = %{version}-%{release}
Provides:       golang(%{import_path}/prediction/v1.5) = %{version}-%{release}
Provides:       golang(%{import_path}/prediction/v1.6) = %{version}-%{release}
Provides:       golang(%{import_path}/pubsub/v1beta1) = %{version}-%{release}
Provides:       golang(%{import_path}/qpxexpress/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/replicapoolupdater/v1beta1) = %{version}-%{release}
Provides:       golang(%{import_path}/replicapool/v1beta1) = %{version}-%{release}
Provides:       golang(%{import_path}/replicapool/v1beta2) = %{version}-%{release}
Provides:       golang(%{import_path}/reseller/v1sandbox) = %{version}-%{release}
Provides:       golang(%{import_path}/reseller/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/resourceviews/v1beta1) = %{version}-%{release}
Provides:       golang(%{import_path}/resourceviews/v1beta2) = %{version}-%{release}
Provides:       golang(%{import_path}/siteverification/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/spectrum/v1explorer) = %{version}-%{release}
Provides:       golang(%{import_path}/sqladmin/v1beta1) = %{version}-%{release}
Provides:       golang(%{import_path}/sqladmin/v1beta3) = %{version}-%{release}
Provides:       golang(%{import_path}/storage/v1beta1) = %{version}-%{release}
Provides:       golang(%{import_path}/storage/v1beta2) = %{version}-%{release}
Provides:       golang(%{import_path}/storage/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/tagmanager/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/taskqueue/v1beta1) = %{version}-%{release}
Provides:       golang(%{import_path}/taskqueue/v1beta2) = %{version}-%{release}
Provides:       golang(%{import_path}/tasks/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/translate/v2) = %{version}-%{release}
Provides:       golang(%{import_path}/urlshortener/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/webfonts/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/webmasters/v3) = %{version}-%{release}
Provides:       golang(%{import_path}/youtubeanalytics/v1beta1) = %{version}-%{release}
Provides:       golang(%{import_path}/youtubeanalytics/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/youtube/v3) = %{version}-%{release}

%description -n %{gg_name}-devel
%{summary}

These are auto-generated Go libraries from the Google Discovery Services JSON
description files of the available "new style" Google APIs.

Announcement email:
http://groups.google.com/group/golang-nuts/browse_thread/thread/6c7281450be9a21e

Status: Relative to the other Google API clients, this library is labeled alpha.
Some advanced features may not work. Please file bugs if any problems are found.

Getting started documentation:
    http://code.google.com/p/google-api-go-client/wiki/GettingStarted 

%prep
%setup -q -n %{gc_repo}-%{gc_shortrev} -T -b 1
%setup -q -n google-api-go-client-%{commit}

%build

%install
install -d %{buildroot}/%{gopath}/src/%{import_path}
mv googleapi/internal/uritemplates/LICENSE LICENSE-googleapi-internal-uritemplates
for d in ./*; do
    if [[ -d $d ]]; then
        cp -pav $d %{buildroot}/%{gopath}/src/%{import_path}/
    fi
done

pushd ../%{gc_repo}-%{gc_shortrev}
install -d %{buildroot}/%{gopath}/src/%{gc_import_path}
for d in ./*; do
    if [[ -d $d ]]; then
        cp -pav $d %{buildroot}/%{gopath}/src/%{gc_import_path}/
    fi
done

%files -n %{gg_name}-devel
%doc AUTHORS CONTRIBUTORS LICENSE NOTES README.md TODO
%doc LICENSE-googleapi-internal-uritemplates CONTRIBUTING.md
%{gopath}/src/%{import_path}

%files -n %{gc_name}-devel
%doc AUTHORS CONTRIBUTORS LICENSE NOTES README.md TODO
%{gopath}/src/%{gc_import_path}

%changelog
* Thu Mar 26 2015 jchaloup <jchaloup@redhat.com> - 0-0.6.gitfc402b0
- fix provides
  related: #1141841

* Thu Mar 26 2015 jchaloup <jchaloup@redhat.com> - 0-0.5.gitfc402b0
- add devel subpackage for code.google.com/p/... import path (for back-compatibility)
  related: #1141841

* Fri Jan 23 2015 jchaloup <jchaloup@redhat.com> - 0-0.4.gitfc402b0
- update to fc402b0d6f2a46ba7dcf0a4606031f45fb82a728
  related: #1141841

* Fri Nov 14 2014 Eric Paris <eparis@redhat.com> - 0-0.3.alpha.hg98c781851970
- update to 98c78185197025f935947caac56a7b6d022f89d2

* Mon Sep 15 2014 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0-0.2.alpha.hge1c259484b49
- update to e1c259484b495133836706f46319f5897f1e9bf6
- preserve timestamps of copied files

* Mon Aug 04 2014 Adam Miller <maxamillion@fedoraproject.org> - 0-0.1.alpha.hg0923cdda5b82
- First package for Fedora.

%global debug_package   %{nil}
%global provider        github
%global provider_tld    com
%global project         grafana
%global repo            grafana
# https://github.com/grafana/grafana
%global import_path     %{provider}.%{provider_tld}/%{project}/%{repo}
%global commit          v2.0.2
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

Name:           grafana
Version:        2.0.2
Release:        1%{?dist}
Summary:        Grafana is an open source, feature rich metrics dashboard and graph editor
License:        ASL 2.0
URL:            https://%{import_path}
Source0:        https://%{import_path}/archive/%{commit}/%{repo}-%{shortcommit}.tar.gz
ExclusiveArch:  %{ix86} x86_64 %{arm}

BuildRequires:  golang >= 1.2.1-3
BuildRequires:  golang(github.com/Unknwon/com)
BuildRequires:  golang(github.com/Unknwon/macaron)
BuildRequires:  golang(github.com/Unknwon/macaron/inject)
BuildRequires:  golang(github.com/bradfitz/gomemcache/memcache)
BuildRequires:  golang(github.com/couchbase/go-couchbase)
BuildRequires:  golang(github.com/go-sql-driver/mysql)
BuildRequires:  golang(github.com/go-xorm/core)
BuildRequires:  golang(github.com/go-xorm/xorm)
BuildRequires:  golang(github.com/jtolds/gls)
BuildRequires:  golang(github.com/lib/pq)
BuildRequires:  golang(github.com/lib/pq/oid)
BuildRequires:  golang(github.com/lunny/nodb)
BuildRequires:  golang(github.com/lunny/nodb/config)
BuildRequires:  golang(github.com/macaron-contrib/binding)
BuildRequires:  golang(github.com/macaron-contrib/session)
BuildRequires:  golang(github.com/macaron-contrib/session/mysql)
BuildRequires:  golang(github.com/macaron-contrib/session/postgres)
BuildRequires:  golang(github.com/macaron-contrib/session/redis)
BuildRequires:  golang(github.com/mattn/go-sqlite3)
BuildRequires:  golang(github.com/mattn/go-sqlite3/sqlite3_test)
BuildRequires:  golang(github.com/siddontang/ledisdb/config)
BuildRequires:  golang(github.com/siddontang/ledisdb/ledis)
BuildRequires:  golang(github.com/smartystreets/goconvey/convey)
BuildRequires:  golang(github.com/streadway/amqp)
BuildRequires:  golang(golang.org/x/net/context)
BuildRequires:  golang(golang.org/x/oauth2)
BuildRequires:  golang(google.golang.org/appengine/urlfetch)
BuildRequires:  golang(google.golang.org/appengine)
BuildRequires:  golang(google.golang.org/cloud/compute/metadata)
BuildRequires:  golang(gopkg.in/bufio.v1)
BuildRequires:  golang(gopkg.in/check.v1)
BuildRequires:  golang(gopkg.in/ini.v1)
BuildRequires:  golang(gopkg.in/redis.v2)
BuildRequires:  golang(github.com/gosimple/slug)
BuildRequires:  nodejs-less
BuildRequires: systemd

Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd

Requires:       golang >= 1.2.1-3

%description
Grafana is an open source, feature rich metrics dashboard and graph editor for
Graphite, InfluxDB & OpenTSDB.

%prep
%setup -q -n %{repo}-%{version}
rm -rf Godeps

%build
mkdir -p ./_build/src/github.com/grafana
ln -s $(pwd) ./_build/src/github.com/grafana/grafana
export GOPATH=$(pwd)/_build:%{gopath}
go build -o ./bin/grafana-server main.go
go build -o ./bin/build build.go

# Generate CSS
lessc --include-path=./public/vendor/bootstrap/less:./public/css/less ./public/css/less/bootstrap.dark.less ./public/css/bootstrap.dark.min.css
lessc --include-path=./public/vendor/bootstrap/less:./public/css/less ./public/css/less/bootstrap.light.less ./public/css/bootstrap.light.min.css
lessc --include-path=./public/vendor/bootstrap/less:./public/css/less ./public/css/less/grafana-responsive.less ./public/css/bootstrap-responsive.min.css
cat public/vendor/css/normalize.min.css public/vendor/css/timepicker.css public/vendor/css/spectrum.css public/css/bootstrap.dark.min.css public/css/bootstrap-responsive.min.css public/vendor/css/font-awesome.min.css >> public/css/grafana.dark.min.css
cat public/vendor/css/normalize.min.css public/vendor/css/timepicker.css public/vendor/css/spectrum.css public/css/bootstrap.light.min.css public/css/bootstrap-responsive.min.css public/vendor/css/font-awesome.min.css >> public/css/grafana.light.min.css

%install
# install -d -p %{buildroot}/%{gopath}/src/%{import_path}/
# cp -pav *.go %{buildroot}/%{gopath}/src/%{import_path}/
# cp -rpav pkg public conf tests %{buildroot}/%{gopath}/src/%{import_path}/
install -d -p %{buildroot}%{_datadir}/%{name}
cp -pav *.md %{buildroot}%{_datadir}/%{name}
# cp -rpav benchmarks %{buildroot}/%{gopath}/src/%{import_path}/
cp -rpav docs %{buildroot}%{_datadir}/%{name}
cp -rpav public %{buildroot}%{_datadir}/%{name}
cp -rpav vendor %{buildroot}%{_datadir}/%{name}
install -d -p %{buildroot}%{_sbindir}
cp bin/%{name}-server %{buildroot}%{_sbindir}/
install -d -p %{buildroot}%{_sysconfdir}/%{name}
cp conf/sample.ini %{buildroot}%{_sysconfdir}/%{name}/grafana.ini
cp -rpav conf %{buildroot}%{_datadir}/%{name}
mkdir -p %{buildroot}%{_unitdir}
install -p -m 0644 packaging/rpm/systemd/grafana-server.service %{buildroot}%{_unitdir}/
mkdir -p %{buildroot}%{_sysconfdir}/sysconfig
install -p -m 0644 packaging/rpm/sysconfig/grafana-server %{buildroot}%{_sysconfdir}/sysconfig
install -d -p %{buildroot}%{_sharedstatedir}/%{name}
install -d -p %{buildroot}/var/log/%{name}

%check
mkdir -p ./_build/src/github.com/grafana
ln -s $(pwd) ./_build/src/github.com/grafana/grafana
export GOPATH=$(pwd)/_build:%{gopath}
go test ./pkg/api
go test ./pkg/bus
go test ./pkg/components/apikeygen
go test ./pkg/components/renderer
go test ./pkg/events
go test ./pkg/models
go test ./pkg/plugins
go test ./pkg/services/sqlstore
go test ./pkg/services/sqlstore/migrations
go test ./pkg/setting
go test ./pkg/util

%files
%defattr(-, grafana, grafana, -)
%{_datadir}/%{name}
%exclude %{_datadir}/%{name}/*.md
%exclude %{_datadir}/%{name}/docs
%doc %{_datadir}/%{name}/CHANGELOG.md
%doc %{_datadir}/%{name}/CONTRIBUTING.md
%doc %{_datadir}/%{name}/LICENSE.md
%doc %{_datadir}/%{name}/NOTICE.md
%doc %{_datadir}/%{name}/README.md
%doc %{_datadir}/%{name}/docs
%{_sbindir}/%{name}-server
%{_sysconfdir}/%{name}/grafana.ini
%attr(-, root, root) %{_unitdir}/grafana-server.service
%attr(-, root, root) %{_sysconfdir}/sysconfig/grafana-server
%dir %{_sharedstatedir}/%{name}
%dir /var/log/%{name}

%pre
getent group grafana >/dev/null || groupadd -r grafana
getent passwd grafana >/dev/null || \
    useradd -r -g grafana -d /etc/grafana -s /sbin/nologin \
    -c "Grafana Dashboard" grafana
exit 0

%post
%systemd_post grafana.service

%preun
%systemd_preun grafana.service

%postun
%systemd_postun grafana.service

%changelog
* Tue Apr 14 2015 Graeme Gillies <ggillies@redhat.com> - 0-0.1.gitd4339ae
- First package for Fedora

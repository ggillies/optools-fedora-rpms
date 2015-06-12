Name:           kibana
Version:        3.1.2 
Release:        2%{?dist}
Summary:        Browser-based analytics and search inteface for Elasticsearch

License:        ASL 2.0
URL:            https://www.elastic.co/products/kibana
Source0:        https://download.elastic.co/kibana/kibana/kibana-%{version}.tar.gz

BuildArch:      noarch

%description
Kibana is an open source, browser-based analytics
and search interface to Logstash and other timestamped
datasets stored in ElasticSearch.  Kibana strives to be
easy to get started with, while also being flexible and powerful.

%prep
%setup -q


%build
true


%install
install -D -m 444 index.html %{buildroot}/%{_usr}/share/kibana/index.html
install -D -m 444 favicon.ico %{buildroot}/%{_usr}/share/kibana/favicon.ico

mkdir -p %{buildroot}/%{_usr}/share/kibana/css
install -m 444 css/*.* %{buildroot}/%{_usr}/share/kibana/css

mkdir -p %{buildroot}/%{_usr}/share/kibana/font
install -m 444 font/*.* %{buildroot}/%{_usr}/share/kibana/font

mkdir -p %{buildroot}/%{_usr}/share/kibana/img
install -m 444 img/*.* %{buildroot}/%{_usr}/share/kibana/img

mkdir -p %{buildroot}/%{_usr}/share/kibana/vendor
cp -p -R vendor/* %{buildroot}/%{_usr}/share/kibana/vendor
rm %{buildroot}/%{_usr}/share/kibana/vendor/LICENSE.json

mkdir -p %{buildroot}/%{_usr}/share/kibana/app
cp -p -R app/* %{buildroot}/%{_usr}/share/kibana/app

mkdir -p %{buildroot}/etc/kibana/
install -D -m 444 config.js %{buildroot}/etc/kibana/config.js
ln -s /etc/kibana/config.js %{buildroot}/%{_usr}/share/kibana/config.js


%files
%doc README.md LICENSE.md vendor/LICENSE.json

%{_usr}/share/kibana/
%attr(0644, root, root) %config(noreplace) /etc/kibana/config.js



%changelog
* Fri Jun 05 2015 Graeme Gillies <ggillies@redhat.com> - 3.1.2-2
- Changed permissions on /etc/kibana/config.js to be writable

* Mon Apr 27 2015 Solly Ross <sross@redhat.com> - 3.1.2-1
- Initial Packaging for Kibana 3

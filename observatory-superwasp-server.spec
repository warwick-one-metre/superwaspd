Name:      observatory-superwasp-server
Version:   2.1.1
Release:   0
Url:       https://github.com/warwick-one-metre/superwaspd
Summary:   SuperWASP weather log client for the Warwick one-metre telescope.
License:   GPL-3.0
Group:     Unspecified
BuildArch: noarch
Requires:  python36, python36-Pyro4, python36-astropy, python36-warwick-observatory-common
Requires:  observatory-log-client, %{?systemd_requires}

%description
Part of the observatory software for the Warwick one-meter telescope.

superwaspd is a Pyro frontend for querying the SuperWASP weather log via http.

%build
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_unitdir}
mkdir -p %{buildroot}/var/tmp/daemon_home/astropy

%{__install} %{_sourcedir}/superwaspd %{buildroot}%{_bindir}
%{__install} %{_sourcedir}/superwaspd.service %{buildroot}%{_unitdir}

%post
%systemd_post superwaspd.service

%preun
%systemd_preun superwaspd.service

%postun
%systemd_postun_with_restart superwaspd.service

%files
%defattr(0755,root,root,-)
%{_bindir}/superwaspd
%defattr(-,root,root,-)
%{_unitdir}/superwaspd.service
%dir /var/tmp/daemon_home/astropy

%changelog

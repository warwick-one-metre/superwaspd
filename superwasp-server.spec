Name:      onemetre-superwasp-server
Version:   1.8
Release:   0
Url:       https://github.com/warwick-one-metre/superwaspd
Summary:   SuperWASP weather log client for the Warwick one-metre telescope.
License:   GPL-3.0
Group:     Unspecified
BuildArch: noarch
Requires:  python3, python3-Pyro4, %{?systemd_requires}
BuildRequires: systemd-rpm-macros

%description
Part of the observatory software for the Warwick one-meter telescope.

superwaspd is a Pyro frontend for querying the SuperWASP weather log via http.

%build
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_unitdir}

%{__install} %{_sourcedir}/superwaspd %{buildroot}%{_bindir}
%{__install} %{_sourcedir}/superwaspd.service %{buildroot}%{_unitdir}

%pre
%service_add_pre superwaspd.service

%post
%service_add_post superwaspd.service
%fillup_and_insserv -f -y superwaspd.service

%preun
%stop_on_removal superwaspd.service
%service_del_preun superwaspd.service

%postun
%restart_on_update superwaspd.service
%service_del_postun superwaspd.service

%files
%defattr(0755,root,root,-)
%{_bindir}/superwaspd
%defattr(-,root,root,-)
%{_unitdir}/superwaspd.service

%changelog

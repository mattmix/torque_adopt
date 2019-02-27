Name:           torque_adopt
Version:        1.0
Release:        0%{?dist}
Summary:        Adopts SSH sessions into Torque cgroups.

License:        MIT
URL:            https://github.com/mattmix/torque_adopt
Source0:        https://github.com/mattmix/torque_adopt
BuildArch:      noarch
BuildRoot:      %{_builddir}/%{name}-root

Requires:       python36
Requires:       pam_script


%description
This provides a PAM script and systemd socket activation service to attempt to best place incoming SSH sessions into a Torque managed cgroup for a running job. 


%install
install -D -m 0755 %{_sourcedir}/torque_adopt/torque_adopt %{buildroot}/usr/sbin/torque_adopt
install -D -m 0755 %{_sourcedir}/torque_adopt/torque_adopt_socket %{buildroot}/usr/sbin/torque_adopt_socket
install -D -m 0644 %{_sourcedir}/torque_adopt/torque_adopt.socket %{buildroot}/usr/lib/systemd/system/torque_adopt.socket
install -D -m 0644 %{_sourcedir}/torque_adopt/torque_adopt@.service %{buildroot}/usr/lib/systemd/system/torque_adopt@.service
install -D -m 0644 %{_sourcedir}/torque_adopt/torque_adopt.te %{buildroot}/usr/share/torque_adopt/torque_adopt.te

%files
%{_sbindir}/torque_adopt
%{_sbindir}/torque_adopt_socket
/usr/lib/systemd/system/torque_adopt@.service
/usr/lib/systemd/system/torque_adopt.socket
/usr/share/torque_adopt/torque_adopt.te

%define url_ver	%(echo %{version} | cut -d. -f1,2)
%define _disable_rebuild_configure 1

Name:		xfce4-statusnotifier-plugin
Summary:	A Status Notifier plugin for the Xfce panel
Version:	0.2.3
Release:	2
License:	GPLv2+
Group:		Graphical desktop/Xfce
Url:		https://goodies.xfce.org/projects/panel-plugins/xfce4-statusnotifier-plugin
Source0:	http://archive.xfce.org/src/panel-plugins/xfce4-statusnotifier-plugin/%{url_ver}/xfce4-statusnotifier-plugin-%{version}.tar.bz2
BuildRequires:	intltool
BuildRequires:	pkgconfig(dbusmenu-gtk3-0.4)
BuildRequires:	pkgconfig(gio-2.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(libxfce4panel-2.0)
BuildRequires:	pkgconfig(libxfce4ui-2)
BuildRequires:	pkgconfig(libxfce4util-1.0)
BuildRequires:	pkgconfig(libxfconf-0)
Requires:	xfce4-panel

%description
This plugin provides a panel area for status notifier items (application
indicators).

Applications may use these items to display their status and
interact with user. This technology is a modern alternative to systray and
has the freedesktop.org specification.

%prep
%setup -q

%build
%configure
%make_build

%install
%make_install

# we don't want these
find %{buildroot} -name "*.la" -delete

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS ChangeLog NEWS THANKS
%{_libdir}/xfce4/panel/plugins/libstatusnotifier.so
%{_iconsdir}/hicolor/*/apps/xfce4-statusnotifier-plugin.*
%{_datadir}/xfce4/panel/plugins/statusnotifier.desktop



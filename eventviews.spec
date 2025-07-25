#define git 20240217
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
%define major 6
%define libname %mklibname KPim6EventViews
%define devname %mklibname KPim6EventViews -d

Name: eventviews
Version:	25.04.3
%define is_beta %(if test `echo %{version} |cut -d. -f3` -ge 70; then echo -n 1; else echo -n 0; fi)
%if %{is_beta}
%define ftpdir unstable
%else
%define ftpdir stable
%endif
Release:	%{?git:0.%{git}.}1
%if 0%{?git:1}
Source0:	https://invent.kde.org/pim/eventviews/-/archive/%{gitbranch}/eventviews-%{gitbranchd}.tar.bz2#/eventviews-%{git}.tar.bz2
%else
Source0: http://download.kde.org/%{ftpdir}/release-service/%{version}/src/eventviews-%{version}.tar.xz
%endif
Summary: KDE library for calendar event handling
URL: https://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: cmake(ECM)
BuildRequires: cmake(Qt6)
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(KPim6Libkdepim)
BuildRequires: cmake(Qt6UiTools)
BuildRequires: cmake(KF6CalendarCore)
BuildRequires: cmake(KPim6CalendarSupport)
BuildRequires: cmake(KF6Holidays)
BuildRequires: cmake(KF6Contacts)
BuildRequires: cmake(KF6Service)
BuildRequires: cmake(KF6Completion)
BuildRequires: cmake(KPim6CalendarUtils)
BuildRequires: cmake(KPim6Akonadi)
BuildRequires: cmake(KGantt6)
BuildRequires: boost-devel
BuildRequires: sasl-devel
# For QCH format docs
BuildRequires: doxygen
BuildRequires: qt6-qttools-assistant
BuildSystem:	cmake
BuildOption:	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON
# Renamed 2025/07/20 after 6.0
%rename plasma6-eventviews

%description
KDE library for calendar event handling.

%package -n %{libname}
Summary: KDE library for calendar event handling
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{libname}
KDE library for calendar handling.

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

%files -f %{name}.lang
%{_datadir}/qlogging-categories6/eventviews.categories
%{_datadir}/qlogging-categories6/eventviews.renamecategories

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/*

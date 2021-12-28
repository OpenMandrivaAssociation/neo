Name: neo
Summary: Simulates the digital rain from "The Matrix" (cmatrix clone with 32-bit color and Unicode support)
Version: 0.6
Release: 1
License: GPLv3
Group:   Graphical desktop/Other
URL:      https://github.com/st3w/neo
Source0: https://github.com/st3w/neo/releases/download/v%{version}/%{name}-%{version}.tar.gz
# Upstream: https://github.com/st3w/neo/issues/2
Patch0: https://github.com/st3w/neo/commit/0650f17254f920c96aeeabd16a78ce7032d02e30.patch

BuildRequires: pkgconfig(ncursesw)

%description
neo recreates the digital rain effect from "The Matrix". Streams of random characters will endlessly scroll down your terminal screen.

%prep
%autosetup -p0

%build
%configure
%make_build

%install
%make_install

%files
%license COPYING
%doc NEWS
%{_bindir}/neo
%{_mandir}/man6/neo.6*

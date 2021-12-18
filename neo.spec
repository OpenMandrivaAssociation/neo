Name: neo
Summary: Simulates the digital rain from "The Matrix" (cmatrix clone with 32-bit color and Unicode support)
Version: 0.6
Release: 1
License: GPLv3
Group:   Graphical desktop/Other
Source0: https://github.com/st3w/neo/releases/download/v%{version}/%{name}-%{version}.tar.gz
URL:      https://github.com/st3w/neo


BuildRequires: pkgconfig(ncursesw)

%description
neo recreates the digital rain effect from "The Matrix". Streams of random characters will endlessly scroll down your terminal screen.

%prep
%autosetup -p1

%build
./autogen.sh
%configure
%make_build

%install
%make_install

%files
%license COPYING
%doc NEWS
%{_bindir}/neo
%{_mandir}/man6/neo.6*
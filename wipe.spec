# $Log: wipe.spec,v $
# Revision 1.1  1999-12-07 09:09:42  kravietz
# - created wipe spec
# 9958639531e1a0c42b11832b4c43fac9  wipe.spec
#
Summary:	Cryptographically secure file wiping utility
Summary(pl):	Narzêdzie do kryptograficznie bezpiecznego kasowania plików
Name:		wipe
Version:	0.15
Release:	1
Copyright:	GPL
Group:		X11/Utilities
Group(pl):	X11/Narzêdzia
Source:		http://gsu.linux.org.tr/wipe/%{name}-%{version}.tar.gz
URL:		http://gsu.linux.org.tr/wipe/
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Wipe is a tool for cryptographically secure file deletion from magnetic
media, to prevent using advanced recovery techniques like magnetic force
microscopy (MFM). Wipe will repeadetly overwrites special patterns to
the files to be  destroyed, using the fsync() call and/or the O_SYNC bit
to force disk access. In normal mode, 34 patterns are used (of  which
8 are random).

%description -l pl
Wipe jest narzêdziem, s³u¿±cym do kryptograficznie bezpiecznego kasowania
plików z no¶ników magnetycznych tak, by uniemo¿liwiæ próby ich odtworzenia
przy pomocy zaawansowanych technik takich jak mikroskopia magnetyczna
MFM. Wipe wielokrotnie nadpisuje dany plik specjalnymi maskami, u¿ywaj±c
fsync() i/lub bitu O_SYNC dla zapewnienia dostêpu do dysku. W normalnym
trybie wipe u¿ywa 34 masek, z których 8 jest losowych.

%prep
%setup -q

%build
make %{_os}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}}

install -m 711 -s wipe $RPM_BUILD_ROOT%{_bindir}
install -m 644 wipe.1.bz2 $RPM_BUILD_ROOT%{_mandir}/man1

bzip2 -9nf $RPM_BUILD_ROOT%{_mandir}/man1/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BUGS CHANGES README secure_del.html

%attr(711,root,root) %{_bindir}/wipe
%{_mandir}/man1/*

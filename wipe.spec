Summary:	Cryptographically secure file wiping utility
Summary(pl):	Narzêdzie do kryptograficznie bezpiecznego kasowania plików
Name:		wipe
Version:	0.16
Release:	1
License:	GPL
Group:		Utilities/File
Group(pl):	Narzêdzia/Pliki
Source:		http://gsu.linux.org.tr/wipe/%{name}-%{version}.tar.gz
URL:		http://gsu.linux.org.tr/wipe/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Wipe is a tool for cryptographically secure file deletion from magnetic
media, to prevent using advanced recovery techniques like magnetic force
microscopy (MFM). Wipe will repeadetly overwrites special patterns to
the files to be  destroyed, using the fsync() call and/or the O_SYNC bit
to force disk access. In normal mode, 34 patterns are used (of which
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
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install -s wipe $RPM_BUILD_ROOT%{_bindir}
install wipe.1 $RPM_BUILD_ROOT%{_mandir}/man1

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/* \
	BUGS CHANGES README secure_del.html

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz

%attr(755,root,root) %{_bindir}/wipe
%{_mandir}/man1/*

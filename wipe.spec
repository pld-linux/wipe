Summary:	Cryptographically secure file wiping utility
Summary(pl.UTF-8):	Narzędzie do kryptograficznie bezpiecznego kasowania plików
Name:		wipe
Version:	0.20
Release:	3
License:	GPL v2
Group:		Applications/File
Source0:	http://abaababa.ouvaton.org/wipe/%{name}-%{version}.tar.gz
# Source0-md5:	dbf3027f46d014dc899a1cdf2ed93d00
Patch0:		%{name}-Makefile.patch
URL:		http://abaababa.ouvaton.org/wipe/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Wipe is a tool for cryptographically secure file deletion from
magnetic media, to prevent using advanced recovery techniques like
magnetic force microscopy (MFM). Wipe will repeadetly overwrites
special patterns to the files to be destroyed, using the fsync() call
and/or the O_SYNC bit to force disk access. In normal mode, 34
patterns are used (of which 8 are random).

%description -l pl.UTF-8
Wipe jest narzędziem, służącym do kryptograficznie bezpiecznego
kasowania plików z nośników magnetycznych tak, by uniemożliwić próby
ich odtworzenia przy pomocy zaawansowanych technik takich jak
mikroskopia magnetyczna MFM. Wipe wielokrotnie nadpisuje dany plik
specjalnymi maskami, używając fsync() i/lub bitu O_SYNC dla
zapewnienia dostępu do dysku. W normalnym trybie wipe używa 34 masek,
z których 8 jest losowych.

%prep
%setup -q
%patch -P0 -p1

%build
%{__make} \
	%{_os} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}" 

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install wipe $RPM_BUILD_ROOT%{_bindir}
install wipe.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BUGS CHANGES README secure_del.html
%attr(755,root,root) %{_bindir}/wipe
%{_mandir}/man1/*

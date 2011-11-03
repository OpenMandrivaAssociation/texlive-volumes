# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/volumes
# catalog-date 2007-03-01 21:27:41 +0100
# catalog-license lppl
# catalog-version 1.0
Name:		texlive-volumes
Version:	1.0
Release:	1
Summary:	Typeset only parts of a document, with complete indexes etc
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/volumes
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/volumes.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/volumes.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/volumes.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
This package helps you if you want to produce separate printed
volumes from one LaTeX document, as well as one comprehensive,
"all-inclusive" version. It suppresses the part of the table of
contents that are not typeset, while counters, definitions,
index entries etc. are kept consistent throughout the input
file.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/volumes/nowtoaux.sty
%{_texmfdistdir}/tex/latex/volumes/volumes.sty
%doc %{_texmfdistdir}/doc/latex/volumes/README
%doc %{_texmfdistdir}/doc/latex/volumes/volumes.pdf
#- source
%doc %{_texmfdistdir}/source/latex/volumes/volumes.dtx
%doc %{_texmfdistdir}/source/latex/volumes/volumes.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}

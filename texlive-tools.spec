# revision 34051
# category Package
# catalog-ctan /macros/latex/required/tools
# catalog-date 2014-05-14 23:49:31 +0200
# catalog-license lppl1.3
# catalog-version undef
Name:		texlive-tools
Version:	20140514
Release:	1
Summary:	The LaTeX standard tools bundle
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/required/tools
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tools.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tools.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tools.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A collection of (variously) simple tools provided as part of
the LaTeX required tools distribution, comprising the packages:
afterpage, array, bm, calc, dcolumn, delarray, enumerate,
fileerr, fontsmpl, ftnright, hhline, indentfirst, layout,
longtable, multicol, rawfonts, showkeys, somedefs, tabularx,
theorem, trace, varioref, verbatim, xr, and xspace.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/tools/.tex
%{_texmfdistdir}/tex/latex/tools/afterpage.sty
%{_texmfdistdir}/tex/latex/tools/array.sty
%{_texmfdistdir}/tex/latex/tools/bm.sty
%{_texmfdistdir}/tex/latex/tools/calc.sty
%{_texmfdistdir}/tex/latex/tools/dcolumn.sty
%{_texmfdistdir}/tex/latex/tools/delarray.sty
%{_texmfdistdir}/tex/latex/tools/e.tex
%{_texmfdistdir}/tex/latex/tools/enumerate.sty
%{_texmfdistdir}/tex/latex/tools/fontsmpl.sty
%{_texmfdistdir}/tex/latex/tools/fontsmpl.tex
%{_texmfdistdir}/tex/latex/tools/ftnright.sty
%{_texmfdistdir}/tex/latex/tools/h.tex
%{_texmfdistdir}/tex/latex/tools/hhline.sty
%{_texmfdistdir}/tex/latex/tools/indentfirst.sty
%{_texmfdistdir}/tex/latex/tools/layout.sty
%{_texmfdistdir}/tex/latex/tools/longtable.sty
%{_texmfdistdir}/tex/latex/tools/multicol.sty
%{_texmfdistdir}/tex/latex/tools/q.tex
%{_texmfdistdir}/tex/latex/tools/r.tex
%{_texmfdistdir}/tex/latex/tools/rawfonts.sty
%{_texmfdistdir}/tex/latex/tools/s.tex
%{_texmfdistdir}/tex/latex/tools/showkeys.sty
%{_texmfdistdir}/tex/latex/tools/somedefs.sty
%{_texmfdistdir}/tex/latex/tools/tabularx.sty
%{_texmfdistdir}/tex/latex/tools/thb.sty
%{_texmfdistdir}/tex/latex/tools/thc.sty
%{_texmfdistdir}/tex/latex/tools/thcb.sty
%{_texmfdistdir}/tex/latex/tools/theorem.sty
%{_texmfdistdir}/tex/latex/tools/thm.sty
%{_texmfdistdir}/tex/latex/tools/thmb.sty
%{_texmfdistdir}/tex/latex/tools/thp.sty
%{_texmfdistdir}/tex/latex/tools/trace.sty
%{_texmfdistdir}/tex/latex/tools/varioref.sty
%{_texmfdistdir}/tex/latex/tools/verbatim.sty
%{_texmfdistdir}/tex/latex/tools/verbtest.tex
%{_texmfdistdir}/tex/latex/tools/x.tex
%{_texmfdistdir}/tex/latex/tools/xr.sty
%{_texmfdistdir}/tex/latex/tools/xspace.sty
%doc %{_texmfdistdir}/doc/latex/tools/00readme.txt
%doc %{_texmfdistdir}/doc/latex/tools/afterpage.pdf
%doc %{_texmfdistdir}/doc/latex/tools/array.pdf
%doc %{_texmfdistdir}/doc/latex/tools/bm.pdf
%doc %{_texmfdistdir}/doc/latex/tools/calc.pdf
%doc %{_texmfdistdir}/doc/latex/tools/changes.txt
%doc %{_texmfdistdir}/doc/latex/tools/dcolumn.pdf
%doc %{_texmfdistdir}/doc/latex/tools/delarray.pdf
%doc %{_texmfdistdir}/doc/latex/tools/enumerate.pdf
%doc %{_texmfdistdir}/doc/latex/tools/fileerr.pdf
%doc %{_texmfdistdir}/doc/latex/tools/fontsmpl.pdf
%doc %{_texmfdistdir}/doc/latex/tools/ftnright.pdf
%doc %{_texmfdistdir}/doc/latex/tools/hhline.pdf
%doc %{_texmfdistdir}/doc/latex/tools/indentfirst.pdf
%doc %{_texmfdistdir}/doc/latex/tools/layout.pdf
%doc %{_texmfdistdir}/doc/latex/tools/longtable.pdf
%doc %{_texmfdistdir}/doc/latex/tools/manifest.txt
%doc %{_texmfdistdir}/doc/latex/tools/multicol.pdf
%doc %{_texmfdistdir}/doc/latex/tools/rawfonts.pdf
%doc %{_texmfdistdir}/doc/latex/tools/showkeys.pdf
%doc %{_texmfdistdir}/doc/latex/tools/somedefs.pdf
%doc %{_texmfdistdir}/doc/latex/tools/tabularx.pdf
%doc %{_texmfdistdir}/doc/latex/tools/theorem.pdf
%doc %{_texmfdistdir}/doc/latex/tools/tools.pdf
%doc %{_texmfdistdir}/doc/latex/tools/trace.pdf
%doc %{_texmfdistdir}/doc/latex/tools/varioref.pdf
%doc %{_texmfdistdir}/doc/latex/tools/verbatim.pdf
%doc %{_texmfdistdir}/doc/latex/tools/xr.pdf
%doc %{_texmfdistdir}/doc/latex/tools/xspace.pdf
#- source
%doc %{_texmfdistdir}/source/latex/tools/afterpage.dtx
%doc %{_texmfdistdir}/source/latex/tools/afterpage.ins
%doc %{_texmfdistdir}/source/latex/tools/array.dtx
%doc %{_texmfdistdir}/source/latex/tools/bm.dtx
%doc %{_texmfdistdir}/source/latex/tools/bm.ins
%doc %{_texmfdistdir}/source/latex/tools/calc.dtx
%doc %{_texmfdistdir}/source/latex/tools/dcolumn.dtx
%doc %{_texmfdistdir}/source/latex/tools/delarray.dtx
%doc %{_texmfdistdir}/source/latex/tools/enumerate.dtx
%doc %{_texmfdistdir}/source/latex/tools/fileerr.dtx
%doc %{_texmfdistdir}/source/latex/tools/fontsmpl.dtx
%doc %{_texmfdistdir}/source/latex/tools/ftnright.dtx
%doc %{_texmfdistdir}/source/latex/tools/hhline.dtx
%doc %{_texmfdistdir}/source/latex/tools/indentfirst.dtx
%doc %{_texmfdistdir}/source/latex/tools/layout.dtx
%doc %{_texmfdistdir}/source/latex/tools/longtable.dtx
%doc %{_texmfdistdir}/source/latex/tools/longtable.ins
%doc %{_texmfdistdir}/source/latex/tools/multicol.dtx
%doc %{_texmfdistdir}/source/latex/tools/multicol.ins
%doc %{_texmfdistdir}/source/latex/tools/rawfonts.dtx
%doc %{_texmfdistdir}/source/latex/tools/showkeys.dtx
%doc %{_texmfdistdir}/source/latex/tools/somedefs.dtx
%doc %{_texmfdistdir}/source/latex/tools/tabularx.dtx
%doc %{_texmfdistdir}/source/latex/tools/tabularx.ins
%doc %{_texmfdistdir}/source/latex/tools/theorem.dtx
%doc %{_texmfdistdir}/source/latex/tools/tools.ins
%doc %{_texmfdistdir}/source/latex/tools/trace.dtx
%doc %{_texmfdistdir}/source/latex/tools/varioref.dtx
%doc %{_texmfdistdir}/source/latex/tools/varioref.ins
%doc %{_texmfdistdir}/source/latex/tools/verbatim.dtx
%doc %{_texmfdistdir}/source/latex/tools/xr.dtx
%doc %{_texmfdistdir}/source/latex/tools/xspace.dtx

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}

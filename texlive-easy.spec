Name:		texlive-easy
Version:	19440
Release:	2
Summary:	A collection of easy-to-use macros
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/easy
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/easy.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/easy.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The collection comprises: - easybib, support for customising
bibliographies; - easybmat, support for composing block
matrices; - easyeqn, support for various aspects of equations;
- easymat, support for composing matrices; - easytable, support
for writing tables; - easyvector, a C-like syntax for writing
vectors.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/easy/easy.sty
%{_texmfdistdir}/tex/latex/easy/easybib.sty
%{_texmfdistdir}/tex/latex/easy/easybmat.sty
%{_texmfdistdir}/tex/latex/easy/easyeqn.sty
%{_texmfdistdir}/tex/latex/easy/easymat.sty
%{_texmfdistdir}/tex/latex/easy/easytable.sty
%{_texmfdistdir}/tex/latex/easy/easyvector.sty
%doc %{_texmfdistdir}/doc/latex/easy/README
%doc %{_texmfdistdir}/doc/latex/easy/README.TEXLIVE
%doc %{_texmfdistdir}/doc/latex/easy/for-latex2html/easybib.perl
%doc %{_texmfdistdir}/doc/latex/easy/for-latex2html/easybmat.perl
%doc %{_texmfdistdir}/doc/latex/easy/for-latex2html/easyeqn.perl
%doc %{_texmfdistdir}/doc/latex/easy/for-latex2html/easymat.perl
%doc %{_texmfdistdir}/doc/latex/easy/for-latex2html/easytable.perl
%doc %{_texmfdistdir}/doc/latex/easy/for-latex2html/easyvector.perl
%doc %{_texmfdistdir}/doc/latex/easy/mydoc.sty

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}

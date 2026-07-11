%global tl_name easy
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.99
Release:	%{tl_revision}.1
Summary:	A collection of easy-to-use macros
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/easy
License:	lppl1
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/easy.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/easy.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The collection comprises: easybib, support for customising
bibliographies; easybmat, support for composing block matrices; easyeqn,
support for various aspects of equations; easymat, support for composing
matrices; easytable, support for writing tables; easyvector, a C-like
syntax for writing vectors.


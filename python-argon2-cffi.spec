%define module argon2-cffi
%define uname argon2_cffi

Name:		python-argon2-cffi
Version:	23.1.0
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/a/%{module}/%{uname}-%{version}.tar.gz
Summary:	The Argon2 password hashing algorithm for Python
URL:		https://pypi.org/project/argon2-cffi/
License:	MIT
Group:		Development/Python
BuildSystem:	python
BuildArch:	noarch

BuildRequires:	python
BuildRequires:	pkgconfig(python3)
BuildRequires:	pkgconfig(libargon2)
BuildRequires:	python-setuptools
BuildRequires:	python-setuptools_scm
BuildRequires:	python-flit-core
BuildRequires:	python-hatchling
BuildRequires:	python-hatch-fancy-pypi-readme
BuildRequires:	python-hatch-vcs

Requires:	python-argon2-cffi-bindings
Requires:	python-typing-extensions

%description
The Argon2 password hashing algorithm for Python.

%prep
%autosetup -p1 -n %{uname}-%{version}

%build
export LDFLAGS="%{optflags} -v"
export ARGON2_CFFI_USE_SYSTEM=1
%py_build

%install
%py3_install

%files
%{py_sitedir}/argon2/*.py
%{py_sitedir}/argon2/*.typed
%{py_sitedir}/argon2/*/*.pyc
%{py_sitedir}/%{uname}-%{version}*dist-info/
%doc README.md
%license LICENSE

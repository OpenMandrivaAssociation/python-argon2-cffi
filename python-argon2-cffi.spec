%define module argon2-cffi
%define oname argon2_cffi

Name:		python-argon2-cffi
Version:	25.1.0
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/a/%{module}/%{oname}-%{version}.tar.gz#/%{name}-%{version}.tar.gz
Summary:	The Argon2 password hashing algorithm for Python
URL:		https://pypi.org/project/argon2-cffi/
License:	MIT
Group:		Development/Python
BuildSystem:	python
BuildArch:	noarch
BuildRequires:	python
BuildRequires:	pkgconfig(python3)
BuildRequires:	pkgconfig(libargon2)
BuildRequires:	python%{pyver}dist(flit-core)
BuildRequires:	python%{pyver}dist(hatchling)
BuildRequires:	python%{pyver}dist(hatch-vcs)
BuildRequires:	python%{pyver}dist(hatch-fancy-pypi-readme)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(setuptools-scm)
BuildRequires:	python%{pyver}dist(wheel)

%description
The Argon2 password hashing algorithm for Python.

%build -p
export LDFLAGS="%{ldflags} -v"
export ARGON2_CFFI_USE_SYSTEM=1

%files
%doc README.md
%license LICENSE
%{py_sitedir}/argon2/
%{py_sitedir}/%{oname}-%{version}.dist-info/

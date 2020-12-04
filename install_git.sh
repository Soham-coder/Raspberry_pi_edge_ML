#!/bin/bash
command -v git >/dev/null 2>&1 ||
{ echo >&2 "Git is not installed. Installing..";
  sudo apt install git
}
echo "Git version installed"
git --version
#!/bin/sh
if [ -z "$1" ]
  pages_dir = $1
then
  echo "Using default directory "assets" to deploy to GitHub Pages?"
  pages_dir = "assets"
fi
git subtree push --prefix $pages_dir origin gh-pages
#!/bin/sh -e

SymfonyDir=.
SymfonyWebDir=$SymfonyDir/web
UserName=xbox
Host=azine.me
RemoteBaseDir=/media/data/azine/webApp

echo "clearing symfony cache"
rm $SymfonyDir/cache/* -rf

echo "sync-ing files"
rsync -rltzqv --delete --exclude-from ./rsync_exclude.txt -e ssh $SymfonyDir $User@$Host:$RemoteBaseDir
rsync -rltzqv --delete --exclude-from ./rsync_exclude.txt -e ssh $SymfonyWebDir $User@$Host:$RemoteBaseDir/$SymfonyWebDir



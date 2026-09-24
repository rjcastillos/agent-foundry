##create tar 
tar -czf ~/foundry.tar.gz -T files.txt
tar -tzf  ~/foundry.tar.gz
##extract tar
##asume the tarball is in the repo root and
## this is in the homme directory
cd ~/agent-foundry
tar -xzf foundry.tar.gz 

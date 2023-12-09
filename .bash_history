ssh-keygen -t rsa
mkdir -p ./git/repository/project.git
ll
git init --bare ./project.git/
ll
cd repository
chown -R git:git project.git/
ll
cat id_rsa.pub
cd .ssh
cat id_rsa.pub
cd
mkdir gittest
git init
ll
ls
rm -rf git
rm -rf project.git
ls
vim readme.txt
git add readme.txt
git commit -m "说明"
git status
git diff readme.txt
git log
git log --pretty=oneline
git branch
git branch --set-upstream-to=origin/<branch>
git status
git config --list
git config user.name git
git config user.email 1905815025@qq.com
git config --list
git status
git diff readme.txt
git log
git log --pretty=oneline
git reset --hard HEAD^
git reset --hard^^
git reflog
git add readme.txt
git commit
git reset HEAD readme.txt
git reset --hard HEAD^
git rm readme.txt
git commit -m '删除了readme.txt'
git checkout -- readme.txt
ls
cd gittest
ls
cd
git checkout -- readme.txt
git -version
git --version
add remote add Project "自己创建的ssh,页面会提示"
git add remote add Project "自己创建的ssh,页面会提示"
git remote add Project "自己创建的ssh,界面会提示"
git push -u Project master
git remote add Project https://github.com/1905815025why/Project.git
git push -u Project master
git status
ls
git init
ll
ls
cd gittest
vim readme.txt
git add readme.txt
git commit -m "说明"
git status
git push -u Project master
git remote add origin https://github.com/1905815025why/Project.git
  git branch -M main
  git push -u origin main
git remove -v
git remote -v
git remote add Project https://github.com/1905815025why/Project.git
git status
git add readme.txt
git commit
git push -u Project master

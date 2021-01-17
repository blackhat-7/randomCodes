# If you come from bash you might have to change your $PATH.
# export PATH=$HOME/bin:/usr/local/bin:$PATH
export LD_LIBRARY_PATH="/usr/local/lib/:$LD_LIBRARY_PATH"

# Path to your oh-my-zsh installation.
export ZSH="/Users/macbookpro/.oh-my-zsh"
fpath+=$HOME/.zsh/pure

# OhMyZsh theme
ZSH_THEME="robbyrussell"

# Zsh Plugins
plugins=(
    archlinux
    git
    history-substring-search
    colored-man-pages
)
source $ZSH/oh-my-zsh.sh

# User configuration

autoload -U promptinit; promptinit
prompt pure


# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$('/Users/macbookpro/anaconda3/bin/conda' 'shell.zsh' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "/Users/macbookpro/anaconda3/etc/profile.d/conda.sh" ]; then
        . "/Users/macbookpro/anaconda3/etc/profile.d/conda.sh"
    else
        export PATH="/Users/macbookpro/anaconda3/bin:$PATH"
    fi
fi
unset __conda_setup
# <<< conda initialize <<<


[ -f ~/.fzf.zsh ] && source ~/.fzf.zsh
export FZF_DEFAULT_OPS="--extended"
export FZF_DEFAULT_COMMAND="fd --type f"
export FZF_CTRL_T_COMMAND="$FZF_DEFAULT_COMMAND"
source /Users/macbookpro/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh
export PATH="/usr/local/opt/ruby/bin:$PATH"
export JAVA_HOME=/Library/Java/JavaVirtualMachines/adoptopenjdk-11.jdk/Contents/Home
export HOMEBREW_NO_AUTO_UPDATE=1

# Aliases
alias zshconfig="nvim ~/.zshrc"
alias ohmyzsh="nvim ~/.oh-my-zsh"
alias push="git add -A && git commit -m 'Update' && git push"
alias dmg="cd ~/Documents/sem5/DMG"
alias ml="cd ~/Documents/sem5/ML"
alias cn="cd ~/Documents/sem5/CN"
alias tcom="cd ~/Documents/sem5/TCOM"
alias py="cd ~/Documents/randomCodes/python"
alias ds="cd ~/Documents/randomCodes/DataScience"
alias js="cd ~/Documents/randomCodes/js"
export PATH="/usr/local/sbin:$PATH"
export PATH="/Users/macbookpro/Library/Python/3.8/bin:$PATH"

# Custom commands to run at terminal startup
conda activate py37

import os
l_str = '''
# Set default shell to zsh
# set-option -g default-shell /bin/zsh

# Use the following line to fix OS X tmux problems
# set-option -g default-command "reattach-to-user-namespace -l zsh"

# List of plugins
set -g @plugin 'tmux-plugins/tpm'
set -g @plugin 'tmux-plugins/tmux-sensible'
set -g @plugin 'tmux-plugins/tmux-resurrect'
set -g @plugin 'tmux-plugins/tmux-continuum'

# Other examples:
# set -g @plugin 'github_username/plugin_name'
# set -g @plugin 'git@github.com/user/plugin'
# set -g @plugin 'git@bitbucket.com/user/plugin'

# Enable automatic restore
set -g @continuum-restore 'on'

# Initialize TMUX plugin manager (keep this line at the very bottom of tmux.conf)
run '~/.tmux/plugins/tpm/tpm'
'''
home = os.path.expanduser('~')
with open(home+"/"+file_name,"w") as fp:
    fp.write(l_str)

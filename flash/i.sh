wget http://fpdownload.macromedia.com/pub/flashplayer/updaters/11/flashplayer_11_plugin_debug.i386.tar.gz
tar -zxvf flashplayer_11_plugin_debug.i386.tar.gz
mkdir -p ~/.mozilla/plugins
mv *.so ~/.mozilla/plugins

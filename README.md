Pyrista will use Arista's Pyeapi and Bokeh visuals to do NetOps and get visualizations.

1) Make sure Pyeapi is activated on the switch first. 
```
%>en
en>management api http-commands
```
2) Setup <b>eapi.conf</b>
```
[connection:sw0]
host: 10.x.xx.xxx
username: admin
password: xxxx
enablepwd: xxxx
port: 443
transport: https
```
3) Install to work with modules or just run the pyrista.py file.
```
sudo python setup.py install
cd pyrista
python pyrista.py
```
4) Navigate to file:///directory-to-folder/pyrista-master/pyrista/output/switch.html

![Image of Yaktocat](http://s29.postimg.org/iut9mgok7/Screenshot_from_2015_07_10_00_43_02.png )

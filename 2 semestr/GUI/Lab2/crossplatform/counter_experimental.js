(function(){function i(l){var r=document;var m=navigator;var v=window;var y=screen;window.spylog_js=1;var u='<script language="javascript">window.spylog_js=1;<\/script>';u+='<script language="javascript1.1">window.spylog_js=1.1;<\/script>';u+='<script language="javascript1.2">window.spylog_js=1.2;<\/script>';u+='<script language="javascript1.3">window.spylog_js=1.3;<\/script>';u+='<script language="javascript1.4">window.spylog_js=1.4;<\/script>';u+='<script language="javascript1.5">window.spylog_js=1.5;<\/script>';u+='<script language="javascript1.6">window.spylog_js=1.6;<\/script>';u+='<script language="javascript1.7">window.spylog_js=1.7;<\/script>';u+='<script language="javascript1.8">window.spylog_js=1.8;<\/script>';u+='<script language="javascript1.9">window.spylog_js=1.9;<\/script>';u+='<script language="javascript"><\/script>';document.write(u);l._js=window.spylog_js;l._cookie=1;if(!r.cookie){r.cookie="spylog_test=1; path=/";l._cookie=r.cookie?1:0}if(parent!=v){try{l._referrer=parent.document.referrer||""}catch(q){}}if(l._referrer||l._referrer==""){l._frame_referrer=r.referrer||""}else{l._referrer=r.referrer||""}l._location=v.location.href;l._title=r.title;l._frame=(parent.frames&&parent.frames.length>0)?1:0;l._flash="";if(m.plugins&&m.plugins["Shockwave Flash"]){l._flash=m.plugins["Shockwave Flash"].description.split(" ")[2]}else{if(v.ActiveXObject){for(var o=10;o>=2;o--){try{var p=new ActiveXObject("ShockwaveFlash.ShockwaveFlash."+o);if(p){l._flash=o+".0";break}}catch(q){}}}}if(y.colorDepth){l._color_depth=y.colorDepth}else{if(y.pixelDepth){l._color_depth=y.pixelDepth}}if(y.width&&y.height){l._screen=y.width+"x"+y.height}l._java_enabled=(m.javaEnabled()?"Y":"N");l._html5=d();var t=l.counter.toString();var x="u"+b(t.substring(0,t.length-2),3,"0")+"."+t.substring(t.length-2);l._url=((l.ssl||document.location.protocol=="https:")?"https://sec01-hits":"http://"+x)+".spylog.com/cnt";l._url+="?cid="+l.counter;j(l);if(l.track_links=="none"){l.track_links=null}if(l.track_links||l.track_class){h(v,"load",function(){a(l,l._url)})}}function d(){var m="",n,l;l=!!window.HTMLCanvasElement;m+=l?"1":"0";l=(navigator&&navigator.geolocation);m+=l?"1":"0";l=false;try{l=window.localStorage}catch(n){}m+=l?"1":"0";l=!!window.HTMLVideoElement;m+=l?"1":"0";l=!!window.HTMLAudioElement;m+=l?"1":"0";l=!!window.performance;m+=l?"1":"0";return m}function e(m,l,n){var o=(m.pagelevel?"&p="+m.pagelevel:"")+"&c="+m._cookie+"&fr="+m._frame+"&fl="+k(m._flash)+"&px="+m._color_depth+"&sl="+m._js+"&wh="+m._screen+"&j="+m._java_enabled+"&t="+(new Date()).getTimezoneOffset()+"&h5="+m._html5+"&pg="+k(c(m._location,2048/n))+"&r="+k(c(m._referrer,2048/n));if(m._frame_referrer){o+="&r1="+k(c(m._frame_referrer,2048/n))}if(m.part){o+="&partname="+k(m.part.replace(/^\s+/,"").replace(/\s+$/,""))}if(!l&&n<2){o+="&title="+k(c(m._title))}return o}function j(q,n){var m;for(var p=1;p<4;p++){m=e(q,n,p);if(m.length<1800){break}}var l=q._url+m+"&rn="+Math.random();if(n){var o=new Image();o.src=l;o.onload=function(){return}}else{document.write('<a href="'+l+'&f=3" target="_blank"><img src="'+l+'" alt="SpyLOG" border="0"></a>')}}function a(n,l){var m=(navigator.appVersion.indexOf("MSIE")!=-1)?"click":"mousedown";h(document.body,m,function(o){if(!o){o=window.event}g(o,n,l)})}function g(r,p,n){var o;if(r.target){o=r.target}else{if(r.srcElement){o=r.srcElement}}if(o.nodeType==3){o=o.parentNode}var q=o.tagName.toString().toLowerCase();while(o.parentNode&&o.parentNode.tagName&&((q!="a"&&q!="area")||!o.href)){o=o.parentNode;q=o.tagName.toString().toLowerCase()}if(!o.href){return}if(p.track_class){var l=o.className.split("s");for(var m=0;m<l.length;m++){if(l[m]==p.track_class){p._referrer=document.location.href;p._location=o.href;p.pagelevel=3;j(p,1);return}}}if(!p.track_links||(p.track_links=="ext"&&window.location.hostname==o.hostname)){return}p._referrer=document.location.href;p._location=o.href;p.pagelevel=3;j(p,1)}function h(n,l,m){if(n.addEventListener){n.addEventListener(l,m,false)}else{if(n.attachEvent){n.attachEvent("on"+l,m)}}}function c(m,l){if(!m){return m}if(!l){l=250}if(m.length>l){var n=m.indexOf("?");if(n!=-1){m=m.slice(0,n)}}if(m.length>l){m=m.substring(0,l)}return m}function k(o){var p="";var m=o.length;for(var n=0;n<m;n++){var l=o.charCodeAt(n);if(l<128){p+=escape(o.charAt(n));continue}l=l.toString(16);p+="%u"+b(l.toUpperCase(),4,"0")}return p}function b(q,l,p){var o=q.length;if(o>=l){return q}var n=l-o;for(var m=0;m<n;m++){q=p+q}return q}if("undefined"==typeof(spylog_counter)){var f=document.getElementById("spylog_code");if(f){i({counter:f.getAttribute("counter"),pagelevel:f.getAttribute("page_level"),part:f.getAttribute("part"),track_links:f.getAttribute("track_links"),track_class:f.getAttribute("track_class"),ssl:(f.getAttribute("src").substr(0,5)=="https")})}}else{i({counter:spylog_counter,pagelevel:spylog_page_level,part:spylog_part,track_class:("undefined"==typeof(spylog_track_class)?null:spylog_track_class),track_links:spylog_track_links})}window.spylog_tracker=function(m,l){i({counter:m,part:l})}})();
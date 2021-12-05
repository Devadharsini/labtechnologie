'use strict';

window.addEventListener('load', function () {

  console.log("Hello World!");

});

(function(d, m){
    var kommunicateSettings = {"appId":"2b57a98f40d17bdc0060ab574148e0525","popupWidget":true,"automaticChatOpenOnNavigation":true};
    var s = document.createElement("script"); s.type = "text/javascript"; s.async = true;
    s.src = "https://widget.kommunicate.io/v2/kommunicate.app";
    var h = document.getElementsByTagName("head")[0]; h.appendChild(s);
    window.kommunicate = m; m._globals = kommunicateSettings;
})(document, window.kommunicate || {});
/* NOTE : Use web server to view HTML files as real-time update will not work if you directly open the HTML file in the browser. script src="{{ url_for('static', filename='script.js') }}"></script>*/

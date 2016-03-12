"use strict"

function load() {
  var a = document.getElementsByTagName("a"), req = new XMLHttpRequest(), resp
  for (var i = 0; i < a.length; i++)
    if (a[i].href.endsWith("emai1.htm"))
      a[i].onclick = function() {
        if (resp)
          this.href = resp.split(",").reverse().map(function(c, j) {
            return String.fromCharCode((+c + j * 42 + 1) % 256)
          }).join("")
      }
  req.open("GET", "emai1.txt")
  req.onreadystatechange = function() {
    if (req.readyState == 4 && req.status == 200) resp = req.responseText
  }
  req.send()
}

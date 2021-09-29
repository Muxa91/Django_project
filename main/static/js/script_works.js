var request_works = new XMLHttpRequest();
request_works.open('GET', 'http://127.0.0.1:8000/images', false);
request_works.send();
console.log(request_works.responseText)
document.getElementById("works").innerHTML = request_works.responseText ;